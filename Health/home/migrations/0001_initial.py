# Generated by Django 4.0.6 on 2022-07-21 17:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('abbreviated_name', models.CharField(max_length=8)),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('brief', models.CharField(max_length=500)),
                ('instruction', models.CharField(max_length=5000)),
                ('show_home_screen', models.BooleanField(default=False)),
                ('photo', models.ImageField(default='service_image/default.png', upload_to='service_image')),
                ('lang', models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='home.language')),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('position', models.CharField(max_length=30)),
                ('photo', models.ImageField(default='person_image/default.png', upload_to='person_image')),
                ('lang', models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='home.language')),
            ],
        ),
        migrations.CreateModel(
            name='JobExperience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.IntegerField(default=0)),
                ('finish_date', models.IntegerField(default=0)),
                ('business_name', models.CharField(max_length=50)),
                ('position', models.CharField(max_length=30)),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.person')),
            ],
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.IntegerField(default=0)),
                ('finish_date', models.IntegerField(default=0)),
                ('school_name', models.CharField(max_length=50)),
                ('school_department_name', models.CharField(max_length=50)),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.person')),
            ],
        ),
        migrations.CreateModel(
            name='ClinicalApplications',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.person')),
            ],
        ),
        migrations.CreateModel(
            name='Certificate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('certificate_year', models.IntegerField(default=0)),
                ('educator_name', models.CharField(blank=True, default='', max_length=80, null=True)),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.person')),
            ],
        ),
    ]
