# Generated by Django 3.1.6 on 2021-11-07 18:57

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0005_course_students'),
    ]

    operations = [
        migrations.AlterField(
            model_name='text',
            name='content',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]
