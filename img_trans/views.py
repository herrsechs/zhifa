from django.http import HttpResponse
import json
import random
from models import HairImg, HeadImg, SelfieImg
from account.models import Customer, Barber
import logging as log
import swap
# Create your views here.


def index(request):
    return HttpResponse("Hello, wolrd.")


def upload_hair_img(request):
    """
    For a barber to upload a haircut image
    :param request: form-data
                {string} barber_id
                {string} type
                {string} gender
                {file} hair_img
    :return: HttpResponse("Uploaded successfully")
    """
    # logger = log.getLogger('django')
    # logger.info(request.POST)
    # logger.info(request.FILES.getlist('hair_img')[0])

    bid = request.POST['barber_id']
    img = request.FILES.getlist('hair_img')[0]
    if not img:
        img = request.FILES['hair_img']

    if not img:
        return HttpResponse("Image can't be none")

    img_type = request.POST['type']
    gender = request.POST['gender']
    hi = HairImg(bid=bid, img=img, favor_count=0, type=img_type, gender=gender)
    try:
        hi.save()
    except IOError:
        return HttpResponse("Failed to save it in server")

    # logger.debug(hi)
    return HttpResponse("Upload successfully")


def upload_head_img(request):
    """
    For a user to upload head image
    :param request: form-data
                {string} uid
                {string} role
                {file} head_img
    :return: HttpResponse("Upload successfully")
    """

    uid = request.POST['uid']
    role = request.POST['role']
    img = request.FILES.getlist('head_img')[0]
    hi = HeadImg(user_id=uid, role=role, img=img)
    try:
        hi.save()
    except IOError:
        return HttpResponse("Failed to save it in server")
    return HttpResponse("Upload successfully")


def upload_selfie_img(request):
    """
    For a customer to upload selfie image
    :param request: form-data
                {string} cid
                {file} image
    :return: json
                {int} hid
                {int} sid
    """

    cid = request.POST['cid']
    img = request.FILES.get('selfie_img')
    si = SelfieImg(cid=cid, img=img)
    try:
        si.save()
    except IOError:
        return HttpResponse("Failed to save it in server")
    item = {"HAIRCUT": 124, "SELFIE": si.id}
    json_str = json.dumps(item)
    return HttpResponse(json_str)


def get_hair_img(request):
    """
    Get hair image through id
    :param request: JSON string
                {string} pid
    :return:
                HttpResponse(ImageFile)
    """
    req = json.loads(request.body)
    pid = req['pid']
    qs_img = HairImg.objects.filter(id=pid)
    if qs_img.count() == 0:
        return HttpResponse("Hair image " + pid + "does not exist")
    img_model = qs_img[0]
    path = str(img_model.img)
    try:
        with open(path, 'rb') as f:
            return HttpResponse(f.read(), content_type="image/jpeg")
    except IOError:
        return HttpResponse("Fail to load image")


def get_head_img(request):
    """
    Get head image through id
    :param request: JSON string
                {string} pid
    :return:
    """
    req = json.loads(request.body)
    pid = req['pid']
    qs_img = HeadImg.objects.filter(id=pid)
    if qs_img.count() == 0:
        return HttpResponse("Head image" + pid + "does not exist")
    img_model = qs_img[0]
    path = str(img_model.img)
    try:
        with open(path, 'rb') as f:
            return HttpResponse(f.read(), content_type="image/jpeg")
    except IOError:
        return HttpResponse("Fail to load image")


def get_selfie_img(request):
    """
    Get selfie image through id
    :param request:
    :return:
    """
    req = json.loads(request.body)
    pid = req['pid']
    qs_img = SelfieImg.objects.filter(id=pid)
    if qs_img.count() == 0:
        return HttpResponse("Selfie image " + pid + "does not exist")
    img_model = qs_img[0]
    path = str(img_model.img)
    try:
        with open(path, 'rb') as f:
            return HttpResponse(f.read(), content_type="image/jpeg")
    except IOError:
        return HttpResponse("Fail to load image")


def get_recommended_haircuts(request):
    req = json.loads(request.body)
    cid = req['cid']
    hids = random.sample(range(1, 100), 8)
    json_arr = json.dumps(hids)
    return HttpResponse(json_arr)


def get_search_result(request):
    """
    Get haircut ids for a certain search entry
    :param request: JSON string
                {string} gender
                {string} hair_len
    :return: JSON array
    """
    req = json.loads(request.body)
    gender = req['gender']
    hair_len = req['hair_len']
    hids = []
    if gender != '' and hair_len != '':
        qs_img = HairImg.objects.filter(gender=gender)
        if qs_img.count() == 0:
            return HttpResponse("No match result")
        for q in qs_img:
            if q.type == hair_len:
                hids.append(q.id)
    elif gender != '':
        qs_img = HairImg.objects.filter(gender=gender)
        if qs_img.count() == 0:
            return HttpResponse("No match result")
        for q in qs_img:
            hids.append(q.id)
    elif hair_len != '':
        qs_img = HairImg.objects.filter(type=hair_len)
        if qs_img.count() == 0:
            return HttpResponse("No match result")
        for q in qs_img:
            hids.append(q.id)

    if len(hids) > 6:
        hids = random.sample(hids, 6)
    json_str = json.dumps(hids)
    return HttpResponse(json_str)


def get_haircut_info(request):
    """
    Get pic info according to haircut id and customer id
    :param request: JSON string
                {string} hid
                {string} cid
    :return: JSON string
                {string} bid
                {int} favor_count
                {string} barber_name
                {boolean} is_followed
                {boolean} is_favored
    """
    req = json.loads(request.body)
    hid = req['hid']
    cid = req['cid']

    qs_img = HairImg.objects.filter(id=hid)
    if qs_img.count() == 0:
        return HttpResponse("No match haircut image")
    img = qs_img[0]

    qs_customer = Customer.objects.filter(id=cid)
    if qs_customer.count() == 0:
        return HttpResponse("No match customer")
    c = qs_customer[0]

    bid = img.bid
    favor_count = img.favor_count

    qs_barber = Barber.objects.filter(id=bid)
    if qs_barber.count() == 0:
        return HttpResponse("No match barber")
    b = qs_barber[0]

    b_name = b.username
    is_followed = False
    is_favored = True

    followed_barbers = c.followed_barbers.all()
    favored_imgs = c.favored_img.all()

    for fb in followed_barbers:
        if fb.id == bid:
            is_followed = True
            break

    for fi in favored_imgs:
        if fi.id == hid:
            is_favored = True
            break

    result = dict()
    result['bid'] = bid
    result['favor_count'] = favor_count
    result['barber_name'] = b_name
    result['is_followed'] = is_followed
    result['is_favored'] = is_favored
    info_str = json.dumps(result)
    return HttpResponse(info_str)


def change_face(request):
    """
    Change face in two photos
    :param request: JSON string
                {string} sid
                {string} hid
                {string} fname
    :return:
    """
    req = json.loads(request.body)
    sid = req['selfie_id']
    hid = req['hair_id']
    fname = req['file_name']

    qs_s_img = SelfieImg.objects.filter(id=sid)
    if qs_s_img.count() == 0:
        return HttpResponse("Selfie image " + sid + "does not exist")
    s_img_model = qs_s_img[0]
    s_path = str(s_img_model.img)

    qs_h_img = HairImg.objects.filter(id=hid)
    if qs_h_img.count() == 0:
        return HttpResponse("Haircut image " + hid + "does not exist")
    h_img_model = qs_h_img[0]
    h_path = str(h_img_model.img)

    o_path = "/home/clouddata/img/output/" + fname
    swap.wap_face(h_path, s_path, o_path)
    try:
        image = open(o_path, "rb").read()
    except IOError:
        return HttpResponse("Fail to get changed image")
    return HttpResponse(image, content_type="image/jpeg")


