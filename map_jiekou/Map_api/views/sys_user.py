# *_* coding:UTF *_*
# author :v_zhangjunjie02
# 开发时间 ：2019-07-20 16:30
from common.models import Sys_user
from rest_framework import serializers
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser


class Sys_user_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Sys_user

        fields = '__all__'



@csrf_exempt
def sys_user_list(request):
    if request.method == 'GET':
        sys_users = Sys_user.objects.all()
        print("aaa")
        serializer = Sys_user_Serializer(sys_users, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = Sys_user_Serializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def sys_user_detail(request,id):

    try:
        sys_user = Sys_user.objects.get(id=id)
        print(sys_user.bd_uid)
        print("bbb")
    except Sys_user.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = Sys_user_Serializer(sys_user)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = Sys_user_Serializer(sys_user, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        sys_user.delete()
        return HttpResponse(status=204)