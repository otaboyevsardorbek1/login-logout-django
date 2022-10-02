# Generated by Django 3.0.11 on 2022-10-02 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=40)),
                ('password', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('gender', models.CharField(max_length=15)),
            ],
        ),
    ]