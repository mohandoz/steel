# Generated by Django 2.1.4 on 2018-12-10 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('steel_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='steel',
            name='cooling_media',
            field=models.CharField(choices=[('furnace', 'furnace'), ('oil', 'oil'), ('air', 'air'), ('water', 'water')], max_length=50),
        ),
        migrations.AlterField(
            model_name='steel',
            name='heat_temp',
            field=models.CharField(choices=[('1050', '1050'), ('925', '925'), ('885', '885'), ('815', '815'), ('845', '845'), ('900', '900'), ('925', '925'), ('870', '870'), ('880', '880'), ('940', '940'), ('830', '830')], max_length=50),
        ),
        migrations.AlterField(
            model_name='steel',
            name='heat_treatment',
            field=models.CharField(choices=[('austenitizing', 'austenitizing'), ('carburizing', 'carburizing'), ('normalizing', 'normalizing'), ('annealing', 'annealing'), ('quencheing', 'quencheing'), ('carbonitrieding', 'carbonitrieding')], max_length=50),
        ),
        migrations.AlterField(
            model_name='steel',
            name='holding_time',
            field=models.CharField(choices=[('30 min', '30 min'), ('4 hour', '4 hour'), ('2 hour', '2 hour'), ('1 hour', '1 hour'), ('0 hour', '0 hour'), ('11 hour', '11 hour'), ('3 hour', '3 hour'), ('20 min', '20 min'), ('5 min', '5 min'), ('8 hour', '8 hour')], max_length=50),
        ),
        migrations.AlterField(
            model_name='steel',
            name='image',
            field=models.ImageField(upload_to='media/images'),
        ),
        migrations.AlterField(
            model_name='steel',
            name='steel_type',
            field=models.CharField(choices=[('1080', '1080'), ('9310', '9310'), ('8645', '8645'), ('8620', '8620'), ('8617', '8617'), ('6150', '6150'), ('5160', '5160'), ('4620', '4620'), ('4140', '4140'), ('4130', '4130'), ('4118', '4118'), ('4047', '4047')], max_length=50),
        ),
    ]
