# Generated by Django 4.0.5 on 2022-07-07 21:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tguser',
            name='verification_code',
            field=models.CharField(blank=True, default=None, max_length=40, null=True),
        ),
    ]