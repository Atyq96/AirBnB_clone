import unittest
import sys
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):
    def setUp(self):
        self.base_model = BaseModel()

    def test_id_generation(self):
        self.assertIsNotNone(self.base_model.id)  # Assert that id is generated

    def test_created_at(self):
        self.assertIsNotNone(self.base_model.created_at)  # Assert created_at is set

    def test_updated_at(self):
        initial_updated_at = self.base_model.updated_at
        self.base_model.save()
        self.assertNotEqual(initial_updated_at, self.base_model.updated_at)  # Assert updated_at changes after save

    def test_to_dict(self):
        model_dict = self.base_model.to_dict()
        self.assertIsInstance(model_dict, dict) # Assert returned value is a dictionary
        self.assertIn('__class__', model_dict) # Assert '__class__' key is present
        self.assertEqual(model_dict['__class__'], 'BaseModel') # Assert '__class__' value is correct
        self.assertIn('created_at', model_dict) # Assert 'created_at' key is present
        self.assertIn('updated_at', model_dict) # Assert 'updated_at' key is present

if __name__ == '__main__':
    unittest.main()
