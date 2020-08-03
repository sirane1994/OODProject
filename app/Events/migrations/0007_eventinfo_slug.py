# Generated by Django 2.2.6 on 2019-12-02 09:16

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('Events', '0006_remove_eventinfo_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='eventinfo',
            name='slug',
            field=models.SlugField(default=uuid.uuid1, unique=True),
        ),
    ]