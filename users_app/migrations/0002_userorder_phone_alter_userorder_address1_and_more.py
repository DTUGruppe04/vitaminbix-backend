# Generated by Django 5.0.2 on 2024-04-19 08:10

import encrypted_model_fields.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userorder',
            name='phone',
            field=encrypted_model_fields.fields.EncryptedCharField(default='00000000'),
        ),
        migrations.AlterField(
            model_name='userorder',
            name='address1',
            field=encrypted_model_fields.fields.EncryptedCharField(),
        ),
        migrations.AlterField(
            model_name='userorder',
            name='address2',
            field=encrypted_model_fields.fields.EncryptedCharField(),
        ),
        migrations.AlterField(
            model_name='userorder',
            name='city',
            field=encrypted_model_fields.fields.EncryptedCharField(),
        ),
        migrations.AlterField(
            model_name='userorder',
            name='email',
            field=encrypted_model_fields.fields.EncryptedCharField(),
        ),
        migrations.AlterField(
            model_name='userorder',
            name='zipcode',
            field=encrypted_model_fields.fields.EncryptedCharField(),
        ),
    ]
