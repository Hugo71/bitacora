# Generated by Django 4.2.4 on 2023-09-20 21:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bitacora', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actividad',
            name='fecha',
            field=models.DateField(null=True),
        ),
    ]
