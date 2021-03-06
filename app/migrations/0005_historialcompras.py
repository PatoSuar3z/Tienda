# Generated by Django 4.0.4 on 2022-06-27 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_remove_items_carrito_id_producto'),
    ]

    operations = [
        migrations.CreateModel(
            name='HistorialCompras',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_producto', models.CharField(max_length=40)),
                ('precio_producto', models.IntegerField()),
                ('imagen', models.ImageField(null=True, upload_to='items_carrito')),
            ],
            options={
                'db_table': 'db_historialcompras',
            },
        ),
    ]
