# Generated by Django 4.1 on 2022-08-24 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Online_Test', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='cpp_language',
            fields=[
                ('qno', models.IntegerField(auto_created=True, primary_key=True, serialize=False)),
                ('que', models.CharField(max_length=500)),
                ('optiona', models.CharField(max_length=300)),
                ('optionb', models.CharField(max_length=300)),
                ('optionc', models.CharField(max_length=300)),
                ('optiond', models.CharField(max_length=300)),
                ('ans', models.CharField(max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='java',
            fields=[
                ('qno', models.IntegerField(auto_created=True, primary_key=True, serialize=False)),
                ('que', models.CharField(max_length=500)),
                ('optiona', models.CharField(max_length=300)),
                ('optionb', models.CharField(max_length=300)),
                ('optionc', models.CharField(max_length=300)),
                ('optiond', models.CharField(max_length=300)),
                ('ans', models.CharField(max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='javascript',
            fields=[
                ('qno', models.IntegerField(auto_created=True, primary_key=True, serialize=False)),
                ('que', models.CharField(max_length=500)),
                ('optiona', models.CharField(max_length=300)),
                ('optionb', models.CharField(max_length=300)),
                ('optionc', models.CharField(max_length=300)),
                ('optiond', models.CharField(max_length=300)),
                ('ans', models.CharField(max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='python',
            fields=[
                ('qno', models.IntegerField(auto_created=True, primary_key=True, serialize=False)),
                ('que', models.CharField(max_length=500)),
                ('optiona', models.CharField(max_length=300)),
                ('optionb', models.CharField(max_length=300)),
                ('optionc', models.CharField(max_length=300)),
                ('optiond', models.CharField(max_length=300)),
                ('ans', models.CharField(max_length=1)),
            ],
        ),
        migrations.RenameModel(
            old_name='programmingQ',
            new_name='c_language',
        ),
    ]
