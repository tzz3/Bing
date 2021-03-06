# Generated by Django 2.0.5 on 2018-08-26 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('startdate', models.CharField(max_length=8)),
                ('fullstartdate', models.CharField(max_length=12)),
                ('enddate', models.CharField(max_length=8)),
                ('url', models.CharField(max_length=200)),
                ('urlbase', models.CharField(max_length=200)),
                ('copyright', models.CharField(max_length=200)),
                ('copyrightlink', models.CharField(max_length=200)),
                ('title', models.CharField(max_length=200)),
                ('quiz', models.CharField(max_length=200)),
                ('hsh', models.CharField(max_length=200)),
                ('drk', models.CharField(max_length=200)),
                ('top', models.CharField(max_length=200)),
                ('bot', models.CharField(max_length=200)),
                ('hs', models.CharField(max_length=200)),
                ('path', models.CharField(max_length=200)),
            ],
        ),
    ]
