from rest_framework import serializers
from .models import Deck


class DeckSerializer(serializers.ModelSerializer):

    owner = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Deck
        fields = ('created_at',
                  'updated_at',
                  'id',
                  'title',
                  'description',
                  'front_label',
                  'back_label',
                  'owner',
                  'contributors')
