# Generated by Django 3.0.4 on 2020-05-29 21:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('job_seeker_app', '0002_auto_20200530_0259'),
    ]

    operations = [
        migrations.AlterField(
            model_name='academicinfo',
            name='degree',
            field=models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, to='job_seeker_app.Degree'),
        ),
    ]
