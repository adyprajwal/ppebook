# Generated by Django 2.1.5 on 2019-02-03 08:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='numbers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num_id', models.IntegerField()),
                ('num_word', models.CharField(max_length=15)),
                ('num_pic', models.ImageField(upload_to='')),
            ],
        ),
    ]
