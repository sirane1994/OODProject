# Generated by Django 2.2.6 on 2019-12-02 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Events', '0002_auto_20191201_0611'),
    ]

    operations = [
        migrations.AddField(
            model_name='eventinfo',
            name='slug',
            field=models.SlugField(default=7, max_length=255, unique=True),
            preserve_default=False,
        ),
    ]