# Generated by Django 2.2.14 on 2021-06-03 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boec', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(default='path/static/image/placeholder.png', upload_to=''),
        ),
    ]
