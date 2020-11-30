# Generated by Django 3.1.3 on 2020-11-29 20:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('real_estate_api', '0003_auto_20201129_2033'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estate',
            name='company',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='estate', to='real_estate_api.company'),
        ),
    ]
