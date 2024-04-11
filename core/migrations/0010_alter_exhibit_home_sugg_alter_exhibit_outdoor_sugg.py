# Generated by Django 4.2.9 on 2024-03-14 14:52

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_alter_exhibit_home_sugg_alter_exhibit_outdoor_sugg'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exhibit',
            name='home_sugg',
            field=models.TextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='exhibit',
            name='outdoor_sugg',
            field=models.TextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
