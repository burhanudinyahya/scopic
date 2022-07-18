## /////////////////////////////////////////////////////////////////////////////
## TESTING AREA
## THIS IS AN AREA WHERE YOU CAN TEST YOUR WORK AND WRITE YOUR TESTS
## /////////////////////////////////////////////////////////////////////////////

from rest_framework.test import APITestCase, RequestsClient

from ..models.player import Player
from ..models.player_skill import PlayerSkill

class CreatePlayerTestCase(APITestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.client = RequestsClient()

    def setUp(self):
        Player.objects.all().delete()
        PlayerSkill.objects.all().delete()

    def test_save_valid_value(self):
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

        expect = {
            "id": 1,
            "name": "player name 2",
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

        response = self.client.post('http://127.0.0.1:3000/api/player', data=data, format='json')
        self.assertEqual(response.json(), expect)

    def test_invalid_value_for_position(self):
        data = {
            "name": "player name",
            "position": "goalkeeper",
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
        self.assertEqual(response.data, {"message": "Invalid value for position: goalkeeper"})

    def test_invalid_value_for_skill(self):
        data = {
            "name": "player name 2",
            "position": "defender",
            "playerSkills": [
                {
                    "skill": "coding",
                    "value": 60
                },
                {
                    "skill": "speed",
                    "value": 80
                }
            ]
        }

        response = self.client.post('http://127.0.0.1:3000/api/player', data=data, format='json')
        self.assertEqual(response.data, {"message": "Invalid value for skill: coding"})
        