# Generated by Django 4.1 on 2022-11-08 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='cname',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stuname', models.CharField(max_length=50)),
                ('stusurname', models.CharField(max_length=50)),
                ('stuage', models.IntegerField()),
                ('sturoll_no', models.IntegerField()),
            ],
        ),
    ]
