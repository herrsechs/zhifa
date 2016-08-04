from django.shortcuts import render
from django.http import HttpResponse
from django.core.files.uploadedfile import SimpleUploadedFile
from django import forms
from models import HairImg
import logging as log
# Create your views here.


class ImgForm(forms.Form):
    bid = forms.CharField(label='barber_id')
    img = forms.ImageField(label='hair_img')


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
    logger = log.getLogger('django')
    # logger.info(request.POST)
    # logger.info(request.FILES.getlist('hair_img')[0])

    bid = request.POST['barber_id']
    img = request.FILES.getlist('hair_img')[0]
    hi = HairImg(bid=bid, img=img, favor_count=0)
    hi.save()
    logger.debug(hi)
    #form = ImgForm({'bid': request.POST['barber_id']}, {'img': SimpleUploadedFile('fol.jpg', request.FILES.getlist('hair_img')[0])})
    #logger.info(form.errors)
    #if not form.is_bound:
    #    return HttpResponse("Not bound")
    #if form.is_valid():
    #    bid = form.cleaned_data['bid']
    #    img = form.cleaned_data['img']
    #    hi = HairImg(barber=bid, img=img, favor_count=0)
    #    hi.save()
    #else:
    #    return HttpResponse("Upload failed")

    return HttpResponse("Upload successfully")
