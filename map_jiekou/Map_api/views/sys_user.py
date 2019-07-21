# *_* coding:UTF *_*
# author :v_zhangjunjie02
# 开发时间 ：2019-07-20 16:30
from common.models import Sys_user
from rest_framework import routers, serializers, viewsets

# Serializers define the API representation.
class Sys_user_Serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Sys_user

        fields = '__all__'

# ViewSets define the view behavior.
class Sys_user_ViewSet(viewsets.ModelViewSet):
    try:
        queryset = Sys_user.objects.all()
        serializer_class = Sys_user_Serializer
    except Exception as err:
        print(err)

router = routers.DefaultRouter()
router.register(r'sys_user', Sys_user_ViewSet)