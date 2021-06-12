import json
import types
from io import BufferedReader, TextIOWrapper
from django.conf.urls import url
from django.core.handlers.wsgi import WSGIRequest, LimitedStream
from django.http import HttpResponse
from django.urls import ResolverMatch, URLResolver
from django.urls.resolvers import RoutePattern
from beex import views
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404, redirect
from beex.models import User as Beex_user
from beex.serializer import BeexUserSerializer
response_result = {'message': "Error!", 'result': {}}
success_message = "OK"

def LoginViewSet(request):
    global response_result
    parameters = get_parameters(request)
    response_result["message"] = "No se reconoce el usuario!"
    if "username" not in parameters:
        json_data = json.dumps(response_result, indent=4)
        return HttpResponse(json_data, content_type="application/json")
    p_username = parameters['username']
    print(parameters)
    beex_user_objects = Beex_user.objects
    response_result["message"] = "El usuario no ha sido registrado!"
    is_username = {}
    if beex_user_objects.all():
        is_username = beex_user_objects.get(username=p_username)
        response_result["result"] = is_username.__dict__
        response_result["message"] = success_message
    print(response_result)
    json_data = json.dumps(response_result, indent=4)
    return HttpResponse(json_data, content_type="application/json")


def get_parameters(request):
    dict_request = request.__dict__
    query_string = dict_request['environ']['QUERY_STRING']
    parameters = {val.split("=")[0]: val.split("=")[1] for val in query_string.split(",") if "=" in val}
    return parameters


urlpatterns = [
    url('', LoginViewSet, name='login')
]