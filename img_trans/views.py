from django.http import HttpResponse
import json
from models import HairImg, HeadImg, SelfieImg
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
                {file} hair_img
    :return: HttpResponse("Uploaded successfully")
    """
    # logger = log.getLogger('django')
    # logger.info(request.POST)
    # logger.info(request.FILES.getlist('hair_img')[0])

    bid = request.POST['barber_id']
    img = request.FILES.getlist('hair_img')[0]
    hi = HairImg(bid=bid, img=img, favor_count=0)
    # Try/Catch need to be added
    hi.save()

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
    hi.save()
    return HttpResponse("Upload successfully")


def upload_selfie_img(request):
    """
    For a customer to upload selfie image
    :param request: form-data
                {string} cid
                {file} image
    :return:
    """

    cid = request.POST['cid']
    img = request.FILES.get('selfie_img')
    si = SelfieImg(cid=cid, img=img)
    si.save()
    return HttpResponse("Upload successfully")


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

def change_face(request):
    """
    Change face in two photos
    :param request:
    :return:
    """
    req = json.loads(request.body)
    sid = req['selfie_id']
    hid = req['hair_id']

    qs_s_img = SelfieImg.objects.filter(id=sid)
    if qs_s_img.count() == 0:
        return HttpResponse("Selfie image " + pid + "does not exist")
    s_img_model = qs_s_img[0]
    s_path = str(s_img_model.img)

    qs_h_img = HairImg.objects.filter(id=hid)
    if qs_h_img.count() == 0:
        return HttpResponse("Haircut image " + hid + "does not exist")
    h_img_model = qs_h_img[0]
    h_path = str(h_img_model.img)

    o_path = "/home/clouddata/img/output/output.jpg"
    swap.wap_face(s_path, h_path, o_path)
    try:
        image = open(o_path, "rb").read()
    except IOError:
        return HttpResponse("Fail to get changed image")
    return HttpResponse(image, content_type="image/jpeg")


