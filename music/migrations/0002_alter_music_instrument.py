# Generated by Django 4.0.3 on 2022-03-17 03:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='music',
            name='instrument',
            field=models.CharField(max_length=24),
        ),
    ]