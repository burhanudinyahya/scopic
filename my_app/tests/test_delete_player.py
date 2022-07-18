## /////////////////////////////////////////////////////////////////////////////
## TESTING AREA
## THIS IS AN AREA WHERE YOU CAN TEST YOUR WORK AND WRITE YOUR TESTS
## /////////////////////////////////////////////////////////////////////////////

from rest_framework.test import APITestCase, RequestsClient
from rest_framework.test import APIClient

from django.test import Client

from ..models.player import Player
from ..models.player_skill import PlayerSkill

class DeletePlayerTestCase(APITestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.client = RequestsClient()

    def setUp(self):
        Player.objects.all().delete()
        PlayerSkill.objects.all().delete()

    def test_delete_with_no_token(self):
        response = self.client.delete('http://127.0.0.1:3000/api/player/2')
        self.assertEqual(response.status_code, 401)
    
    def test_delete_with_invalid_token(self):
        token = 'invalid'
        self.client = Client(HTTP_AUTHORIZATION='Bearer ' + token)
        response = self.client.delete('http://127.0.0.1:3000/api/player/2')
        self.assertEqual(response.status_code, 401)

    def test_delete_with_valid_token_and_when_player_exist(self):
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
        token = 'SkFabTZibXE1aE14ckpQUUxHc2dnQ2RzdlFRTTM2NFE2cGI4d3RQNjZmdEFITmdBQkE='
        self.client = Client(HTTP_AUTHORIZATION='Bearer ' + token)
        response = self.client.delete('http://127.0.0.1:3000/api/player/' + str(player['id']))
        self.assertEqual(response.status_code, 200)

    def test_delete_with_valid_token_and_when_player_not_exist(self):
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
        token = 'SkFabTZibXE1aE14ckpQUUxHc2dnQ2RzdlFRTTM2NFE2cGI4d3RQNjZmdEFITmdBQkE='
        self.client = Client(HTTP_AUTHORIZATION='Bearer ' + token)
        response = self.client.delete('http://127.0.0.1:3000/api/player/2')
        self.assertEqual(response.status_code, 404)
