from django.shortcuts import render
from django.http import HttpResponse
from img_trans.models import HairImg
from account.models import Barber
import json
# Create your views here.


class TrendItems:
    def __init__(self):
        self.number = 0
        self.favor_count = 0
        self.barber_name = None
        self.hair_img_id = None


def get_trend_items(request):
    hair_imgs = HairImg.objects.order_by('-favor_count')[0:10]
    trend_items = []
    number = 1
    for hair_img in hair_imgs:
        item = TrendItems()

        item.number = number
        number += 1
        item.favor_count = hair_img.favor_count
        item.hair_img_id = hair_img.id
        item.barber_name = Barber.objects.filter(id=hair_img.bid)[0].username

        trend_items.append(item)

    json_str = json.dumps(trend_items)
    return HttpResponse(json_str)

