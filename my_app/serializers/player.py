from rest_framework import serializers

from .player_skill import PlayerSkillSerializer
from ..models.player import Player
from ..models.player_skill import PlayerSkill
from django.utils.translation import gettext_lazy as _

class PlayerSerializer(serializers.ModelSerializer):
    playerSkills = PlayerSkillSerializer(many=True)

    class Meta:
        model = Player
        fields = ['id', 'name', 'position', 'playerSkills']

    def validate_position(self, value):
        positions = [
            'defender',
            'midfielder',
            'forward'
        ]
        if value.lower() not in positions:
            raise serializers.ValidationError(detail=value)
        return value

    def create(self, validated_data):
        skills_data = validated_data.pop('playerSkills')
        player = Player.objects.create(**validated_data)
        for skill_data in skills_data:
            PlayerSkill.objects.create(player=player, **skill_data)
        return player

    def update(self, instance, validated_data):
        skills_data = validated_data.pop('playerSkills')

        playerSkills = instance.playerSkills.all()
        playerSkills = list(playerSkills)

        instance.name = validated_data.get('name', instance.name)
        instance.position = validated_data.get('position', instance.position)
        instance.save()

        for skill_data in skills_data:
            playerSkill = playerSkills.pop(0)
            playerSkill.skill = skill_data.get('skill', playerSkill.skill)
            playerSkill.value = skill_data.get('value', playerSkill.value)
            playerSkill.save()

        return instance
