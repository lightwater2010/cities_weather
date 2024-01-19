# Generated by Django 4.2.5 on 2023-09-24 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('weather', '0002_remove_weathers_category_delete_categories_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Weather_Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('region', models.TextField()),
                ('country', models.CharField(max_length=100)),
                ('temp', models.FloatField()),
                ('descriprion', models.TextField()),
                ('icon_desc', models.TextField()),
                ('wind_speed_kph', models.FloatField()),
                ('wind_speed_mph', models.FloatField()),
                ('humidity', models.FloatField()),
                ('gust_kph', models.FloatField()),
                ('gust_mph', models.FloatField()),
            ],
        ),
    ]