# *_* coding:UTF *_*
# author :v_zhangjunjie02
# 开发时间 ：2019-07-18 19:57

from django.conf.urls import url
from Map_api.views import Intelligence_result_log,sys_user

urlpatterns = [

    url('intelligence_result_log_all/', Intelligence_result_log.isl_list),
    url('intelligence_result_log/(?P<id>[0-9]+)$', Intelligence_result_log.isl_detail),

    url(r'^sys_user_all/', sys_user.sys_user_list),
    url(r'^sys_user/(?P<id>[0-9]+)$', sys_user.sys_user_detail),

]

