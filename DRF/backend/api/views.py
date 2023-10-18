from django.http import JsonResponse
import json


def api_home(request):
    body = request.body
    print(request.GET)
    print(request.POST)
    data = {}
    try:
        data = json.loads(body)
    except:
        pass
    print(data)
    data['params'] = dict(request.GET)
    data['headers'] = dict(request.headers)
    data['content_type'] = request.content_type
    return JsonResponse(data)
