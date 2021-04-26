# Generated by Django 3.2 on 2021-04-26 15:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, unique=True)),
                ('location', models.CharField(max_length=250)),
                ('address', models.CharField(max_length=250)),
                ('date_of_event', models.DateField()),
                ('description_of_event', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Case',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('case_number', models.CharField(max_length=25, unique=True)),
                ('personal_id', models.CharField(max_length=25, unique=True)),
                ('date_of_birth', models.DateField()),
                ('date_of_onset', models.DateField()),
                ('date_of_test', models.DateField()),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sse_finder.location')),
            ],
        ),
    ]
