# Generated by Django 4.2.9 on 2024-01-21 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projectapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='priority',
            field=models.CharField(choices=[('High', 'High'), ('Medium', 'Medium'), ('Low', 'Low')], default='High', max_length=10),
        ),
    ]
