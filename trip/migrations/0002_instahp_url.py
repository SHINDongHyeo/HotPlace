# Generated by Django 4.0.6 on 2022-08-18 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trip', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='instahp',
            name='url',
            field=models.URLField(default='몰라요', verbose_name='인스타 페이지 주소'),
            preserve_default=False,
        ),
    ]
