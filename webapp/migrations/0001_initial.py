# Generated by Django 2.1.1 on 2018-09-14 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.CharField(max_length=50)),
                ('idUser', models.CharField(max_length=250)),
                ('idClick', models.CharField(max_length=250)),
                ('classe', models.CharField(max_length=50)),
                ('texto', models.TextField(max_length=250)),
                ('current', models.CharField(max_length=250)),
                ('href', models.CharField(max_length=250)),
                ('timestamp', models.FloatField()),
                ('dateTimestamp', models.IntegerField()),
                ('dateR', models.CharField(max_length=250)),
            ],
        ),
    ]
