# Generated by Django 4.1 on 2022-11-08 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='fourthclass',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stuname', models.CharField(max_length=50)),
                ('stusurname', models.CharField(max_length=50)),
                ('stuage', models.IntegerField()),
                ('sturoll_no', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='secondclass',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stuname', models.CharField(max_length=50)),
                ('stusurname', models.CharField(max_length=50)),
                ('stuage', models.IntegerField()),
                ('sturoll_no', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='thirdclass',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stuname', models.CharField(max_length=50)),
                ('stusurname', models.CharField(max_length=50)),
                ('stuage', models.IntegerField()),
                ('sturoll_no', models.IntegerField()),
            ],
        ),
        migrations.RenameModel(
            old_name='cname',
            new_name='firstclass',
        ),
    ]
