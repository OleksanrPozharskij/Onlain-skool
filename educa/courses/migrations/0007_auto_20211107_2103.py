# Generated by Django 3.1.6 on 2021-11-07 19:03

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0006_auto_20211107_2057'),
    ]

    operations = [
        migrations.AlterField(
            model_name='module',
            name='description',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]
