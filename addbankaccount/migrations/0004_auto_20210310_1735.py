# Generated by Django 3.1.5 on 2021-03-10 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('addbankaccount', '0003_auto_20210310_1641'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bank',
            name='status',
            field=models.IntegerField(null=True),
        ),
    ]
