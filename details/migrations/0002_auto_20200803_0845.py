# Generated by Django 2.2.1 on 2020-08-03 03:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('details', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='City',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='details.City'),
        ),
        migrations.AddField(
            model_name='person',
            name='Town',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='details.Town'),
        ),
    ]
