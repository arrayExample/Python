# Generated by Django 2.0.3 on 2019-06-05 13:41

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20190530_1944'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='body',
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(max_length=150, unique=True),
        ),
    ]