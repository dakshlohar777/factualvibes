# Generated by Django 5.1.4 on 2025-05-23 07:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_rename_paragraph_about_paragra'),
    ]

    operations = [
        migrations.RenameField(
            model_name='about',
            old_name='paragra',
            new_name='content',
        ),
        migrations.RemoveField(
            model_name='about',
            name='time',
        ),
        migrations.AddField(
            model_name='about',
            name='title',
            field=models.CharField(default='About Factual Vibes', max_length=200),
            preserve_default=False,
        ),
    ]
