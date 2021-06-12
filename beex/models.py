from django.db import models
from django.contrib.auth import models as auth_models
# Create your models here.


class User(models.Model):
    # bx_user = models.OneToOneField("auth.User", on_delete=models.CASCADE, to_field='username')
    # TODO: valor de username, email clonado
    username = models.CharField(max_length=65)
    email = models.EmailField()
    password = models.CharField(max_length=255)
    fullname = models.CharField(max_length=150)
    identification = models.CharField(max_length=55)
    phone = models.CharField(max_length=35, blank=True, default='')
    age = models.IntegerField(default=18)
    gender = models.CharField(max_length=1)
    estatus = models.CharField(max_length=3)
    #TODO: relacion con grupos
    metadata = models.JSONField()

    def save(self, *args, **kwargs):
        print(args)
        try:
            super(User, self).save(*args, **kwargs)
        except Exception as e:
            print(e)

    def get(self, *args, **kwargs):
        return super(User, self).objects.get(*args, **kwargs)

