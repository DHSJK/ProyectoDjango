# Generated by Django 4.0.4 on 2022-06-13 00:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_alter_producto_stock_delete_stock'),
    ]

    operations = [
        migrations.RenameField(
            model_name='producto',
            old_name='categoria',
            new_name='categoriaProducto',
        ),
        migrations.RenameField(
            model_name='producto',
            old_name='descripcion',
            new_name='descripcionProducto',
        ),
        migrations.RenameField(
            model_name='producto',
            old_name='fotoMascota',
            new_name='fotoProducto',
        ),
        migrations.RenameField(
            model_name='producto',
            old_name='marca',
            new_name='marcaProducto',
        ),
        migrations.RenameField(
            model_name='producto',
            old_name='stock',
            new_name='stockProducto',
        ),
    ]
