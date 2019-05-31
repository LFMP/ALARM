# Generated by Django 2.1.5 on 2019-02-20 19:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0032_auto_20190220_1547'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='dateR',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='recomendacaoacessada',
            name='date',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='recomendacaoacessada',
            name='idClick',
            field=models.ForeignKey(max_length=250, on_delete=django.db.models.deletion.CASCADE, to='webapp.Post'),
        ),
        migrations.AlterField(
            model_name='recomendacaogerada',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
