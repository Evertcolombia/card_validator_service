from rest_framework import serializers
from card_validator.models import CardNumber

class CardNumberSerializer(serializers.ModelSerializer):
    class Meta:
        model = CardNumber
        fields = ('id', 'card_num', 'supplier')
