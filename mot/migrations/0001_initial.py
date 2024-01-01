# Generated by Django 4.2 on 2023-12-01 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('orthographe', models.TextField(max_length=32)),
                ('signification', models.TextField()),
                ('traduction_ang', models.TextField(max_length=48)),
                ('traduction_mat', models.TextField(max_length=48)),
                ('context', models.TextField(max_length=32)),
                ('exemple', models.TextField()),
            ],
        ),
    ]
