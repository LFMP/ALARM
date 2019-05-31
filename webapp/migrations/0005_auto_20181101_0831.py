# Generated by Django 2.1.1 on 2018-11-01 11:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0004_auto_20181017_0922'),
    ]

    operations = [
        migrations.CreateModel(
            name='Adapters',
            fields=[
                ('rid', models.CharField(max_length=250, primary_key=True, serialize=False)),
                ('ativo', models.IntegerField(choices=[(0, 1)], default=0)),
            ],
        ),
        migrations.CreateModel(
            name='RecomendacaoAcessada',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idClick', models.CharField(max_length=250)),
                ('rid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webapp.Adapters')),
            ],
        ),
        migrations.CreateModel(
            name='RecomendacaoGerada',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=250)),
                ('rid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webapp.Adapters')),
            ],
        ),
        migrations.DeleteModel(
            name='recomendacao',
        ),
    ]
