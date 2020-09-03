# chat/views.py
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import UserGroups
import json

def successRsp(data):
    response = Response(data, status=200)
    return response

def failedRsp(data):
    response = Response(data, status=400)
    return response

@api_view(['GET', 'POST', 'DELETE'])
def createGroupForUser(request):
    body = json.loads(request.body)
    user = body["username"]
    group_name = body["group_name"]
    temp_grp_list = [1,2,3]
    temp_channel_list = []
    channel_name = body["channel_name"]
    UserGroups(username=user,groups=temp_grp_list,channels=temp_channel_list).save()
    return successRsp("data")