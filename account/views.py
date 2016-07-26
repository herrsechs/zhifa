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
    :return: "success": save successfully
    """
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


def login(request):
    """
    For user to log in
    :param request: JSON string "username" "password" "role"
    :return: "success": valid usn and pwd
              "user not exist": no matching usn
              "wrong password": invalid pwd
              "No such role":
    """
    req = json.loads(request.body)
    usn = req['username']
    pwd = req['password']
    role = req['role']
    if cmp(role, 'Customer') == 0:
        user = Customer.objects.filter(username=usn)
        return HttpResponse(validateLogin(user, pwd))
    elif cmp(role, 'Barber') == 0:
        user = Barber.objects.filter(username=usn)
        return HttpResponse(validateLogin(user, pwd))
    else:
        return HttpResponse("No such role")


def test(request):
    return render_to_response('test.html')


def validateLogin(user, pwd):
    """
    Validate usn and pwd for customer and barber
    :param user: model Customer or Barber
    :param pwd: string
    :return: string
    """
    if user is None:
        return "user not exist"
    if cmp(pwd, user.password) == 0:
        return "success"
    else:
        return "wrong password"
