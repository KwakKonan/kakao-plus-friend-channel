from django.http import HttpResponse
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from contentParser.serializers import KakaoPlusFriendMessageSerializer
import re
from classMapInfo.views import class_map_info_detail

error_msg = '지원되지 않는 질문입니다.'
regex_array = [
    r'.*초급.*강습실.*어디.*',
    r'.*초중급.*강습실.*어디.*',
    r'.*준중급.*강습실.*어디.*',
    r'.*중급.*강습실.*어디.*',
    r'.*공연단.*강습실.*어디.*',
]
class_name = ['초급', '초중급', '준중급', '중급', '공연단']


# Create your views here.
@csrf_exempt
def parse_content(request):

    if request.method == 'POST':
        try:
            data = JSONParser().parse(request)
            serializer = KakaoPlusFriendMessageSerializer(data=data)
            if serializer.is_valid():

                content = data['content']

                for index, value in enumerate(regex_array):
                    pattern = re.compile(value)
                    if pattern.search(content):
                        return class_map_info_detail(request, class_name[index])
            return HttpResponse(status=404, content=error_msg)
        except:
            return HttpResponse(status=404)
    else:
        content = 'GET method is not supported'
        return HttpResponse(content=content)