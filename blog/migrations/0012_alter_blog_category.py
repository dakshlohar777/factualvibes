# Generated by Django 5.1.4 on 2025-05-26 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_blog_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='category',
            field=models.CharField(choices=[('fact', 'Fact'), ('scripture', 'Scripture'), ('sports', 'Sports'), ('other', 'Other')], default='other', max_length=20),
        ),
    ]
