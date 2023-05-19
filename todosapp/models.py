from django.db import models
from datetime import datetime, timedelta
from django.contrib.auth import get_user_model
User = get_user_model()

class Todos(models.Model):
    name_of_todo = models.CharField(max_length=100, verbose_name="Название")
    description = models.TextField(max_length=2000, verbose_name="Описание")
    is_done = models.BooleanField(default=False, verbose_name="Сделано")
    date = models.DateTimeField(auto_now=True, verbose_name="Дата создания")
    deadline = models.DateTimeField(default = datetime.now() + timedelta(days=1), verbose_name="Дата дедлайна")
    author = models.ForeignKey(User, null=True, verbose_name='Автор', on_delete=models.CASCADE)

    class Meta:
           ordering = ('-date', 'is_done')
