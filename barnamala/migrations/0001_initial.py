# Generated by Django 2.1.5 on 2019-02-06 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='barna',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('barna_id', models.IntegerField()),
                ('barna_word', models.CharField(max_length=15)),
                ('barna_pic', models.ImageField(upload_to='')),
                ('barna_audio', models.FileField(default='', upload_to='')),
            ],
        ),
    ]
