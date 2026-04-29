from django.db import models

class TodoList(models.Model):
    title = models.TextField(max_length=200)
    done = models.BooleanField()

    def __str__(self):
        return self.title
