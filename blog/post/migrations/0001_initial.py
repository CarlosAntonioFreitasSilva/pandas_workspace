# Generated by Django 4.2.4 on 2023-08-12 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Posts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('text', models.TextField()),
                ('author', models.CharField(max_length=30)),
                ('date', models.DateField()),
            ],
        ),
    ]
