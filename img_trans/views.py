from django.shortcuts import render
from django.http import HttpResponse
from django import forms
# Create your views here.


def index(request):
    return HttpResponse("Hello, wolrd.")


#def UploadHairImgForm(forms.Form):



def upload_hair_img(request):
    """

    :param request:
    :return:
    """