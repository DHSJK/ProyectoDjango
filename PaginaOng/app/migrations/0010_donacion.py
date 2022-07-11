# Generated by Django 4.0.4 on 2022-07-05 20:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_alter_organizacion_fotoong'),
    ]

    operations = [
        migrations.CreateModel(
            name='Donacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreDonador', models.CharField(max_length=50)),
                ('correoDonador', models.EmailField(max_length=254)),
                ('fechaDonacion', models.DateField()),
                ('monto', models.IntegerField(choices=[[0, 1000], [1, 2000], [2, 5000], [3, 10000], [4, 20000]])),
                ('ong', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.organizacion')),
            ],
        ),
    ]