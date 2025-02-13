from django.db import models


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


class SubmissionsWater(models.Model):
    adress = models.CharField(max_length=200)
    date = models.DateTimeField("Date of submission")


class SubmissionsElectricity(models.Model):
    adress = models.CharField(max_length=200)
    date = models.DateTimeField("Date of submission")
    data = models.IntegerField()


class Access(models.Model):
    login = models.CharField(max_length=200)


class Users(models.Model):
    login = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
