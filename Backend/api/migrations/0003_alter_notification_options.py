# Generated by Django 4.2 on 2025-01-17 16:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_category_post_notification_comment_bookmark'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='notification',
            options={'ordering': ['-date'], 'verbose_name_plural': 'Notification'},
        ),
    ]
