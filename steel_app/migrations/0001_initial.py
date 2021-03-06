# Generated by Django 2.1.4 on 2018-12-10 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Steel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('steel_type', models.CharField(max_length=50)),
                ('heat_treatment', models.CharField(max_length=50)),
                ('heat_temp', models.IntegerField()),
                ('holding_time', models.CharField(max_length=50)),
                ('cooling_media', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to='static/image')),
                ('notes', models.CharField(max_length=150)),
            ],
        ),
    ]
