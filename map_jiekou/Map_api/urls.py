# *_* coding:UTF *_*
# author :v_zhangjunjie02
# 开发时间 ：2019-07-18 19:57
from django.conf.urls import url,include
from rest_framework import routers, serializers, viewsets
from common.models import Intelligence_result_log

urlpatterns = [
    url(r'^', include(router.urls)),
]
