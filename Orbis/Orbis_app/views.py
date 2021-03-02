from django.shortcuts import render
from django.http import JsonResponse, HttpResponseNotFound, HttpResponseServerError, HttpResponseBadRequest
from .models import Essence
from django.core import exceptions

# Create your views here.
def set_json(request, id = None):
    if request.method == "GET":
        try:
            if id is None or int(id) == 0:
                all_objects = Essence.objects.all()
                obj_list = [obj.get_fields() for obj in all_objects]
                return JsonResponse({"objects": obj_list}, json_dumps_params={"indent": 4})

            id = int(id)
            object = Essence.objects.get(id = id)
            return JsonResponse(object.get_fields(), json_dumps_params={"indent": 4})

        except exceptions.ObjectDoesNotExist:
            return HttpResponseNotFound('<h1>404 Not found</h1><h3>Object not found</h3>')
        except ValueError:
            return HttpResponseBadRequest("<h1>400 Bad request</h1><h3>Expected number after <i>object/</i></h3>")
        except Exception:
            return HttpResponseServerError('<h1>500 Server error</h1>')
