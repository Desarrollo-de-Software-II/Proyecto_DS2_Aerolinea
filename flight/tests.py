#pruebas Funcionales
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model, authenticate
from flight.models import Place, Week, Flight, Passenger, Ticket

class TestFlightViews(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(username='validuser', password='validpassword')

        # Create test data for Flight model
        origin = Place.objects.create(city="Origin City", airport="Origin Airport", code="ORI", country="Origin Country")
        destination = Place.objects.create(city="Destination City", airport="Destination Airport", code="DES", country="Destination Country")
        week = Week.objects.create(number=1, name="Week 1")
        Flight.objects.create(origin=origin, destination=destination, depart_time="12:00:00", arrival_time="14:00:00", plane="Boeing 777", airline="Example Airlines", economy_fare=500.00, business_fare=800.00, first_fare=1200.00)

    # Pruebas de Caja Negra
    def test_login_success(self):
        response = self.client.post(reverse('login'), {'username': 'validuser', 'password': 'validpassword'})
        self.assertRedirects(response, reverse('index'))

    def test_register_success(self):
        response = self.client.post(reverse('register'), {
            'firstname': 'John',
            'lastname': 'Doe',
            'username': 'johndoe',
            'email': 'john.doe@example.com',
            'password': 'password123',
            'confirmation': 'password123'
        })
        self.assertRedirects(response, reverse('index'))
        self.assertTrue(get_user_model().objects.filter(username='johndoe').exists())

    def test_register_password_mismatch(self):
        response = self.client.post(reverse('register'), {
            'firstname': 'John',
            'lastname': 'Doe',
            'username': 'johndoe',
            'email': 'john.doe@example.com',
            'password': 'password123',
            'confirmation': 'password124'
        })
        self.assertContains(response, "Passwords must match.")

    def test_login_valid_credentials(self):
        user = authenticate(username='validuser', password='validpassword')
        self.assertIsNotNone(user)

    def test_login_invalid_credentials(self):
        user = authenticate(username='invaliduser', password='invalidpassword')
        self.assertIsNone(user)


class TestFlightModel(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(username='validuser', password='validpassword')

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
