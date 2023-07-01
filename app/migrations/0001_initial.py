# Generated by Django 4.1.7 on 2023-06-30 03:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BlogPost',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('blog_title', models.CharField(max_length=25)),
                ('author', models.CharField(max_length=25)),
                ('short_desc', models.CharField(max_length=50)),
                ('blog_desc', models.CharField(max_length=1000)),
            ],
        ),
    ]
