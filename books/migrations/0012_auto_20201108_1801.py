# Generated by Django 3.1.2 on 2020-11-08 15:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0011_auto_20201108_1638'),
    ]

    operations = [
        migrations.AlterField(
            model_name='series',
            name='publishing_house',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='series', to='books.publishinghouse', verbose_name='Издательство'),
        ),
    ]
