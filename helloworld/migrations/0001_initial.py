# Generated by Django 2.2.2 on 2019-06-21 05:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Counter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('groupno', models.IntegerField(default=0)),
                ('orderno', models.IntegerField(default=0)),
                ('depth', models.IntegerField(default=0)),
            ],
        ),
    ]
