# Generated by Django 3.0.9 on 2020-08-30 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='admin',
            fields=[
                ('Id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('Email_ID', models.CharField(max_length=200)),
                ('Password', models.CharField(max_length=200)),
            ],
        ),
    ]