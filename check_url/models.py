from django.db import models


class Url(models.Model):
    url = models.URLField()
    status = models.BooleanField()
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.url
