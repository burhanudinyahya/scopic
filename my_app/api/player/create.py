## /////////////////////////////////////////////////////////////////////////////
## YOU CAN FREELY MODIFY THE CODE BELOW IN ORDER TO COMPLETE THE TASK
## /////////////////////////////////////////////////////////////////////////////

from django.http.response import JsonResponse
from rest_framework.request import Request
from rest_framework import status
from rest_framework.parsers import JSONParser
from my_app.serializers.player import PlayerSerializer


def create_player_handler(request: Request):
    data = JSONParser().parse(request)
    serializer = PlayerSerializer(data=data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return JsonResponse(serializer.data, status=status.HTTP_201_CREATED, safe=False)
    return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST, safe=False)
