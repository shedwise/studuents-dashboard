# Generated by Django 5.1.2 on 2024-10-14 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_image', models.URLField(max_length=255)),
                ('full_name', models.CharField(max_length=100)),
                ('cohort', models.CharField(max_length=50)),
                ('program', models.CharField(max_length=100)),
                ('status', models.CharField(max_length=50)),
                ('date_joined', models.DateField()),
                ('rating', models.DecimalField(decimal_places=1, max_digits=2)),
            ],
        ),
    ]
