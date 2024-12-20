# Generated by Django 5.1.3 on 2024-12-03 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0023_remove_message_recaptcha'),
    ]

    operations = [
        migrations.AlterField(
            model_name='competence',
            name='image',
            field=models.FileField(blank=True, upload_to='competence/'),
        ),
        migrations.AlterField(
            model_name='project',
            name='demo',
            field=models.URLField(blank=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='github',
            field=models.URLField(blank=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.ImageField(blank=True, upload_to='projects/'),
        ),
    ]
