# *_* coding:UTF *_*
# author :v_zhangjunjie02
# 开发时间 ：2019-07-20 16:22
from common.models import Intelligence_result_log
from rest_framework import routers, serializers, viewsets

# Serializers define the API representation.
class Isl_Serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Intelligence_result_log

        fields = '__all__'

# ViewSets define the view behavior.
class Isl_ViewSet(viewsets.ModelViewSet):
    try:
        queryset = Intelligence_result_log.objects.all()
        serializer_class = Isl_Serializer
    except Exception as err:
        print(err)

router = routers.DefaultRouter()
router.register(r'intelligence_result_log', Isl_ViewSet)
