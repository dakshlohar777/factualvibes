# Generated by Django 5.1.4 on 2025-05-24 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_about_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='category',
            field=models.CharField(choices=[('fact', 'Fact'), ('scripture', 'Scripture'), ('other', 'Other')], default='other', max_length=20),
        ),
    ]
