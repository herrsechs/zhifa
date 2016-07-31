from django.shortcuts import render
from django.http import HttpResponse
from account.models import Customer, Barber
import json
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

