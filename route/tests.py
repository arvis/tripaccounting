"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

#from django.test import TestCase
from django.utils import unittest
from route.models import Driver,Route,Truck,Trip,TripForm


class TripTestCase(unittest.TestCase):
    """docstring for ModelTest"""
    def setUp(self):
        # basic data to create trip object
        self.driver_dummy=Driver.objects.create(first_name="janis", last_name="Berzins")
        self.truck_dummy=Truck.objects.create(plate_no="AA TEST", title="Volvo")
        self.route_custom=Route.objects.create(title="custom", length_km=0)
        self.route_dummy=Route.objects.create(title="Riga-London", length_km=55)

    def test_create_trip(self):
        pass

    def test_edit_trip(self):
        pass

    def test_create_custom_not_title(self):
        """is possible to create a custom trip without a title"""
        new_trip=Trip.objects.create(custom_route="Riga-Vienna",driver_name=self.driver_dummy,truck_name=self.truck_dummy,route_length=10)

    def test_custom_and_selected_route(self):
        """if there is is custom route and predifined route custom route have to be cleared"""
        new_trip=Trip.objects.create(custom_route="Riga-Vienna",route_name=self.route_dummy,driver_name=self.driver_dummy,truck_name=self.truck_dummy,route_length=10)
        new_trip.clean()
        self.assertEqual(new_trip.custom_route, "")

    def test_no_route(self):
        """ have to fail if no selected and predifined route """
        new_trip=Trip.objects.create(driver_name=self.driver_dummy,truck_name=self.truck_dummy,route_length=10)
        from django.core.exceptions import ValidationError
        self.assertRaises(ValidationError, new_trip.clean)
        #new_trip.clean()
        #self.assertEqual(new_trip, "")

