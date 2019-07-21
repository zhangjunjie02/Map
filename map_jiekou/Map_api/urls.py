# *_* coding:UTF *_*
# author :v_zhangjunjie02
# 开发时间 ：2019-07-18 19:57

from django.conf.urls import url,include

from Map_api.views import Intelligence_result_log,sys_user
#接口路由
urlpatterns = [
    url(r'^', include(Intelligence_result_log.router.urls)),
    url(r'^', include(sys_user.router.urls)),

]

