from django.db import models


class Policy(models.Model):
    category = models.CharField(max_length=30)
    title = models.CharField(max_length=30)
    sex = models.CharField(max_length=30)
    region = models.CharField(max_length=30)
    age = models.CharField(max_length=30)
    # 19-34, if 0: apply for all
    state = models.CharField(max_length=1000, default="")
    benefits = models.CharField(max_length=1000)
    desc = models.CharField(max_length=1000)
    url = models.CharField(max_length=1000, default="")

    def __str__(self):
        return self.title


class Education(models.Model):
    edu = models.CharField(max_length=30)
    policy = models.ForeignKey('Policy', on_delete=models.CASCADE)

    def __str__(self):
        return self.education
