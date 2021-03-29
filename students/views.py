from django.shortcuts import render
from studentsapp.models import student
from django.http import HttpResponse

import logging
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.http.request import HttpRequest
from django.http.response import HttpResponse, HttpResponseBadRequest
from linebot import LineBotApi, WebhookHandler

logger = logging.getLogger("django")

"""
line_bot_api = LineBotApi(settings.CHANNEL_ACCESS_TOKEN)
parser  = WebhookParser(settings.LINE_CHANNEL_SECRET)
"""
app = Flask(__name__)

# 必須放上自己的Channel Access Token
line_bot_api = LineBotApi('Ri9lT/qq4uCbWEAUeUJR2p6203jYy/gdHVJGKS2KrCmb20hfJZQArZdxQOUVy0cZZrAj5RGKMd19PxDngXFx83QMgzIEuVBFId2G4+XZzYQ7xrXRVuRIg45MCtn0Ye4scl+hwgQ+krG1W///mbw6/wdB04t89/1O/w1cDnyilFU=
')
# 必須放上自己的Channel Secret
handler = WebhookHandler('63add4ec777a184c8fac20f2b171fa82')

line_bot_api.push_message('Ubbd823b1d50c5d24216d3cfb2fd0f374', TextSendMessage(text='你可以開始了'))
