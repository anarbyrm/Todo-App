from django.db import models
from django.urls import reverse


class Task(models.Model):
    title = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(default=False, editable=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('task_list', kwargs={"pk": self.pk})

        