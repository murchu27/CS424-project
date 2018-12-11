from django.test import TestCase, Client
from productions.models import Production

# Create your tests here.
class ProductionModelTest(TestCase):
    def setUp(self):
        Production.objects.create(name="A Production", description="Something happens.")
        Production.objects.create(name="Another production.", description="Wow amazing.")

    def test_print(self):
        p = Production.objects.get(name="A Production")
        self.assertEqual(str(p),"A Production")

class ProductionDetailViewTest(TestCase):
    def setUp(self):
        Production.objects.create(name="This Production",description="Heck")

    def test_view(self):
        c = Client()
        response = c.get("/productions/production/id/1")
        self.assertEqual(response.status_code,200)

class ProductionListViewTest(TestCase):
    def setUp(self):
        Production.objects.create(name="Best Show Ever", description="Wow just amazing.")

    def test_view(self):
        c = Client()
        response = c.get("/productions/productions")
        self.assertEqual(response.status_code,200)
