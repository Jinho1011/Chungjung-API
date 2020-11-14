from django.db import models


class Policy(models.Model):
    category = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    sex = models.CharField(max_length=100)
    region = models.CharField(max_length=100)
    edu = models.CharField(max_length=100)
    age = models.CharField(max_length=30)
    # 19-34, if 0: apply for all
    state = models.CharField(max_length=1000, default="")
    benefits = models.CharField(max_length=3000)
    desc = models.CharField(max_length=3000)
    url = models.CharField(max_length=1000, default="")

    def __str__(self):
        return self.title
