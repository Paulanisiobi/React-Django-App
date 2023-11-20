# Generated by Django 4.2.6 on 2023-10-10 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ComputexMain', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='laptop',
            name='graphics_card',
            field=models.CharField(default='Integrated Graphics', max_length=100),
        ),
        migrations.AddField(
            model_name='laptop',
            name='is_on_sale',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='laptop',
            name='operating_system',
            field=models.CharField(default='Windows 10', max_length=50),
        ),
        migrations.AddField(
            model_name='laptop',
            name='quantity',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='laptop',
            name='screen_resolution',
            field=models.CharField(default='1920x1080', max_length=50),
        ),
        migrations.AddField(
            model_name='laptop',
            name='storage',
            field=models.CharField(default='256GB SSD', max_length=50),
        ),
        migrations.AddField(
            model_name='monitor',
            name='is_on_sale',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='monitor',
            name='panel_type',
            field=models.CharField(default='IPS', max_length=50),
        ),
        migrations.AddField(
            model_name='monitor',
            name='quantity',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='monitor',
            name='refresh_rate',
            field=models.PositiveIntegerField(default=60),
        ),
        migrations.AlterField(
            model_name='laptop',
            name='processor',
            field=models.CharField(default='Intel Core i5', max_length=100),
        ),
        migrations.AlterField(
            model_name='laptop',
            name='ram',
            field=models.CharField(default='8GB', max_length=50),
        ),
        migrations.AlterField(
            model_name='monitor',
            name='resolution',
            field=models.CharField(default='1920x1080', max_length=50),
        ),
        migrations.AlterField(
            model_name='monitor',
            name='screen_size',
            field=models.DecimalField(decimal_places=2, default=24.0, max_digits=4),
        ),
    ]
