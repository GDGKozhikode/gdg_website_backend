from test_plus.test import TestCase
from ..models import Organizer


class OrganizerModelTest(TestCase):

    def test_string_representation(self):
        organizer = Organizer(name="Ligin Vellakkad")
        self.assertEqual(str(organizer), organizer.name)
