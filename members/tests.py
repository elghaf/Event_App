from django.test import TestCase
from .models import MyModel

def test_my_model_create(self):
    """Test that a MyModel object can be created."""
    MyModel.objects.create(name="Test create")
    self.assertEqual(MyModel.objects.count(), 2)

def test_my_model_read(self):
    """Test that a MyModel object can be read."""
    my_model = MyModel.objects.get(name="Test name")
    self.assertEqual(my_model.name, "Test name")

def test_my_model_update(self):
    """Test that a MyModel object can be updated."""
    my_model = MyModel.objects.get(name="Test name")
    my_model.name = "Updated name"
    my_model.save()
    updated_model = MyModel.objects.get(name="Updated name")
    self.assertEqual(updated_model.name, "Updated name")

def test_my_model_delete(self):
    """Test that a MyModel object can be deleted."""
    MyModel.objects.filter(name="Updated name").delete()
    self.assertEqual(MyModel.objects.count(), 1)