# Create your views here.
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from classMapInfo.models import ClassMapInfo
from classMapInfo.serializers import ClassMapInfoSerializer, KakaoPlusFriendMessageSerializer
import json


@csrf_exempt
def class_map_info_list(request):

    if request.method == 'GET':
        classMapInfos = ClassMapInfo.objects.all()
        serializer = ClassMapInfoSerializer(classMapInfos, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ClassMapInfoSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def class_map_info_detail(request, className):

    try:
        classMapInfo = ClassMapInfo.objects.get(className=className)
    except ClassMapInfo.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = ClassMapInfoSerializer(classMapInfo)
        return JsonResponse(serializer.data)

    elif request.method == 'POST':
        json_data = ClassMapInfoSerializer(classMapInfo).data

        data = {
            "text": "",
            "photo": {
              "url": "",
              "width": "",
              "height": ""
            },
            "message_button": {
              "label": "",
              "url": ""
            }
        }

        data['text'] = json_data['message']
        data['message_button']['label'] = json_data['message']
        data['message_button']['url'] = json_data['mapUrl']

        res = KakaoPlusFriendMessageSerializer(data)

        a = {}
        a['message'] = res.data
        a['keyboard'] = {
            "type": "text"
        }

        return JsonResponse(json.dumps(a, ensure_ascii=False), safe=False)
