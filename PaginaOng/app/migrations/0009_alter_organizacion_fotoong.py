# Generated by Django 4.0.4 on 2022-06-19 04:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_alter_organizacion_fotoong'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organizacion',
            name='fotoOng',
            field=models.ImageField(blank=True, null=True, upload_to='Organizacion'),
        ),
    ]
