# Generated by Django 2.2 on 2021-03-06 14:14

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0003_auto_20210306_1353'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='description',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]