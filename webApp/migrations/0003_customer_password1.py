# Generated by Django 3.1 on 2020-08-23 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webApp', '0002_customer'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='password1',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
    ]
