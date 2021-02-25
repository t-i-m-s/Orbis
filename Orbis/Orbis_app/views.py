from django.shortcuts import render
from django.http import JsonResponse
from .models import Essence

# Create your views here.
def set_json(request, id = None):
    if request.method == "GET":
        if id == 0 or id is None:
            all_objects = Essence.objects.all()
            obj_list = [obj.get_fields() for obj in all_objects]
            return JsonResponse({"objects": obj_list}, json_dumps_params={"indent": 4})

        object = Essence.objects.get(id = id)
        return JsonResponse(object.get_fields(), json_dumps_params={"indent": 4})
