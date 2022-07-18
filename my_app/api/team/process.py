## /////////////////////////////////////////////////////////////////////////////
## YOU CAN FREELY MODIFY THE CODE BELOW IN ORDER TO COMPLETE THE TASK
## /////////////////////////////////////////////////////////////////////////////

from django.http.response import JsonResponse
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import JSONParser
from my_app.models.player import Player
from my_app.models.player_skill import PlayerSkill
from my_app.serializers.player import PlayerSerializer
from my_app.serializers.player_skill import PlayerSkillSerializer

def team_process_handler(request: Request):
    data = JSONParser().parse(request)

    if len(data) != len(set([x['position'] for x in data])):
        return JsonResponse({'message': 'The position of the player should not be repeated in the request'},
                            status=status.HTTP_400_BAD_REQUEST, safe=False)
    res=None
    for x in data:
        position = x['position']
        main_skill = x['mainSkill']
        num_players = x['numberOfPlayers']
        try:
            players = Player.objects.filter(position=position, playerSkills__skill=main_skill)[:num_players]
            serializer_player = PlayerSerializer(players, many=True)
            if res is None:
                res = serializer_player.data
            else:
                res.append(serializer_player.data)
        except Player.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    return JsonResponse(data=res, status=status.HTTP_200_OK, safe=False)
