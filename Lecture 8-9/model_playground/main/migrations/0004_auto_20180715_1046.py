# Generated by Django 2.0.7 on 2018-07-15 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_person_nickname'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='nickname',
        ),
        migrations.AlterField(
            model_name='person',
            name='age',
            field=models.IntegerField(blank=True),
        ),
    ]
