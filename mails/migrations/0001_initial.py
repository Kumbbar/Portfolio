# Generated by Django 4.1.1 on 2022-09-15 07:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('contacts', models.CharField(max_length=200, null=True)),
                ('text', models.TextField(max_length=200, null=True)),
            ],
            options={
                'db_table': 'mails',
            },
        ),
    ]