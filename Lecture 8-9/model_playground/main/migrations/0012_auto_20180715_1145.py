# Generated by Django 2.0.7 on 2018-07-15 11:45

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_auto_20180715_1143'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='age',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(150)]),
        ),
    ]
