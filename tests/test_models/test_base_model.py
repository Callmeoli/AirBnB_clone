import unittest
import time
import datetime

from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """ Tests base model class"""

    def test_uuid(self):
        """Test uuid attribute of class"""
        bm1 = BaseModel()
        bm2 = BaseModel()
        self.assertIsInstance(bm1, BaseModel)
        self.assertTrue(hasattr(bm1, "id"))
        self.assertNotEqual(bm1.id, bm2.id)
        self.assertIsInstance(bm1.id, str)

    def test_created_at(self):
        """Test created_at attribute of class"""
        bm1 = BaseModel()
        time.sleep(0.1)
        bm2 = BaseModel()
        self.assertIsInstance(bm1, BaseModel)
        self.assertTrue(hasattr(bm1, "created_at"))
        self.assertNotEqual(bm1.created_at, bm2.created_at)
        self.assertIsInstance(bm1.created_at, datetime.datetime)

    def test_updated_at(self):
        """Test updated_at attribute of class"""
        bm1 = BaseModel()
        time.sleep(0.1)
        bm2 = BaseModel()
        self.assertIsInstance(bm1, BaseModel)
        self.assertTrue(hasattr(bm1, "updated_at"))
        self.assertNotEqual(bm1.updated_at, bm2.updated_at)
        self.assertIsInstance(bm1.updated_at, datetime.datetime)
if __name__ == "__main__":
    unittest.main()
