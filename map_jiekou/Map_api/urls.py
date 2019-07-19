# *_* coding:UTF *_*
# author :v_zhangjunjie02
# 开发时间 ：2019-07-18 19:57

from django.conf.urls import url,include

from . import seriallzers
urlpatterns = [
    url(r'^a/', include(seriallzers.router.urls)),
    #url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

