# Generated by Django 2.1.5 on 2019-02-20 01:32

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0024_auto_20190219_1433'),
    ]

    operations = [
        migrations.AddField(
            model_name='recomendacaoacessada',
            name='date',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='post',
            name='dateR',
            field=models.TextField(max_length=250),
        ),
        migrations.AlterField(
            model_name='recomendacaoacessada',
            name='idClick',
            field=models.ForeignKey(max_length=250, on_delete=django.db.models.deletion.CASCADE, to='webapp.Post'),
        ),
    ]
