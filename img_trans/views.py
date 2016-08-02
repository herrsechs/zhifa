from django.shortcuts import render
from django.http import HttpResponse
from django import forms
from models import HairImg
# Create your views here.


class ImgForm(forms.Form):
    bid = forms.CharField()
    img = forms.FileField()


def index(request):
    return HttpResponse("Hello, wolrd.")


def upload_hair_img(request):
    """
    For a barber to upload a haircut image
    :param request: form-data
                {string} barberid
                {file} hair_img
    :return:
    """
    form = ImgForm(request.POST, request.FILES)
    if form.is_valid():
        bid = form.cleaned_data['bid']
        img = form.cleaned_data['img']
        hi = HairImg(barber=bid, img=img, favor_count=0)
        hi.save()
    else:
        return HttpResponse("Upload failed")

    return HttpResponse("Upload successfully")
