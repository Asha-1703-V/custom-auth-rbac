from django.db import models


class Role(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self): return self.name


class Resource(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self): return self.name


class Action(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self): return self.name


class Permission(models.Model):
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    resource = models.ForeignKey(Resource, on_delete=models.CASCADE)
    action = models.ForeignKey(Action, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('role', 'resource', 'action')

    def __str__(self):
        return f"{self.role}-{self.resource}-{self.action}"
