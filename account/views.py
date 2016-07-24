from django.shortcuts import render_to_response
from django.http import HttpResponse
from models import Customer, Barber
from django.template.loader import get_template
import json


def register(request):
    """
    Save account info into db for customer and barber
    :param request: member raw_post_data should be raw json string,
                     with key username, password, gender, role
    :return: success: save successfully
    """
    print "Body: " + request.body
    req = json.loads(request.body)
    usn = req['username']
    pwd = req['password']
    gd = req['gender']

    if cmp(req['role'], 'Customer') == 0:
        c = Customer(username=usn, password=pwd, gender=gd)
        c.save()
        return HttpResponse("success")
    else:
        b = Barber(username=usn, password=pwd, gender=gd)
        b.save()
        return HttpResponse("success")


def test(request):
    return render_to_response('test.html')



