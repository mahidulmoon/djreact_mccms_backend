# Generated by Django 3.1.1 on 2021-01-28 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('complain', '0003_auto_20210128_1759'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ratings',
            name='rating',
            field=models.IntegerField(),
        ),
    ]
