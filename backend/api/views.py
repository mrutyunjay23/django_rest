import json
from django.http import JsonResponse

def api_home(request, *args, **kwargs):
    body = request.body # In the form of byte string of a dict
    data = {}
    try:
        data = json.loads(body)   # byte string of dict -> JSON format
    except:
        pass
    print(data)
    return JsonResponse(data)