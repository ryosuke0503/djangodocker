# Generated by Django 3.0.2 on 2021-07-09 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0003_team'),
    ]

    operations = [
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField()),
                ('league', models.CharField(max_length=64)),
                ('kind', models.CharField(max_length=64)),
                ('date', models.CharField(max_length=64)),
                ('time', models.CharField(max_length=64)),
                ('home', models.IntegerField()),
                ('homescore', models.IntegerField()),
                ('awayscore', models.IntegerField()),
                ('away', models.IntegerField()),
                ('stadium', models.CharField(max_length=64)),
                ('viewers', models.IntegerField()),
                ('broadcasts', models.CharField(max_length=64)),
            ],
        ),
    ]