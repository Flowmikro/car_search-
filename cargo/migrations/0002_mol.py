# Generated by Django 4.2.1 on 2023-05-24 07:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cargo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mol',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('asdd', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cargo.cdd')),
            ],
        ),
    ]
