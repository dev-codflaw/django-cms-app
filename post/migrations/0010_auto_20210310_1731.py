# Generated by Django 2.2 on 2021-03-10 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0009_auto_20210310_1208'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='media/cat_images'),
        ),
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='media/posts'),
        ),
    ]