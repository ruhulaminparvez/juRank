# Generated by Django 4.0.2 on 2022-02-22 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0013_testimonial_class_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='blog_images', verbose_name='Upload an Image of Blog')),
                ('heading', models.CharField(blank=True, max_length=50, null=True, verbose_name='Write a Heading of Blog')),
                ('description', models.CharField(blank=True, max_length=200, null=True, verbose_name='Write a Description of Blog')),
                ('admin_name', models.CharField(blank=True, max_length=50, null=True, verbose_name='Write Name of Admin')),
                ('date', models.DateField(auto_now_add=True, verbose_name='Write Date of Blog')),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Blog',
                'verbose_name_plural': 'Blogs',
            },
        ),
    ]