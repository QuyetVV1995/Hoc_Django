from django.db import models
# models là phần ánh xạ cơ sở dữ liệu tu python
# Create your models here.

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    time_pub = models.DateTimeField()
    # Khi luu tru trong database se tu dong co them 1 truong ID


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)    # Cascade: Khi Question xoa, thi Choice cung bi xoa theo
    choice_text = models.CharField(max_length=100)
    vote = models.IntegerField(default=0)

# tao migrations bang command: python manage.py makemigrations
# tao database: python manage.py migrate
