import json

from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Task(models.Model):
    title = models.TextField()
    complete = models.BooleanField(default=False)
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.title

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)


