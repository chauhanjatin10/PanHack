# Generated by Django 2.0.4 on 2019-01-19 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('object', '0005_auto_20190119_1628'),
    ]

    operations = [
        migrations.AddField(
            model_name='queryimage',
            name='aadhar',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AlterField(
            model_name='queryimage',
            name='lat',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AlterField(
            model_name='queryimage',
            name='long',
            field=models.CharField(default='', max_length=500),
        ),
    ]
