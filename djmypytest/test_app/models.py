from django.db import models


class ManagerA(models.Manager):

    def do_something(self) -> "ModelB":
        return ModelB.objects.create(movie="There's something about mypy")


class ModelA(models.Model):
    title = models.TextField()

    objects = ManagerA()


class ModelB(models.Model):
    movie = models.TextField()
