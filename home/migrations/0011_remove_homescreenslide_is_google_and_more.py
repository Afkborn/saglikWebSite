# Generated by Django 4.0.6 on 2022-07-24 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_homescreenslide_is_google_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='homescreenslide',
            name='is_google',
        ),
        migrations.RemoveField(
            model_name='homescreenslide',
            name='show_home_page',
        ),
        migrations.AddField(
            model_name='comment',
            name='is_google',
            field=models.BooleanField(default=False, help_text="Google'dan gelen mesaj mi?"),
        ),
        migrations.AddField(
            model_name='comment',
            name='show_home_page',
            field=models.BooleanField(default=True, help_text='Ana sayfa da gösterilsin mi?'),
        ),
    ]
