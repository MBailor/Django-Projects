# Generated by Django 3.1.1 on 2020-09-06 22:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0004_auto_20200906_1521'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profiles',
            name='type',
            field=models.CharField(blank=True, choices=[('Mr.', 'Mr.'), ('Mrs.', 'Mrs.'), ('Ms.', 'M s.'), ('Lord', 'Lord'), ('Lady', 'Lady')], max_length=60),
        ),
    ]
