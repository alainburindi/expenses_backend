# Generated by Django 2.2.8 on 2020-02-05 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expense', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='expense',
            name='deleted_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
