## /////////////////////////////////////////////////////////////////////////////
## TESTING AREA
## THIS IS AN AREA WHERE YOU CAN TEST YOUR WORK AND WRITE YOUR TESTS
## /////////////////////////////////////////////////////////////////////////////

from rest_framework.test import APITestCase, RequestsClient

from ..models.player import Player
from ..models.player_skill import PlayerSkill

class ProcessTeamTestCase(APITestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.client = RequestsClient()

    def setUp(self):
        Player.objects.all().delete()
        PlayerSkill.objects.all().delete()

    def test_process_team(self):
        # create 
        data_create1 = {
            "name": "player name 1",
            "position": "midfielder",
            "playerSkills": [
                {
                    "skill": "speed",
                    "value": 60
                },
                {
                    "skill": "attack",
                    "value": 50
                }
            ]
        }
        response_player1 = self.client.post('http://127.0.0.1:3000/api/player', data=data_create1, format='json')
        # player1 = response_player1.json()
        # create 
        data_create2 = {
            "name": "player name 2",
            "position": "defender",
            "playerSkills": [
                {
                    "skill": "strength",
                    "value": 60
                },
                {
                    "skill": "defense",
                    "value": 50
                }
            ]
        }
        response_player2 = self.client.post('http://127.0.0.1:3000/api/player', data=data_create2, format='json')
        # player2 = response_player2.json()
        data = [
            {
                'position': 'midfielder',
                'mainSkill': 'speed',
                'numberOfPlayers': 1
            },
            {
                "position": "defender",
                "mainSkill": "strength",
                "numberOfPlayers": 1
            }
        ]

        expect = [
                    {
                        "id": 1,
                        "name": "player name 1",
                        "position": "midfielder",
                        "playerSkills": [
                            {
                                "id": 1,
                                "skill": "speed",
                                "value": 60,
                                "player": 1
                            },
                            {
                                "id": 2,
                                "skill": "attack",
                                "value": 50,
                                "player": 1
                            }
                        ]
                    },
                    {
                        "id": 2,
                        "name": "player name 2",
                        "position": "defender",
                        "playerSkills": [
                            {
                                "id": 1,
                                "skill": "strength",
                                "value": 60,
                                "player": 2
                            },
                            {
                                "id": 2,
                                "skill": "defense",
                                "value": 50,
                                "player": 2
                            }
                        ]
                    }
                ]

        response = self.client.post('http://127.0.0.1:3000/api/team/process', data=data, format='json')
        self.assertIsNotNone(response.json(), expect)
