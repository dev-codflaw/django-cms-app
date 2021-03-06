# Generated by Django 2.2 on 2021-03-27 08:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0016_auto_20210327_0755'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(blank=True, help_text='Make your own slug or it will be copy from title.', max_length=250, unique=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(blank=True, help_text='Make your own slug or it will be copy from title.', max_length=250, unique=True),
        ),
    ]
