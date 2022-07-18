## /////////////////////////////////////////////////////////////////////////////
## YOU CAN FREELY MODIFY THE CODE BELOW IN ORDER TO COMPLETE THE TASK
## /////////////////////////////////////////////////////////////////////////////

from django.http.response import JsonResponse
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from typing import Any
from rest_framework.parsers import JSONParser
from my_app.serializers.player import PlayerSerializer
from my_app.models.player import Player


def update_player_handler(request: Request, id: Any):
    data = JSONParser().parse(request)
    try:
        player = Player.objects.get(id=id)
    except Player.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = PlayerSerializer(instance=player, data=data)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data, status=status.HTTP_201_CREATED, safe=False)
    return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST, safe=False)

