# Generated by Django 3.0.2 on 2021-07-16 11:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0006_auto_20210712_1025'),
    ]

    operations = [
        migrations.RenameField(
            model_name='match',
            old_name='home',
            new_name='homes',
        ),
    ]
