# Generated by Django 2.2.14 on 2021-06-04 01:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('boec', '0005_auto_20210604_0833'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='Customer',
            new_name='customer',
        ),
    ]
