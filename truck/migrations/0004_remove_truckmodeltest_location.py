# Generated by Django 4.2.1 on 2023-05-24 19:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('truck', '0003_alter_truckmodeltest_zip'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='truckmodeltest',
            name='location',
        ),
    ]