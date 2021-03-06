# Generated by Django 4.0.5 on 2022-06-13 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='sleepData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('age', models.IntegerField()),
                ('date', models.DateField()),
                ('hoursSlept', models.IntegerField()),
                ('routine', models.CharField(max_length=20)),
                ('sleepQuality', models.IntegerField()),
            ],
        ),
    ]
