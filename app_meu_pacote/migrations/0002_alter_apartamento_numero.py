# Generated by Django 4.1.7 on 2023-04-27 04:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_meu_pacote', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apartamento',
            name='numero',
            field=models.CharField(max_length=10),
        ),
    ]
