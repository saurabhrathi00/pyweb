# chat/views.py
from . import makeMongoConnection
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from pprint import pprint

import json


def successRsp(data):
    response = Response(data, status=200)
    return response


def failedRsp(data):
    response = Response(data, status=400)
    return response


@api_view(['PUT'])
def updateGroupForUser(request, username):
    body = json.loads(request.body)
    group_name = body['group_name']
    db = makeMongoConnection.useDatabase('user_details')
    if db.testing_chat.find({'username': username}).count() == 0 :
        db.testing_chat.insert_one({"username": username, "groups": [group_name], "channels": []})
        return successRsp("Inserted Successfully")
    db.testing_chat.update({'username': username}, {'$push': {'groups': group_name}})
    return successRsp("Inserted Successfully")


@api_view(['GET'])
def getAllForUser(request, username):
    body = json.loads(request.body)
    db = makeMongoConnection.useDatabase('bezkoder_db')
    result = db.testing_chat.find({'username': username})
    pprint(result)
    return successRsp("data")
