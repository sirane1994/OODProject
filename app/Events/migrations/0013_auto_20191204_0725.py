# Generated by Django 2.2.6 on 2019-12-04 07:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Events', '0012_remove_eventinfo_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventinfo',
            name='EventLocation',
            field=models.CharField(max_length=200),
        ),
    ]
