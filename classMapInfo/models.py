from django.db import models


# Create your models here.
class ClassMapInfo(models.Model):
    className = models.TextField()
    message = models.TextField()
    danceHallName = models.TextField()
    mapUrl = models.TextField()

    def publish(self):
        self.save()

    def __str__(self):
        return "{} : {}".format(self.id, self.className)


class Message(models.Model):
    text = models.TextField()


class Photo(models.Model):
    url = models.TextField()
    width = models.TextField()
    height = models.TextField()


class MessageButton(models.Model):
    label = models.TextField()
    url = models.TextField()


class KakaoPlusFriendResponse:
    a = models.TextField()
