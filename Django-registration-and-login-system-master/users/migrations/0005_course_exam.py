# Generated by Django 5.2 on 2025-04-08 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_profile_bio'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('Course', models.CharField(max_length=255)),
                ('chap1', models.URLField()),
                ('chap2', models.URLField()),
                ('chap3', models.URLField()),
                ('chap4', models.URLField()),
                ('chap5', models.URLField()),
                ('chap6', models.URLField()),
                ('chap7', models.URLField()),
                ('chap8', models.URLField()),
                ('chap9', models.URLField()),
                ('chap10', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Exam',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('Question', models.TextField()),
                ('opt1', models.CharField(max_length=255)),
                ('opt2', models.CharField(max_length=255)),
                ('opt3', models.CharField(max_length=255)),
                ('opt4', models.CharField(max_length=255)),
                ('Course', models.ManyToManyField(to='users.course')),
            ],
        ),
    ]
