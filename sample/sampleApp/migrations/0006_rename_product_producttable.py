# Generated by Django 4.2.16 on 2024-12-24 07:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sampleApp', '0005_feedback_logintable_alter_manufacturetable_phone_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Product',
            new_name='ProductTable',
        ),
    ]
