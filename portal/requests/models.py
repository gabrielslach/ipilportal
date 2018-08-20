import datetime

from django.db import models
from django.utils import timezone
from django.core.validators import MinValueValidator

# Create your models here.
class User(models.Model):
    f_name = models.CharField('First Name', max_length=50)
    l_name = models.CharField('Last Name', max_length=50)
    room_n = models.PositiveIntegerField('Room Number', validators=[MinValueValidator(1)])
    form_n = models.IntegerField('Form Number', validators=[MinValueValidator(1)])

    def __str__(self):
        return (self.f_name + self.l_name)

class LateNight(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    permit_status_choices = (('AP', 'Approved'),
        ('DC', 'Declined'),
        ('PD', 'Pending'))

    permit_status = models.CharField(
        'Status',
        max_length = 2,
        choices = permit_status_choices,
        default = 'PD'
        )
    reason = models.CharField(
        'Reason',
        max_length = 200
        )
    destination = models.CharField(
        'Destination',
        max_length = 200
        )
    date_applied_for = models.DateField(
        'Date Applying For',
        default = timezone.now(),
        #Take note of this
        editable = True
        )
    pub_date =  models.DateTimeField(
        auto_now_add = True)

    def __str__(self):
        date = self.date_applied_for
        return ('[' + str(self.user.form_n) + '] '
            + self.user.l_name
            + ' (' + date.strftime('%Y/%m/%d') + ')')

class EarlyMorning(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    permit_status_choices = (('AP', 'Approved'),
        ('DC', 'Declined'),
        ('PD', 'Pending'))

    permit_status = models.CharField(
        'Status',
        max_length = 2,
        choices = permit_status_choices,
        default = 'PD'
        )
    reason = models.CharField(
        'Reason',
        max_length = 200
        )
    destination = models.CharField(
        'Destination',
        max_length = 200
        )
    date_applied_for = models.DateField(
        'Date Applying For',
        default = timezone.now(),
        #Take note of this
        editable = True
        )
    pub_date =  models.DateTimeField(
        auto_now_add = True)

    def __str__(self):
        date = self.date_applied_for
        return ('[' + str(self.user.form_n) + '] '
            + self.user.l_name
            + ' (' + date.strftime('%Y/%m/%d') + ')')

class OverNight(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    permit_status_choices = (('AP', 'Approved'),
        ('DC', 'Declined'),
        ('PD', 'Pending'))

    permit_status = models.CharField(
        'Status',
        max_length = 2,
        choices = permit_status_choices,
        default = 'PD'
        )
    reason = models.CharField(
        'Reason',
        max_length = 200
        )
    destination = models.CharField(
        'Destination',
        max_length = 200
        )
    departure = models.DateField(
        'Departure',
        default = timezone.now(),
        #Take note of this
        editable = True
        )
    arrival = models.DateTimeField(
        'Arrival',
        default = timezone.now() + datetime.timedelta(days=1),
        #Take note of this
        editable = True
        )
    pub_date =  models.DateTimeField(
        auto_now_add = True)

    def __str__(self):
        arrival = self.arrival
        dept = self.departure
        return ('[' + str(self.user.form_n) + '] '
            + self.user.l_name
            + ' (' + dept.strftime('%Y/%m/%d')
            + ' - ' + arrival.strftime('%Y/%m/%d') + ')')
