from django.db import models
from category.models import CategoryModel
# Create your models here.
class TaskModel(models.Model):
    task_titel = models.CharField(max_length=50)
    task_description = models.TextField()
    is_completed = models.BooleanField(default=False)
    task_assaign_date = models.DateField()
    task_category = models.ManyToManyField(CategoryModel)

    def __str__(self):
        return self.task_titel