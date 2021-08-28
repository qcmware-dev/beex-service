# Generated by Django 3.2.4 on 2021-06-12 05:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=65)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=255)),
                ('fullname', models.CharField(max_length=150)),
                ('identification', models.CharField(max_length=55)),
                ('phone', models.CharField(blank=True, default='', max_length=35)),
                ('age', models.IntegerField(default=18)),
                ('gender', models.CharField(max_length=1)),
                ('estatus', models.CharField(max_length=3)),
                ('metadata', models.JSONField()),
            ],
        ),
    ]
