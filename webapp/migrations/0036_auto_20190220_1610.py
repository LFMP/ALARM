# Generated by Django 2.1.5 on 2019-02-20 16:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0035_auto_20190220_1609'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recomendacaoacessada',
            name='idClick',
            field=models.ForeignKey(max_length=250, on_delete=django.db.models.deletion.CASCADE, to='webapp.Post'),
        ),
    ]
