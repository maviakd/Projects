# Generated by Django 3.1.6 on 2021-05-08 21:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0069_auto_20210508_2136'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ivk',
            name='iv',
            field=models.TextField(default=b'\x12\xdc\xac\xa3\x1e\r\x94\x0bE\x1bd\xa5B\x1c\xf7\x9d\x1b2^m\xb2\x890\xc4\xe5\xde\xf5I\x061\xe6\xa5'),
        ),
    ]
