## /////////////////////////////////////////////////////////////////////////////
## YOU CAN FREELY MODIFY THE CODE BELOW IN ORDER TO COMPLETE THE TASK
## /////////////////////////////////////////////////////////////////////////////

from requests import Response
from rest_framework.decorators import permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
from ...authentication import BearerAuthentication
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from typing import Any
from rest_framework.parsers import JSONParser
from my_app.models.player import Player

@authentication_classes([BearerAuthentication])
@permission_classes([IsAuthenticated])
def delete_player_handler(request: Request, id: Any):
    try:
        player = Player.objects.get(id=id)
    except Player.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    opr = player.delete()
    if opr:
        return Response(status=status.HTTP_200_OK)  
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)  