# Generated by Django 2.2 on 2021-03-10 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carousel', '0002_auto_20210310_1731'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carouselslide',
            name='slide_img',
            field=models.ImageField(upload_to='carousel/slider'),
        ),
    ]
