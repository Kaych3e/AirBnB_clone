#!/usr/bin/python3
"""Defines unittests for models/base_model.py.

Unittest classes:
    TestBaseModel_instantiation
    TestBaseModel_save
    TestBaseModel_to_dict
"""
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.base_model import BaseModel


class TestBaseModel_instantiation(unittest.TestCase):
    """Unittests for testing instantiation of the BaseModel class."""

    def test_no_args_instantiates(self):
        self.assertEqual(BaseModel, type(BaseModel()))

    def test_new_instance_stored_in_objects(self):
        self.assertIn(BaseModel(), models.storage.all().values())

    def test_id_is_public_str(self):
        self.assertEqual(str, type(BaseModel().id))

    def test_created_at_is_public_datetime(self):
        self.assertEqual(datetime, type(BaseModel().created_at))

    def test_updated_at_is_public_datetime(self):
        self.assertEqual(datetime, type(BaseModel().updated_at))

    def test_two_models_unique_ids(self):
        bm1 = BaseModel()
        bm2 = BaseModel()
        self.assertNotEqual(bm1.id, bm2.id)

    def test_two_models_different_created_at(self):
        bm1 = BaseModel()
        sleep(0.05)
        bm2 = BaseModel()
        self.assertLess(bm1.created_at, bm2.created_at)

    def test_two_models_different_updated_at(self):
        bm1 = BaseModel()
        sleep(0.05)
        bm2 = BaseModel()
        self.assertLess(bm1.updated_at, bm2.updated_at)

    def test_str_representation(self):
        dt = datetime.today()
        dt_repr = repr(dt)
        bm = BaseModel()
        bm.id = "123456"
        bm.created_at = bm.updated_at = dt
        bmstr = bm.__str__()
        self.assertIn("[BaseModel] (123456)", bmstr)
        self.assertIn("'id': '123456'", bmstr)
        self.assertIn("'created_at': " + dt_repr, bmstr)
        self.assertIn("'updated_at': " + dt_repr, bmstr)

    def test_args_unused(self):
        bm = BaseModel(None)
        self.assertNotIn(None, bm.__dict__.values())

    def test_instantiation_with_kwargs(self):
        dt = datetime.today()
        dt_iso = dt.isoformat()
        bm = BaseModel(id="345", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(bm.id, "345")
        self.assertEqual(bm.created_at, dt)
        self.assertEqual(bm.updated_at, dt)

    def test_instantiation_with_None_kwargs(self):
        with self.assertRaises(TypeError):
            BaseModel(id=None, created_at=None, updated_at=None)

    def test_instantiation_with_args_and_kwargs(self):
        dt = datetime.today()
        dt_iso = dt.isoformat()
        bm = BaseModel("12", id="345", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(bm.id, "345")
        self.assertEqual(bm.created_at, dt)
        self.assertEqual(bm.updated_at, dt)


class TestBaseModel_save(unittest.TestCase):
    """Unittests for testing save method of the BaseModel class."""

    @classmethod
    def setUp(self):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass

    @classmethod
    def tearDown(self):
<<<<<<< HEAD
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass

    def test_one_save(self):
        bm = BaseModel()
        sleep(0.05)
        first_updated_at = bm.updated_at
        bm.save()
        self.assertLess(first_updated_at, bm.updated_at)

    def test_two_saves(self):
        bm = BaseModel()
        sleep(0.05)
        first_updated_at = bm.updated_at
        bm.save()
        second_updated_at = bm.updated_at
        self.assertLess(first_updated_at, second_updated_at)
        sleep(0.05)
        bm.save()
        self.assertLess(second_updated_at, bm.updated_at)

    def test_save_with_arg(self):
        bm = BaseModel()
        with self.assertRaises(TypeError):
            bm.save(None)

    def test_save_updates_file(self):
        bm = BaseModel()
        bm.save()
        bmid = "BaseModel." + bm.id
        with open("file.json", "r") as f:
            self.assertIn(bmid, f.read())


class TestBaseModel_to_dict(unittest.TestCase):
    """Unittests for testing to_dict method of the BaseModel class."""

    def test_to_dict_type(self):
        bm = BaseModel()
        self.assertTrue(dict, type(bm.to_dict()))

    def test_to_dict_contains_correct_keys(self):
        bm = BaseModel()
        self.assertIn("id", bm.to_dict())
        self.assertIn("created_at", bm.to_dict())
        self.assertIn("updated_at", bm.to_dict())
        self.assertIn("__class__", bm.to_dict())

    def test_to_dict_contains_added_attributes(self):
        bm = BaseModel()
        bm.name = "Holberton"
        bm.my_number = 98
        self.assertIn("name", bm.to_dict())
        self.assertIn("my_number", bm.to_dict())

    def test_to_dict_datetime_attributes_are_strs(self):
        bm = BaseModel()
        bm_dict = bm.to_dict()
        self.assertEqual(str, type(bm_dict["created_at"]))
        self.assertEqual(str, type(bm_dict["updated_at"]))

    def test_to_dict_output(self):
        dt = datetime.today()
        bm = BaseModel()
        bm.id = "123456"
        bm.created_at = bm.updated_at = dt
        tdict = {
            'id': '123456',
            '__class__': 'BaseModel',
            'created_at': dt.isoformat(),
            'updated_at': dt.isoformat()
        }
        self.assertDictEqual(bm.to_dict(), tdict)

    def test_contrast_to_dict_dunder_dict(self):
        bm = BaseModel()
        self.assertNotEqual(bm.to_dict(), bm.__dict__)

    def test_to_dict_with_arg(self):
        bm = BaseModel()
        with self.assertRaises(TypeError):
            bm.to_dict(None)


if __name__ == "__main__":
=======
        """Tears down test methods."""
        self.resetStorage()
        pass

    def resetStorage(self):
        """Resets FileStorage data."""
        FileStorage._FileStorage__objects = {}
        if os.path.isfile(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_3_instantiation(self):
        """Tests instantiation of BaseModel class."""

        b = BaseModel()
# self.assertEqual(str(type(b)), "<class 'models.base_model.BaseModel'>")
        self.assertIsInstance(b, BaseModel)
        self.assertTrue(issubclass(type(b), BaseModel))

    def test_3_init_no_args(self):
        """Tests __init__ with no arguments."""
        self.resetStorage()
        with self.assertRaises(TypeError) as e:
            BaseModel.__init__()
        msg = "__init__() missing 1 required positional argument: 'self'"
        self.assertEqual(str(e.exception), msg)

    def test_3_init_many_args(self):
        """Tests __init__ with many arguments."""
        self.resetStorage()
        args = [i for i in range(1000)]
        b = BaseModel(0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
        b = BaseModel(*args)

    def test_3_attributes(self):
        """Tests attributes value for instance of a BaseModel class."""

        attributes = storage.attributes()["BaseModel"]
        o = BaseModel()
        for k, v in attributes.items():
            self.assertTrue(hasattr(o, k))
            self.assertEqual(type(getattr(o, k, None)), v)

    def test_3_datetime_created(self):
        """Tests if updated_at & created_at are current at creation."""

        date_now = datetime.now()
        b = BaseModel()
        diff = b.updated_at - b.created_at
        self.assertTrue(abs(diff.total_seconds()) < 0.01)
        diff = b.created_at - date_now
        self.assertTrue(abs(diff.total_seconds()) < 0.1)

    def test_3_id(self):
        """Tests for unique user ids."""

        nl = [BaseModel().id for i in range(1000)]
        self.assertEqual(len(set(nl)), len(nl))

    def test_3_save(self):
        """Tests the public instance method save()."""

        b = BaseModel()
        time.sleep(0.5)
        date_now = datetime.now()
        b.save()
        diff = b.updated_at - date_now
        self.assertTrue(abs(diff.total_seconds()) < 0.01)

    def test_3_str(self):
        """Tests for __str__ method."""
        b = BaseModel()
        rex = re.compile(r"^\[(.*)\] \((.*)\) (.*)$")
        res = rex.match(str(b))
        self.assertIsNotNone(res)
        self.assertEqual(res.group(1), "BaseModel")
        self.assertEqual(res.group(2), b.id)
        s = res.group(3)
        s = re.sub(r"(datetime\.datetime\([^)]*\))", "'\\1'", s)
        d = json.loads(s.replace("'", '"'))
        d2 = b.__dict__.copy()
        d2["created_at"] = repr(d2["created_at"])
        d2["updated_at"] = repr(d2["updated_at"])
        self.assertEqual(d, d2)

    def test_3_to_dict(self):
        """Tests the public instance method to_dict()."""

        b = BaseModel()
        b.name = "Laura"
        b.age = 23
        d = b.to_dict()
        self.assertEqual(d["id"], b.id)
        self.assertEqual(d["__class__"], type(b).__name__)
        self.assertEqual(d["created_at"], b.created_at.isoformat())
        self.assertEqual(d["updated_at"], b.updated_at.isoformat())
        self.assertEqual(d["name"], b.name)
        self.assertEqual(d["age"], b.age)

    def test_3_to_dict_no_args(self):
        """Tests to_dict() with no arguments."""
        self.resetStorage()
        with self.assertRaises(TypeError) as e:
            BaseModel.to_dict()
        msg = "to_dict() missing 1 required positional argument: 'self'"
        self.assertEqual(str(e.exception), msg)

    def test_3_to_dict_excess_args(self):
        """Tests to_dict() with too many arguments."""
        self.resetStorage()
        with self.assertRaises(TypeError) as e:
            BaseModel.to_dict(self, 98)
        msg = "to_dict() takes 1 positional argument but 2 were given"
        self.assertEqual(str(e.exception), msg)

    def test_4_instantiation(self):
        """Tests instantiation with **kwargs."""

        my_model = BaseModel()
        my_model.name = "Holberton"
        my_model.my_number = 89
        my_model_json = my_model.to_dict()
        my_new_model = BaseModel(**my_model_json)
        self.assertEqual(my_new_model.to_dict(), my_model.to_dict())

    def test_4_instantiation_dict(self):
        """Tests instantiation with **kwargs from custom dict."""
        d = {"__class__": "BaseModel",
                "updated_at":
                datetime(2050, 12, 30, 23, 59, 59, 123456).isoformat(),
                "created_at": datetime.now().isoformat(),
                "id": uuid.uuid4(),
                "var": "foobar",
                "int": 108,
                "float": 3.14}
        o = BaseModel(**d)
        self.assertEqual(o.to_dict(), d)

    def test_5_save(self):
        """Tests that storage.save() is called from save()."""
        self.resetStorage()
        b = BaseModel()
        b.save()
        key = "{}.{}".format(type(b).__name__, b.id)
        d = {key: b.to_dict()}
        self.assertTrue(os.path.isfile(FileStorage._FileStorage__file_path))
        with open(FileStorage._FileStorage__file_path,
                  "r", encoding="utf-8") as f:
            self.assertEqual(len(f.read()), len(json.dumps(d)))
            f.seek(0)
            self.assertEqual(json.load(f), d)

    def test_5_save_no_args(self):
        """Tests save() with no arguments."""
        self.resetStorage()
        with self.assertRaises(TypeError) as e:
            BaseModel.save()
        msg = "save() missing 1 required positional argument: 'self'"
        self.assertEqual(str(e.exception), msg)

    def test_5_save_excess_args(self):
        """Tests save() with too many arguments."""
        self.resetStorage()
        with self.assertRaises(TypeError) as e:
            BaseModel.save(self, 98)
        msg = "save() takes 1 positional argument but 2 were given"
        self.assertEqual(str(e.exception), msg)


if __name__ == '__main__':
>>>>>>> 3c3d44e0994df6b4ae32654479a3238060577520
    unittest.main()
