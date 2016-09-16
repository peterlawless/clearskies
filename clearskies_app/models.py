from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Airfield(models.Model):
    identifier = models.CharField(max_length=10)
    name = models.CharField(max_length=200)
    latitude = models.FloatField()
    longitude = models.FloatField()
    city = models.CharField(max_length=200, blank=True)
    state = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return "{}-{}-{}, {}".format(self.identifier, self.name,
                                     self.city, self.state)


class METAR:
    def __init__(self, string):
        abbrevs = ['CLR', 'OVC', 'SCT', 'BKN', 'FEW']
        x = string.split(' ')
        self.identifier = x[0]
        self.ceiling = []
        for item in x[2:]:
            if item == 'AUTO':
                continue
            if item[-2:] == 'KT':
                self.windstring = item
            if item[:3] in abbrevs:
                self.parse_ceiling(item)

    def parse_ceiling(self, item):
        returnstring = ''
        if item[:3] == 'CLR':
            returnstring += 'Clear sky'
        if item[:3] == 'BKN':
            returnstring += 'Broken clouds at '
            returnstring += str(self.parse_number(item[3:]))
            returnstring += '00 feet AGL'
        if item[:3] == 'SCT':
            returnstring += 'Scattered clouds at '
            returnstring += str(self.parse_number(item[3:]))
            returnstring += '00 feet AGL'
        if item[:3] == 'OVC':
            returnstring += 'Overcast at '
            returnstring += str(self.parse_number(item[3:]))
            returnstring += '00 feet AGL'
        if item[:3] == 'FEW':
            returnstring += 'Few clouds at '
            returnstring += str(self.parse_number(item[3:]))
            returnstring += '00 feet AGL'
        self.ceiling.append(returnstring)

    def parse_number(self, string):
        while string[0] == '0':
            string = string[1:]
        return int(string)
