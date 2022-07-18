## /////////////////////////////////////////////////////////////////////////////
## TESTING AREA
## THIS IS AN AREA WHERE YOU CAN TEST YOUR WORK AND WRITE YOUR TESTS
## /////////////////////////////////////////////////////////////////////////////

from rest_framework.test import APITestCase, RequestsClient

from ..models.player import Player
from ..models.player_skill import PlayerSkill

class ListPlayerTestCase(APITestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.client = RequestsClient()

    def setUp(self):
        Player.objects.all().delete()
        PlayerSkill.objects.all().delete()

    def test_list_player(self):
        # create 
        data = {
            "name": "player name 2",
            "position": "midfielder",
            "playerSkills": [
                {
                    "skill": "attack",
                    "value": 60
                },
                {
                    "skill": "speed",
                    "value": 80
                }
            ]
        }
        response = self.client.post('http://127.0.0.1:3000/api/player', data=data, format='json')
        player = response.json()

        response = self.client.get('http://testserver/api/player')
        self.assertEqual(response.json(), [player])
