# Generated by Django 4.1 on 2022-08-24 05:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0004_alter_book_options'),
    ]

    operations = [
        migrations.AddIndex(
            model_name='book',
            index=models.Index(fields=['id'], name='id_index'),
        ),
    ]
