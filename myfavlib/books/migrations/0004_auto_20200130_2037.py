# Generated by Django 2.2.7 on 2020-01-30 17:37

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_auto_20191113_1654'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='author',
            options={'verbose_name': 'Автор', 'verbose_name_plural': 'Авторы'},
        ),
        migrations.AlterModelOptions(
            name='book',
            options={'verbose_name': 'Книга', 'verbose_name_plural': 'Книги'},
        ),
        migrations.AlterModelOptions(
            name='genre',
            options={'verbose_name': 'Жанр', 'verbose_name_plural': 'Жанры'},
        ),
        migrations.AddField(
            model_name='book',
            name='post_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='author',
            name='country',
            field=models.CharField(blank=True, default='unknown', max_length=100),
        ),
        migrations.AlterField(
            model_name='author',
            name='name',
            field=models.CharField(default='unknown', max_length=50),
        ),
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.ManyToManyField(blank=True, default='unknown', to='books.Author'),
        ),
        migrations.AlterField(
            model_name='book',
            name='cover',
            field=models.ImageField(blank=True, null=True, upload_to='covers'),
        ),
        migrations.AlterField(
            model_name='genre',
            name='base_genre',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='children', to='books.Genre'),
        ),
    ]
