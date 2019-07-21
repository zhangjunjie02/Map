# *_* coding:UTF *_*
# author :v_zhangjunjie02
# 开发时间 ：2019-07-20 16:22
from common.models import Intelligence_result_log
from rest_framework import routers, serializers, viewsets
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

# Serializers define the API representation.
class Isl_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Intelligence_result_log

        fields = '__all__'


#查看所有数据
@csrf_exempt
def isl_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        ils = Intelligence_result_log.objects.all()
        serializer = Isl_Serializer(ils, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = Isl_Serializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

#指定id,检索，查询，修改，删除
@csrf_exempt
def isl_detail(request,id):

    try:
        ils = Intelligence_result_log.objects.get(id=id)
    except Intelligence_result_log.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = Isl_Serializer(ils)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = Isl_Serializer(ils, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        ils.delete()
        return HttpResponse(status=204)
