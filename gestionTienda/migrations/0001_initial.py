# Generated by Django 4.2.3 on 2023-07-31 02:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tienda',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('direccionTienda', models.CharField(blank=True, max_length=32, null=True)),
                ('provinciaTienda', models.CharField(blank=True, max_length=32, null=True)),
                ('regionTienda', models.CharField(blank=True, max_length=32, null=True)),
                ('fechaTienda', models.CharField(blank=True, max_length=32, null=True)),
                ('telefonoTienda', models.CharField(blank=True, max_length=32, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcionProducto', models.CharField(blank=True, max_length=32, null=True)),
                ('codigoProducto', models.CharField(blank=True, max_length=32, null=True)),
                ('precioProducto', models.CharField(blank=True, max_length=32, null=True)),
                ('cantidadProducto', models.CharField(blank=True, max_length=32, null=True)),
                ('tiendaProducto', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='gestionTienda.tienda')),
            ],
        ),
    ]
