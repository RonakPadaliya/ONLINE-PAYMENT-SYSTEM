# Generated by Django 3.1.5 on 2021-03-28 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('addbankaccount', '0004_auto_20210310_1735'),
    ]

    operations = [
        migrations.AddField(
            model_name='bank',
            name='block',
            field=models.CharField(max_length=1, null=True),
        ),
    ]
