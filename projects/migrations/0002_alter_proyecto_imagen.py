# Generated by Django 4.2.6 on 2023-10-25 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proyecto',
            name='imagen',
            field=models.ImageField(upload_to='projects/images/'),
        ),
    ]
