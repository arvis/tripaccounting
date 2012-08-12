from django.db import models

class Driver(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    def __unicode__(self):
        return self.first_name+" "+self.last_name



class Truck(models.Model):
    plate_no = models.CharField(max_length=12)
    title = models.CharField(max_length=200)

    def __unicode__(self):
        return self.title


class Route(models.Model):
    title = models.CharField(max_length=200)
    length_km = models.IntegerField()

    def __unicode__(self):
        return self.title


class Trip(models.Model):
    route_name=models.ForeignKey(Route, default=None, null=True, blank=True)
    custom_route = models.CharField(max_length=200, blank=True,null=True)
    driver_name=models.ForeignKey(Driver)
    truck_name=models.ForeignKey(Truck)
    route_length= models.IntegerField()
    route_started = models.DateTimeField('date published')
    route_ended = models.DateTimeField('date published')
    date_created = models.DateTimeField(auto_now=True, blank=True)


    def clean(self):
        from django.core.exceptions import ValidationError
        print self.custom_route 
        if self.route_name.id==1 and self.custom_route=="":
            raise ValidationError('Please enter custom route name.')
        if self.route_name.id!=1:
            self.custom_route=""

    def __unicode__(self):
        if self.custom_route==1:
            return self.custom_route
        else:
            return self.route_name.title
