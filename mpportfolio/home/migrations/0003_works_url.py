# Generated by Django 3.0.6 on 2020-05-14 18:18

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20200514_2346'),
    ]

    operations = [
        migrations.AddField(
            model_name='works',
            name='url',
            field=models.URLField(default=django.utils.timezone.now, max_length=256),
            preserve_default=False,
        ),
    ]
