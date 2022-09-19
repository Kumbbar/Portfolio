# Generated by Django 4.1.1 on 2022-09-14 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100, null=True)),
                ('description', models.TextField(null=True)),
                ('date', models.DateField()),
                ('image', models.ImageField(upload_to='')),
            ],
            options={
                'db_table': 'events',
            },
        ),
    ]
