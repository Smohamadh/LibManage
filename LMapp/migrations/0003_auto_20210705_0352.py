# Generated by Django 3.2.5 on 2021-07-04 23:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LMapp', '0002_auto_20210705_0346'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='books',
            field=models.ManyToManyField(blank=True, null=True, to='LMapp.Book'),
        ),
        migrations.AlterField(
            model_name='book',
            name='Authors',
            field=models.ManyToManyField(blank=True, null=True, to='LMapp.Author'),
        ),
    ]
