# Generated by Django 3.2 on 2021-05-07 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('readdataapp', '0008_auto_20210507_1655'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='writer_copied',
        ),
        migrations.AlterField(
            model_name='comment',
            name='created_at',
            field=models.TextField(default=1620406628.7648673),
        ),
        migrations.AlterField(
            model_name='profile',
            name='created_at',
            field=models.TextField(default=1620406628.7645187),
        ),
    ]
