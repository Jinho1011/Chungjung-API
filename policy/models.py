from django.db import models


class Policy(models.Model):
    category = models.CharField(max_length=30)
    title = models.CharField(max_length=30)
    sex = models.CharField(max_length=30)
    region = models.CharField(max_length=30)
    edu = models.ForeignKey('Education', on_delete=models.CASCADE)
    age = models.CharField(max_length=30)
    # 19-34, if 0: apply for all
    state = models.ForeignKey('State', on_delete=models.CASCADE)
    benefits = models.CharField(max_length=1000)
    desc = models.CharField(max_length=1000)

    def __str__(self):
        return self.title


class Education(models.Model):
    education = models.CharField(max_length=30)


class State(models.Model):
    stat = models.CharField(max_length=30)