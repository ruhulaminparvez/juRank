# Generated by Django 4.0.2 on 2022-02-22 05:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0006_alter_choose_class_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='choose',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]