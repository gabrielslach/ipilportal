# Generated by Django 2.1 on 2018-08-20 18:50

import datetime
import django.core.validators
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('requests', '0002_auto_20180821_0234'),
    ]

    operations = [
        migrations.AlterField(
            model_name='earlymorning',
            name='date_applied_for',
            field=models.DateField(default=datetime.datetime(2018, 8, 20, 18, 50, 16, 386832, tzinfo=utc), verbose_name='Date Applying For'),
        ),
        migrations.AlterField(
            model_name='earlymorning',
            name='destination',
            field=models.CharField(max_length=200, verbose_name='Destination'),
        ),
        migrations.AlterField(
            model_name='earlymorning',
            name='permit_status',
            field=models.CharField(choices=[('AP', 'Approved'), ('DC', 'Declined'), ('PD', 'Pending')], default='PD', max_length=2, verbose_name='Status'),
        ),
        migrations.AlterField(
            model_name='earlymorning',
            name='pub_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='earlymorning',
            name='reason',
            field=models.CharField(max_length=200, verbose_name='Reason'),
        ),
        migrations.AlterField(
            model_name='latenight',
            name='date_applied_for',
            field=models.DateField(default=datetime.datetime(2018, 8, 20, 18, 50, 16, 385832, tzinfo=utc), verbose_name='Date Applying For'),
        ),
        migrations.AlterField(
            model_name='latenight',
            name='destination',
            field=models.CharField(max_length=200, verbose_name='Destination'),
        ),
        migrations.AlterField(
            model_name='latenight',
            name='permit_status',
            field=models.CharField(choices=[('AP', 'Approved'), ('DC', 'Declined'), ('PD', 'Pending')], default='PD', max_length=2, verbose_name='Status'),
        ),
        migrations.AlterField(
            model_name='latenight',
            name='pub_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='latenight',
            name='reason',
            field=models.CharField(max_length=200, verbose_name='Reason'),
        ),
        migrations.AlterField(
            model_name='overnight',
            name='arrival',
            field=models.DateTimeField(default=datetime.datetime(2018, 8, 21, 18, 50, 16, 387832, tzinfo=utc), verbose_name='Arrival'),
        ),
        migrations.AlterField(
            model_name='overnight',
            name='departure',
            field=models.DateField(default=datetime.datetime(2018, 8, 20, 18, 50, 16, 387832, tzinfo=utc), verbose_name='Departure'),
        ),
        migrations.AlterField(
            model_name='overnight',
            name='destination',
            field=models.CharField(max_length=200, verbose_name='Destination'),
        ),
        migrations.AlterField(
            model_name='overnight',
            name='permit_status',
            field=models.CharField(choices=[('AP', 'Approved'), ('DC', 'Declined'), ('PD', 'Pending')], default='PD', max_length=2, verbose_name='Status'),
        ),
        migrations.AlterField(
            model_name='overnight',
            name='pub_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='overnight',
            name='reason',
            field=models.CharField(max_length=200, verbose_name='Reason'),
        ),
        migrations.AlterField(
            model_name='user',
            name='f_name',
            field=models.CharField(max_length=50, verbose_name='First Name'),
        ),
        migrations.AlterField(
            model_name='user',
            name='form_n',
            field=models.IntegerField(verbose_name='Form Number'),
        ),
        migrations.AlterField(
            model_name='user',
            name='l_name',
            field=models.CharField(max_length=50, verbose_name='Last Name'),
        ),
        migrations.AlterField(
            model_name='user',
            name='room_n',
            field=models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1)], verbose_name='Room Number'),
        ),
    ]
