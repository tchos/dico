# Generated by Django 4.2 on 2023-12-03 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mot', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mot',
            name='context',
            field=models.CharField(max_length=32),
        ),
        migrations.AlterField(
            model_name='mot',
            name='exemple',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='mot',
            name='orthographe',
            field=models.CharField(error_messages='Un mot ne doit pas dépasser 128 caractères !', max_length=32),
        ),
        migrations.AlterField(
            model_name='mot',
            name='signification',
            field=models.TextField(error_messages="L'explication du terme est obligatoire !"),
        ),
        migrations.AlterField(
            model_name='mot',
            name='traduction_ang',
            field=models.CharField(error_messages="L'équivalent en anglais doit avoir au plus 48 caractères !", max_length=48),
        ),
        migrations.AlterField(
            model_name='mot',
            name='traduction_mat',
            field=models.CharField(error_messages="L'équivalent en anglais doit avoir au plus 48 caractères !", max_length=48),
        ),
    ]
