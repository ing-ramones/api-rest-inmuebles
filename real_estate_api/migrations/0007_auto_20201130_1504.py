# Generated by Django 3.1.3 on 2020-11-30 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('real_estate_api', '0006_auto_20201129_2037'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='estate',
            options={'ordering': ['-id'], 'verbose_name': 'Estate', 'verbose_name_plural': 'Estates'},
        ),
        migrations.RemoveField(
            model_name='company',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='company',
            name='last_modified_by',
        ),
        migrations.RemoveField(
            model_name='estate',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='estate',
            name='last_modified_by',
        ),
        migrations.AlterField(
            model_name='company',
            name='name',
            field=models.TextField(max_length=255, unique=True, verbose_name='name'),
        ),
        migrations.AlterField(
            model_name='company',
            name='nif',
            field=models.IntegerField(unique=True, verbose_name='nif'),
        ),
    ]
