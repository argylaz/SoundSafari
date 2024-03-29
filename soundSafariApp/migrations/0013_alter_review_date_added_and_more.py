# Generated by Django 4.0.6 on 2024-03-22 13:50

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('soundSafariApp', '0012_alter_page_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='date_added',
            field=models.DateField(default=django.utils.timezone.now, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='date_created',
            field=models.DateField(default=django.utils.timezone.now, null=True),
        ),
    ]
