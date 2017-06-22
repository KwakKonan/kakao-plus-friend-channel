from rest_framework import serializers
from contentParser.models import KakaoPlusFriendMessage


class KakaoPlusFriendMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = KakaoPlusFriendMessage
        fields = ('user_key', 'type', 'content')
