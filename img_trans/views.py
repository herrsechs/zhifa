from django.shortcuts import render
from django.http import HttpResponse
from django.core.files.uploadedfile import SimpleUploadedFile
from django import forms
from models import HairImg, HeadImg, SelfieImg
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
    img = request.FILES.getlist('selfie_img')[0]
    si = SelfieImg(cid=cid, img=img)
    si.save()
    return HttpResponse("Upload successfully")