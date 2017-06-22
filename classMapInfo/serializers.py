from rest_framework import serializers
from classMapInfo.models import ClassMapInfo, Message, MessageButton, Photo, KakaoPlusFriendResponse


class ClassMapInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassMapInfo
        fields = ('className', 'message', 'mapUrl')


class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = ('url', 'width', 'height')


class MessageButtonSerializer(serializers.ModelSerializer):
    class Meta:
        model = MessageButton
        fields = ('label', 'url')


class KakaoPlusFriendMessageSerializer(serializers.ModelSerializer):
    # photo = PhotoSerializer(many=False)
    message_button = MessageButtonSerializer(many=False)

    class Meta:
        model = Message
        fields = ('text', 'message_button')
        # fields = ('text', 'photo', 'message_button')

