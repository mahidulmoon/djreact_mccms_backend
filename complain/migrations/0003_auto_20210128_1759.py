# Generated by Django 3.1.1 on 2021-01-28 11:59

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('complain', '0002_auto_20210128_1753'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ratings',
            name='agree',
        ),
        migrations.AddField(
            model_name='ratings',
            name='rating',
            field=models.DecimalField(decimal_places=1, default=1, max_digits=2, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)]),
            preserve_default=False,
        ),
    ]
