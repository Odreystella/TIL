# Generated by Django 3.2.3 on 2021-05-18 04:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0003_alter_comment_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='created_at',
            field=models.TextField(default=1621312966.0481296),
        ),
        migrations.AlterField(
            model_name='tag',
            name='name',
            field=models.CharField(max_length=64),
        ),
    ]
