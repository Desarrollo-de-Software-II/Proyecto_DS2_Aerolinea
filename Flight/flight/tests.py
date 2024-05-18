from django.test import TestCase
from flight.models import Place, Week, Flight, Passenger, Ticket

class TestFlightModels(TestCase):
    def setUp(self):
        # Create test data for Flight model
        origin = Place.objects.create(city="Origin City", airport="Origin Airport", code="ORI", country="Origin Country")
        destination = Place.objects.create(city="Destination City", airport="Destination Airport", code="DES", country="Destination Country")
        week = Week.objects.create(number=1, name="Week 1")
        Flight.objects.create(origin=origin, destination=destination, depart_time="12:00:00", arrival_time="14:00:00", plane="Boeing 777", airline="Example Airlines", economy_fare=500.00, business_fare=800.00, first_fare=1200.00)

    def test_flight_model_creation(self):
        # Retrieve the instance of the Flight model created in setUp
        flight_instance = Flight.objects.get(airline="Example Airlines")

        # Verify if the fields were configured correctly
        self.assertEqual(flight_instance.origin.city, "Origin City")
        self.assertEqual(flight_instance.destination.city, "Destination City")
        self.assertEqual(flight_instance.plane, "Boeing 777")
        self.assertEqual(flight_instance.economy_fare, 500.00)

    def test_passenger_model_creation(self):
        # Create test data for Passenger model
        Passenger.objects.create(first_name="John", last_name="Doe", gender="male")

        # Retrieve the instance of the Passenger model created
        passenger_instance = Passenger.objects.get(first_name="John")

        # Verify if the fields were configured correctly
        self.assertEqual(passenger_instance.last_name, "Doe")
        self.assertEqual(passenger_instance.gender, "male")

    def test_ticket_model_creation(self):
        # Create test data for Ticket model
        flight_instance = Flight.objects.get(airline="Example Airlines")
        passenger_instance = Passenger.objects.get(first_name="John")
        Ticket.objects.create(user_id=1, ref_no="ABC123", flight=flight_instance, flight_ddate="2024-05-10", flight_adate="2024-05-11", flight_fare=500.00, seat_class="economy", status="CONFIRMED")

        # Retrieve the instance of the Ticket model created
        ticket_instance = Ticket.objects.get(ref_no="ABC123")

        # Verify if the fields were configured correctly
        self.assertEqual(ticket_instance.flight_airline, "Example Airlines")
        self.assertEqual(ticket_instance.passengers.first().first_name, "John")
        self.assertEqual(ticket_instance.total_fare, 500.00)
        self.assertEqual(ticket_instance.status, "CONFIRMED")
