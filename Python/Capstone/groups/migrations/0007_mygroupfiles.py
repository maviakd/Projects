# Generated by Django 3.1.6 on 2021-05-09 16:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fileshare', '0001_initial'),
        ('groups', '0006_auto_20210321_0541'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyGroupFiles',
            fields=[
                ('files_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='fileshare.files')),
                ('belongs', models.ManyToManyField(to='groups.MyGroup')),
            ],
            bases=('fileshare.files', models.Model),
        ),
    ]