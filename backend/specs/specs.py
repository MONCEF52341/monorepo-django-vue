from django.test import TestCase


class FakeTestCase(TestCase):
    def setUp(self):
        pass

    def test_animals_can_speak(self):
        self.assertEqual(1, 1)
