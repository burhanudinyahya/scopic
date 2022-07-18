from rest_framework import serializers 

from ..models.player_skill import PlayerSkill


class PlayerSkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlayerSkill
        fields = ['id', 'skill', 'value', 'player']
        read_only_fields = ['player']
    
    def validate_skill(self, value):
        skills = [
            'defense',
            'attack',
            'speed',
            'strength',
            'stamina'
        ]
        if value.lower() not in skills:
            raise serializers.ValidationError(detail=value)
        return value
