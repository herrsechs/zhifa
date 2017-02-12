from django.shortcuts import render
from django.http import HttpResponse
from account.models import Customer, Barber
from social.models import Comment
from social.models import Message
from img_trans.models import HairImg
import json
import logging as log
# Create your views here.


def follow(request):
    """
    Customer follows a barber, save relationship to db
    :param request: JSON string
                    cid: customer id
                    bid: barber id
    :return:
    """
    req = json.loads(request.body)
    cid = req['cid']
    bid = req['bid']

    qs_customer = Customer.objects.filter(id=cid)
    if qs_customer.count() == 0:
        return HttpResponse("customer " + cid + " not exist")
    qs_barber = Barber.objects.filter(id=bid)
    if qs_barber.count() == 0:
        return HttpResponse("barber " + bid + " not exist")

    c = qs_customer[0]
    b = qs_barber[0]

    c.followed_barbers.add(b)
    c.save()

    return HttpResponse("follow successfully")


def follow_list(request):
    """
    Get customer's follow list
    :param request:
            JSON string
            cid: Customer ID
    :return:
            JSON string
            [
                {
                    "username":
                    "gender":
                }
            ]
    """
    req = json.loads(request.body)
    cid = req['cid']
    qs_customer = Customer.objects.filter(id=cid)
    if qs_customer.count() == 0:
        return HttpResponse("customer " + cid + " not exist")
    c = qs_customer[0]

    qs_barber = c.followed_barbers.all()
    if qs_barber.count() == 0:
        return HttpResponse("no followed barber")
    ls_barber = []

    for b in qs_barber:
        dic_barber = dict()
        dic_barber["username"] = b.username
        dic_barber["gender"] = b.gender
        ls_barber.append(dic_barber.copy())

    jstring = json.dumps(ls_barber)
    return HttpResponse(jstring)


def comment(request):
    """
    Customer leaves a comment to an image
    :param request: JSON string
                    {string} cid: Customer ID
                    {string} date: Comment date
                    {string} txt:
                    {string} pid: picture id
    :return:
            HttpResponse('Fail to comment'): when fail to save info
            HttpResponse('Comment successfully')
    """
    req = json.loads(request.body)
    cid = req['cid']
    date = req['date']
    txt = req['txt']
    pid = req['pid']

    try:
        c = Comment(cid=cid, date=date, text=txt, img_id=pid)
        c.save()
    except Exception as e:
        logger = log.getLogger('django')
        logger.error(e)
        return HttpResponse("Fail to comment")

    return HttpResponse("Comment successfully")


def get_img_comment(request):
    """
    Get comment list of an image
    :param request: JSON string:
                {string} pid
    :return:
    """
    req = json.loads(request.body)
    img_id = req['pid']

    comments = []
    qs_comment = Comment.objects.filter(img_id=img_id)
    for c in qs_comment:
        c_dict = dict()
        c_dict['text'] = c.text
        c_dict['date'] = c.date
        qs_customer = Customer.objects.filter(id=c.cid)
        customer = qs_customer[0]
        c_dict['username'] = customer.username
        comments.append(c_dict)

    jstring = json.dumps(comments)
    return HttpResponse(jstring)


def favor_img(request):
    """
    For a customer to favor an image
    :param request: JSON string
                {string} cid: Customer ID
                {string} pid: Hair image ID
    :return:
    """
    req = json.loads(request.body)
    cid = req['cid']
    pid = req['pid']
    qs_img = HairImg.objects.filter(id=pid)
    qs_customer = Customer.objects.filter(id=cid)
    if qs_img.count() == 0:
        return HttpResponse("Image " + str(pid) + "does not exist")
    elif qs_customer.count() == 0:
        return HttpResponse("Customer " + str(cid) + "does not exist")

    img = qs_img[0]
    img.favor_count += 1
    img.save()

    c = qs_customer[0]
    c.favored_img.add(img)
    c.save()
    return HttpResponse("Favor successfully")


def upload_barber_message(request):
    """
    For a barber to leave a message to his fans
    :param request: JSON string
                {string} bid: barber id
                {string} text: message text
    :return:
    """
    req = json.loads(request.body)
    bid = req['bid']
    text = req['text']
    msg = Message(bid=bid, text=text)
    try:
        msg.save()
    except IOError:
        return HttpResponse("Failed to save it in server")
    return HttpResponse("Uploaded successfully!")


def get_customer_message(request):
    """
    For a customer to get messages leaved by barber
    :param request: JSON string
                {string} cid: Customer id
    :return:
    """
    req = json.loads(request.body)
    cid = req['cid']
    qs_customer = Customer.objects.filter(id=cid)
    if qs_customer.count() == 0:
        return HttpResponse("customer " + cid + " not exist")
    c = qs_customer[0]

    qs_barber = c.followed_barbers.all()
    if qs_barber.count() == 0:
        return HttpResponse("no followed barber")

    msg_list = []
    for b in qs_barber:
        msgs = Message.objects.filter(bid=b.id)
        for msg in msgs:
            item = dict()
            item['barber_id'] = b.id
            item['barber_name'] = b.username
            item['text'] = msg.text
            msg_list.append(item)

    json_str = json.dumps(msg_list)
    return HttpResponse(json_str)
