# Generated by Django 3.1 on 2020-08-25 04:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webApp', '0003_customer_password1'),
    ]

    operations = [
        migrations.CreateModel(
            name='vehicle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=20)),
                ('number', models.CharField(max_length=20)),
                ('owner', models.CharField(max_length=100)),
            ],
        ),
    ]