# Generated by Django 5.0.7 on 2025-02-11 22:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gallery',
            name='choice_text',
        ),
        migrations.AddField(
            model_name='usefuleinfo',
            name='text',
            field=models.TextField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='usefuleinfo',
            name='title',
            field=models.CharField(default=0, max_length=200),
            preserve_default=False,
        ),
    ]
