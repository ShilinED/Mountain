from django.http import JsonResponse
from .models import PerevalAdded, User
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

@csrf_exempt
def get_pereval(request, id):
    if request.method == "GET":
        try:
            pereval = PerevalAdded.objects.get(pk=id)
            data = {
                "id": pereval.id,
                "beauty_title": pereval.beauty_title,
                "title": pereval.title,
                "other_titles": pereval.other_titles,
                "connect": pereval.connect,
                "add_time": pereval.add_time,
                "user": {
                    "email": pereval.user.email,
                    "fam": pereval.user.fam,
                    "name": pereval.user.name,
                    "otc": pereval.user.otc,
                    "phone": pereval.user.phone
                },
                "coords": {
                    "latitude": pereval.coord.latitude,
                    "longitude": pereval.coord.longitude,
                    "height": pereval.coord.height
                },
                "level": {
                    "winter": pereval.level_winter,
                    "summer": pereval.level_summer,
                    "autumn": pereval.level_autumn,
                    "spring": pereval.level_spring
                },
                "status": pereval.status
            }
            return JsonResponse(data)
        except PerevalAdded.DoesNotExist:
            return JsonResponse({"status": 404, "message": "Not Found"})
    else:
        return JsonResponse({"status": 405, "message": "Method Not Allowed"})

@csrf_exempt
def edit_pereval(request, id):
    if request.method == "PATCH":
        try:
            data = json.loads(request.body)
            pereval = PerevalAdded.objects.get(pk=id)

            # Проверяем, что статус не равен 'new'
            if pereval.status != 'new':
                return JsonResponse({"state": 0, "message": "Cannot edit pereval with status other than 'new'"})

            # Обновляем поля
            pereval.beauty_title = data.get('beauty_title', pereval.beauty_title)
            pereval.title = data.get('title', pereval.title)
            pereval.other_titles = data.get('other_titles', pereval.other_titles)
            pereval.connect = data.get('connect', pereval.connect)
            pereval.level_winter = data.get('level', {}).get('winter', pereval.level_winter)
            pereval.level_summer = data.get('level', {}).get('summer', pereval.level_summer)
            pereval.level_autumn = data.get('level', {}).get('autumn', pereval.level_autumn)
            pereval.level_spring = data.get('level', {}).get('spring', pereval.level_spring)

            pereval.save()

            return JsonResponse({"state": 1, "message": "Pereval updated successfully"})
        except PerevalAdded.DoesNotExist:
            return JsonResponse({"status": 404, "message": "Not Found"})
        except Exception as e:
            return JsonResponse({"state": 0, "message": str(e)})
    else:
        return JsonResponse({"status": 405, "message": "Method Not Allowed"})

@csrf_exempt
def get_user_perevals(request):
    if request.method == "GET":
        try:
            email = request.GET.get('user__email')
            user = User.objects.get(email=email)
            perevals = PerevalAdded.objects.filter(user=user)
            data = []
            for pereval in perevals:
                data.append({
                    "id": pereval.id,
                    "beauty_title": pereval.beauty_title,
                    "title": pereval.title,
                    "other_titles": pereval.other_titles,
                    "connect": pereval.connect,
                    "add_time": pereval.add_time,
                    "coords": {
                        "latitude": pereval.coord.latitude,
                        "longitude": pereval.coord.longitude,
                        "height": pereval.coord.height
                    },
                    "level": {
                        "winter": pereval.level_winter,
                        "summer": pereval.level_summer,
                        "autumn": pereval.level_autumn,
                        "spring": pereval.level_spring
                    },
                    "status": pereval.status
                })
            return JsonResponse(data, safe=False)
        except User.DoesNotExist:
            return JsonResponse({"status": 404, "message": "User Not Found"})
    else:
        return JsonResponse({"status": 405, "message": "Method Not Allowed"})


