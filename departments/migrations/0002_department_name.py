# Generated by Django 3.2.9 on 2021-11-12 04:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('departments', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='department',
            name='name',
            field=models.CharField(default='dpt', max_length=100),
        ),
    ]
