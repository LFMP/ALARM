# Generated by Django 2.1.1 on 2018-11-08 10:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0007_auto_20181105_1319'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recomendacaoacessada',
            name='idClick',
            field=models.ForeignKey(max_length=250, on_delete=django.db.models.deletion.CASCADE, to='webapp.Post'),
        ),
        migrations.AlterField(
            model_name='recomendacaoacessada',
            name='idRows',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]