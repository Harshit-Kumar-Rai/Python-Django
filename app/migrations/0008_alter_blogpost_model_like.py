# Generated by Django 4.1.7 on 2023-07-01 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_alter_blogpost_model_like'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='model_like',
            field=models.IntegerField(default=0),
        ),
    ]
