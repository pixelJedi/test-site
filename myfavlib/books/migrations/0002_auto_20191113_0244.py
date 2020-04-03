# Generated by Django 2.2.7 on 2019-11-12 23:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='cover',
            field=models.ImageField(null=True, upload_to='covers'),
        ),
        migrations.AlterField(
            model_name='book',
            name='genre',
            field=models.ManyToManyField(blank=True, default='unknown', to='books.Genre'),
        ),
        migrations.AlterField(
            model_name='book',
            name='text',
            field=models.FileField(null=True, upload_to='texts'),
        ),
    ]