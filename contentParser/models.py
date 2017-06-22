from django.db import models


# Create your models here.
class KakaoPlusFriendMessage(models.Model):
    user_key = models.TextField()
    type = models.TextField()
    content = models.TextField()

    def __str__(self):
        return "{} : {}".format(self.id, self.type, self.content)
