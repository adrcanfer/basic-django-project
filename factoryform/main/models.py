from django.db import models
from datetime import datetime, timezone

from django.db.models import CASCADE


class Capsule(models.Model):
    creation_date = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=250)
    emails = models.CharField(blank=True, max_length=2500)
    capsule_type = models.CharField(max_length=1, choices=(('F', 'FREE'), ('P', 'PREMIUM'), ('M', 'MODULAR')))
    private = models.BooleanField()
    price = models.DecimalField(null=True, max_digits=7, decimal_places=2)
    dead_man_switch = models.BooleanField()
    dead_man_counter = models.BigIntegerField()
    dead_man_initial_counter = models.BigIntegerField()
    time_unit = models.IntegerField(null=True, choices=((0, 'minutes'), (1, 'days'), (2, 'months'), (3, 'years')))
    twitter = models.BooleanField()
    facebook = models.BooleanField()

    @property
    def is_released(self):
        res = False
        for i in self.modules.all():
            if (i.is_released):
                res = True
                break
        return res

    def seconds_to_unit(self):
        conversion_to_seconds = [60, 86400, 2592000, 31536000]
        if self.time_unit != None:
            res = round(self.dead_man_counter / conversion_to_seconds[int(self.time_unit)])
        else:
            res = 0
        return res

    def unit_to_seconds(self, unit):
        conversion_to_seconds = [60, 86400, 2592000, 31536000]
        if unit != None:
            res = self.dead_man_counter * conversion_to_seconds[unit]
        else:
            res = 0
        return res


class Module(models.Model):
    description = models.CharField(max_length=250)
    release_date = models.DateTimeField()
    capsule = models.ForeignKey(Capsule, related_name='modules', on_delete=CASCADE)
    release_notify = models.BooleanField(default=False)

    @property
    def is_released(self):
        return datetime.now(timezone.utc) >= self.release_date
