from django.shortcuts import render
from django.http import HttpResponse
from account.models import Customer, Barber
from social.models import Comment
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
    TO-BE-COMPLETED
    Get comment list of an image
    :param request:
    :return:
    """
    req = json.loads(request.body)
    img_id = req['pid']

    comments = []
    qs_comment = Comment.objects.filter(img_id=img_id)
    for c in qs_comment:
        c_dict = dict()
        c_dict['text'] = c.text
        qs_customer = Customer.objects.filter(id=c.cid)
        cname = qs_customer[0]
        c_dict['']
        comments.append()

