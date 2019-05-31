# Generated by Django 2.1.5 on 2019-02-26 11:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0036_auto_20190220_1610'),
    ]

    operations = [
        migrations.AddField(
            model_name='adapters',
            name='erro',
            field=models.IntegerField(choices=[(1, 0)], default=0),
        ),
        migrations.AlterField(
            model_name='recomendacaoacessada',
            name='idClick',
            field=models.ForeignKey(max_length=250, on_delete=django.db.models.deletion.CASCADE, to='webapp.Post'),
        ),
    ]
