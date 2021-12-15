# Generated by Django 2.2.24 on 2021-10-06 17:10

import courses.fields
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_content_file_image_text_video'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='content',
            options={'ordering': ['order']},
        ),
        migrations.AlterModelOptions(
            name='module',
            options={'ordering': ['order']},
        ),
        migrations.AddField(
            model_name='content',
            name='order',
            field=courses.fields.OrderField(blank=True, default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='module',
            name='order',
            field=courses.fields.OrderField(blank=True, default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='course',
            name='slug',
            field=models.SlugField(default=uuid.uuid1, max_length=200, unique=True),
        ),
    ]
