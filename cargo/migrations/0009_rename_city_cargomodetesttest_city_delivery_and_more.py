# Generated by Django 4.2.1 on 2023-05-24 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cargo', '0008_alter_cargomodetesttest_pick_up'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cargomodetesttest',
            old_name='city',
            new_name='city_delivery',
        ),
        migrations.RenameField(
            model_name='cargomodetesttest',
            old_name='state',
            new_name='city_pick_up',
        ),
        migrations.RenameField(
            model_name='cargomodetesttest',
            old_name='lat',
            new_name='lat_delivery',
        ),
        migrations.RenameField(
            model_name='cargomodetesttest',
            old_name='lng',
            new_name='lat_pick_up',
        ),
        migrations.RenameField(
            model_name='cargomodetesttest',
            old_name='zip_code',
            new_name='zip_code_delivery',
        ),
        migrations.AddField(
            model_name='cargomodetesttest',
            name='delivery',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='cargomodetesttest',
            name='lng_delivery',
            field=models.DecimalField(blank=True, decimal_places=6, max_digits=9, null=True),
        ),
        migrations.AddField(
            model_name='cargomodetesttest',
            name='lng_pick_up',
            field=models.DecimalField(blank=True, decimal_places=6, max_digits=9, null=True),
        ),
        migrations.AddField(
            model_name='cargomodetesttest',
            name='state_delivery',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='cargomodetesttest',
            name='state_pick_up',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='cargomodetesttest',
            name='zip_code_pick_up',
            field=models.CharField(default=0, max_length=10),
        ),
    ]
