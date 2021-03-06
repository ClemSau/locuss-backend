from rest_framework import serializers
from .models import Card


class CardSerializer(serializers.ModelSerializer):

    class Meta:
        model = Card
        fields = ('created_at',
                  'updated_at',
                  'id',
                  'front_text',
                  'back_text',
                  'deck',)
