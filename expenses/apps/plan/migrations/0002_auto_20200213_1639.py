# Generated by Django 3.0.2 on 2020-02-13 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plan', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='plan',
            name='to_be_done',
        ),
        migrations.AddField(
            model_name='plan',
            name='due_date',
            field=models.DateField(),
            preserve_default=False,
        ),
    ]
