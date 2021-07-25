from django.test import TestCase
from app.mycal import addit,subit,multit,divit

class calcTests(TestCase):
    def test_addit(self):
        self.assertEqual(addit(3,2),5)

    def test_subit(self):
        self.assertEqual(subit(5,2),3)

    def test_multit(self):
        self.assertEqual(multit(5,2),10)

    def test_div(self):
        self.assertEqual(divit(6,2),3)