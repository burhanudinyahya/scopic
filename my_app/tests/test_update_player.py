## /////////////////////////////////////////////////////////////////////////////
## TESTING AREA
## THIS IS AN AREA WHERE YOU CAN TEST YOUR WORK AND WRITE YOUR TESTS
## /////////////////////////////////////////////////////////////////////////////

from rest_framework.test import APITestCase, RequestsClient

from ..models.player import Player
from ..models.player_skill import PlayerSkill

class UpdatePlayerTestCase(APITestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.client = RequestsClient()

    def setUp(self):
        Player.objects.all().delete()
        PlayerSkill.objects.all().delete()

    def test_update_player_found(self):
        # create 
        data_create = {
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
        response_player = self.client.post('http://127.0.0.1:3000/api/player', data=data_create, format='json')
        player = response_player.json()

        data_update = {
            'name': 'player name updated',
            'position': 'midfielder',
            'playerSkills': [
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

        res_update = {
            "id": 1,
            "name": "player name updated",
            "position": "midfielder",
            "playerSkills": [
                {
                    "id": 1,
                    "skill": "attack",
                    "value": 60,
                    "player": 1
                },
                {
                    "id": 2,
                    "skill": "speed",
                    "value": 80,
                    "player": 1
                }
            ]
        }

        response = self.client.put('http://127.0.0.1:3000/api/player/' + str(player['id']), data=data_update, format='json')
        self.assertEqual(response.json(), res_update)

    def test_update_player_not_found(self):
        # create 
        data_create = {
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
        response_player = self.client.post('http://127.0.0.1:3000/api/player', data=data_create, format='json')
        player = response_player.json()

        data_update = {
            'name': 'player name updated',
            'position': 'midfielder',
            'playerSkills': [
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

        res_update = {
            "id": 1,
            "name": "player name updated",
            "position": "midfielder",
            "playerSkills": [
                {
                    "id": 1,
                    "skill": "attack",
                    "value": 60,
                    "player": 1
                },
                {
                    "id": 2,
                    "skill": "speed",
                    "value": 80,
                    "player": 1
                }
            ]
        }

        response = self.client.put('http://127.0.0.1:3000/api/player/2', data=data_update, format='json')
        self.assertEqual(response.status_code, 404)
