from django.contrib.auth.models import AbstractUser
from django.db import models

from django.core.validators import MinValueValidator


class Contacts(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=12)
    description = models.TextField()
    job = models.CharField(max_length=200)


class Gallery(models.Model):
    pass

class Docs(models.Model):
    # text = models.FilePathField()
    text = models.TextField()
    date = models.DateTimeField()


class News(models.Model):
    date = models.DateTimeField()
    title = models.CharField(max_length=200)
    text = models.TextField()


class UsefuleInfo(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    date = models.DateTimeField()


class SubmissionsElectricity(models.Model):
    adress = models.CharField(max_length=200)
    date = models.DateTimeField("Date of submission")
    data = models.IntegerField()


class User(AbstractUser):
    email = models.EmailField(unique=True)

    def __str__(self):
        if self.first_name == '' or self.last_name == '':
            return self.email
        return '{0} {1}'.format (self.first_name, self.last_name)
        


class LandPlot(models.Model):
    street = models.CharField(max_length=20, help_text= 'Улица')
    house_number = models.IntegerField(validators = [MinValueValidator(0)], help_text = 'Номер дома')
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    DISTRICTS = (
        (1, 'Участки первой очереди'),
        (2, 'Участки второй очереди'),
        (3, 'Участки третьей очереди'),
    )

    district = models.IntegerField(choices = DISTRICTS, help_text = 'Очередь участка')

    def water_meters(self):
        return WaterMeter.objects.filter(land_plot__id=self.id)

    def __str__(self):
        return '{0}, {1}'.format (self.street, self.house_number)

    class Meta:
        unique_together = ('street', 'house_number',)
        ordering = ["district", "street", 'house_number']
        

class WaterMeter(models.Model):
    reg_number = models.IntegerField(validators = [MinValueValidator(0)], help_text = 'Номер счетчика ОКОС', null=True)
    land_plot = models.ForeignKey(LandPlot, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField("Дата добавления счетчика")

    def water_submissions(self):
        return WaterSubmission.objects.filter(water_meter__id=self.id)

    class Meta:
        ordering = ['id']


class WaterSubmission(models.Model):
    value = models.IntegerField(validators = [MinValueValidator(0)], help_text = 'Показания счетчика')
    water_meter = models.ForeignKey(WaterMeter, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField("Дата подачи показаний")

    class Meta:
        ordering = ['created_at']
