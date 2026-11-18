
import unittest
from main import StudentTaskManager


class TestStudentTaskManager(unittest.TestCase):

    def setUp(self):
        self.manager = StudentTaskManager()

    def test_add_task(self):
        task = self.manager.add_task("Complete assignment")

        # self.assertEqual(task["title"], "Complete assignment")
        self.assertEqual(task["title"], "Wrong assignment")
        self.assertFalse(task["completed"])

    def test_complete_task(self):
        task = self.manager.add_task("Study Python")

        result = self.manager.complete_task(task["id"])

        self.assertTrue(result)
        self.assertTrue(task["completed"])

    def test_delete_task(self):
        task = self.manager.add_task("Read book")

        result = self.manager.delete_task(task["id"])

        self.assertTrue(result)
        self.assertEqual(len(self.manager.tasks), 0)

    def test_empty_task(self):
        with self.assertRaises(ValueError):
            self.manager.add_task("")


if __name__ == "__main__":
    unittest.main()
