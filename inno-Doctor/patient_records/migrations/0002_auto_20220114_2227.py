# Generated by Django 2.2.24 on 2022-01-14 22:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient_records', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medicationstatement',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]