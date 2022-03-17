from django.test import TestCase
from django.contrib.auth import get_user_model

from .models import Music

class MusicTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        testuser1 = get_user_model().objects.create_user(username='testuser', password='pass')
        testuser1.save()

        test_thing = Music.objects.create(name='Les Paul', seller=testuser1, instrument='Guitar', description='Slash played this guitar')
        test_thing.save()

    def test_things_model(self):
        thing = Music.objects.get(id=1)
        actual_seller = str(thing.seller)
        actual_name = str(thing.name)
        actual_instrument = str(thing.instrument)
        actual_description = str(thing.description)
        self.assertEqual(actual_name, 'Les Paul')
        self.assertEqual(actual_seller,'testuser')
        self.assertEqual(actual_instrument, 'Guitar')
        self.assertEqual(actual_description,'Slash played this guitar')
