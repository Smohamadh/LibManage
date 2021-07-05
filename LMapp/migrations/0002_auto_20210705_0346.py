# Generated by Django 3.2.5 on 2021-07-04 23:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LMapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='Authors',
            field=models.ManyToManyField(to='LMapp.Author'),
        ),
        migrations.RemoveField(
            model_name='author',
            name='books',
        ),
        migrations.AddField(
            model_name='author',
            name='books',
            field=models.ManyToManyField(to='LMapp.Book'),
        ),
    ]
