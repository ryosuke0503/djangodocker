# Generated by Django 3.0.2 on 2021-07-16 11:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0007_auto_20210716_1153'),
    ]

    operations = [
        migrations.RenameField(
            model_name='match',
            old_name='homes',
            new_name='home',
        ),
    ]
