# Generated by Django 3.2.3 on 2021-05-17 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0002_auto_20210517_1326'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='created_at',
            field=models.TextField(default=1621270650.571877),
        ),
    ]