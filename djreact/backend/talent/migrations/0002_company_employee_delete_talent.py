# Generated by Django 4.2.4 on 2023-08-07 12:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('talent', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('date_of_registration', models.DateField()),
                ('registration_number', models.CharField(max_length=50)),
                ('address', models.TextField()),
                ('contact_person', models.CharField(max_length=100)),
                ('departments', models.TextField()),
                ('number_of_employees', models.PositiveIntegerField()),
                ('contact_phone', models.CharField(max_length=15)),
                ('email_address', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('employee_id', models.CharField(blank=True, max_length=50)),
                ('department', models.CharField(max_length=100)),
                ('role', models.CharField(max_length=100)),
                ('date_started', models.DateField()),
                ('date_left', models.DateField(blank=True, null=True)),
                ('duties', models.TextField()),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='talent.company')),
            ],
        ),
        migrations.DeleteModel(
            name='talent',
        ),
    ]
