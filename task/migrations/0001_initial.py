# Generated by Django 3.0.4 on 2020-03-10 21:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Model1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('param1', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Model2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('param2', models.CharField(max_length=20)),
            ],
        ),
    ]