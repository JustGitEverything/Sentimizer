# Generated by Django 4.0.4 on 2022-04-26 20:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='diaryentry',
            name='title',
            field=models.CharField(default='No Title', max_length=20),
        ),
    ]
