# Generated by Django 4.0.4 on 2022-05-24 02:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('family', '0003_alter_family_dni'),
    ]

    operations = [
        migrations.AlterField(
            model_name='family',
            name='DNI',
            field=models.CharField(max_length=8, unique=True),
        ),
    ]
