from django.shortcuts import render
from django.http import HttpResponse
import json

# Create your views here.
def testResponse(request):
    data = {
        "type": "buttons",
        "buttons": ["선택 1", "선택 2", "선택 3"]
    }
    print()
    return HttpResponse(json.dumps(data), status=200)
