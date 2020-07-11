from django.db import models


class ManagerA(models.Manager):

    def do_something(self, other_obj: "ModelB"):
        return None


class ModelA(models.Model):
    title = models.TextField()

    objects = ManagerA()


class ModelB(models.Model):
    movie = models.TextField()
