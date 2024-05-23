from django.http import JsonResponse
from .models import User, Coords, PerevalAdded, PerevalImages
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def submit_data(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            return JsonResponse({"status": 200, "message": "Отправлено успешно", "id": 42})
        except Exception as e:
            return JsonResponse({"status": 500, "message": str(e), "id": None})
    else:
        return JsonResponse({"status": 400, "message": "Bad Request", "id": None})

