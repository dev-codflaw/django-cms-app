# Generated by Django 2.2 on 2021-03-10 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0010_auto_20210310_1731'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='category/images'),
        ),
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='posts/images'),
        ),
    ]