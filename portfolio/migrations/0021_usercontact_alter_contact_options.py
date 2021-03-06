# Generated by Django 4.0.2 on 2022-02-22 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0020_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserContact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('phone', models.CharField(max_length=100, verbose_name='Phone')),
                ('subject', models.CharField(max_length=100, verbose_name='Subject')),
                ('message', models.TextField(verbose_name='Message')),
            ],
            options={
                'verbose_name': 'User Contact Info',
                'verbose_name_plural': 'User Contact Info',
                'ordering': ['timestamp'],
            },
        ),
        migrations.AlterModelOptions(
            name='contact',
            options={'verbose_name': 'Contact Info', 'verbose_name_plural': 'Contacts Info'},
        ),
    ]
