# Generated by Django 2.1.5 on 2019-01-30 17:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0015_auto_20190130_1651'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recomendacaoacessada',
            name='idClick',
            field=models.ForeignKey(max_length=250, on_delete=django.db.models.deletion.CASCADE, to='webapp.Post'),
        ),
        migrations.AlterField(
            model_name='recomendacaogerada',
            name='idClick',
            field=models.ForeignKey(default=0, max_length=250, on_delete=django.db.models.deletion.CASCADE, to='webapp.Post'),
        ),
    ]
