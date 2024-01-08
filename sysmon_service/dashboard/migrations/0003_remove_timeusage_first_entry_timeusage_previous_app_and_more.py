# Generated by Django 4.2.7 on 2023-11-06 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_timeusage_first_entry'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='timeusage',
            name='first_entry',
        ),
        migrations.AddField(
            model_name='timeusage',
            name='previous_app',
            field=models.CharField(default=None, max_length=500),
        ),
        migrations.AddField(
            model_name='timeusage',
            name='previous_url',
            field=models.CharField(default=None, max_length=2000),
        ),
        migrations.AlterField(
            model_name='timeusage',
            name='usage_json',
            field=models.JSONField(default=dict),
        ),
    ]
