# Generated by Django 5.0.2 on 2024-06-24 20:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('email', models.EmailField(max_length=100, unique=True)),
                ('phone', models.CharField(max_length=11, unique=True)),
                ('address', models.CharField(max_length=200)),
            ],
        ),
    ]
