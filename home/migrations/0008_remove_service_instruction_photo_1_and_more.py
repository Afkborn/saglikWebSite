# Generated by Django 4.0.6 on 2022-07-23 21:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_alter_service_instruction'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='service',
            name='instruction_photo_1',
        ),
        migrations.RemoveField(
            model_name='service',
            name='instruction_photo_1_visible',
        ),
        migrations.RemoveField(
            model_name='service',
            name='instruction_photo_2',
        ),
        migrations.RemoveField(
            model_name='service',
            name='instruction_photo_2_visible',
        ),
        migrations.RemoveField(
            model_name='service',
            name='instruction_photo_3',
        ),
        migrations.RemoveField(
            model_name='service',
            name='instruction_photo_3_visible',
        ),
    ]