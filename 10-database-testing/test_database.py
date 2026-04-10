import unittest
import database


class TestDatabase(unittest.TestCase):
    def setUp(self):
        database.init_database()
        database.delete_all_users()

    def tearDown(self):
        database.delete_all_users()

    def test_create_user(self):
        user_id = database.create_user("Alice", "alice@example.com", 30)
        self.assertIsInstance(user_id, int)

        user = database.get_user_by_id(user_id)
        self.assertIsNotNone(user)
        self.assertEqual(user["name"], "Alice")
        self.assertEqual(user["email"], "alice@example.com")
        self.assertEqual(user["age"], 30)
        self.assertIn("created_at", user)

    def test_create_duplicate_user(self):
        database.create_user("Alice", "alice@example.com", 30)

        with self.assertRaises(ValueError):
            database.create_user("Alice 2", "alice@example.com", 25)

        users = database.get_all_users()
        self.assertEqual(len(users), 1)

    def test_get_user_by_id(self):
        user_id = database.create_user("Bob", "bob@example.com", 22)

        user = database.get_user_by_id(user_id)
        self.assertIsNotNone(user)
        self.assertEqual(user["id"], user_id)
        self.assertEqual(user["email"], "bob@example.com")

        missing = database.get_user_by_id(999999)
        self.assertIsNone(missing)

    def test_get_user_by_email(self):
        database.create_user("Carol", "carol@example.com", 41)

        user = database.get_user_by_email("carol@example.com")
        self.assertIsNotNone(user)
        self.assertEqual(user["name"], "Carol")

        missing = database.get_user_by_email("missing@example.com")
        self.assertIsNone(missing)

    def test_get_all_users(self):
        database.create_user("A", "a@example.com", 10)
        database.create_user("B", "b@example.com", 20)

        users = database.get_all_users()
        self.assertEqual(len(users), 2)
        emails = {u["email"] for u in users}
        self.assertEqual(emails, {"a@example.com", "b@example.com"})

    def test_update_user(self):
        user_id = database.create_user("Dave", "dave@example.com", 28)

        updated = database.update_user(user_id, name="David", age=29)
        self.assertTrue(updated)

        user = database.get_user_by_id(user_id)
        self.assertEqual(user["name"], "David")
        self.assertEqual(user["age"], 29)

        updated = database.update_user(user_id, email="david@example.com")
        self.assertTrue(updated)
        user = database.get_user_by_id(user_id)
        self.assertEqual(user["email"], "david@example.com")

    def test_update_nonexistent(self):
        updated = database.update_user(999999, name="Nobody")
        self.assertFalse(updated)

    def test_delete_user(self):
        user_id = database.create_user("Eve", "eve@example.com", 35)

        deleted = database.delete_user(user_id)
        self.assertTrue(deleted)
        self.assertIsNone(database.get_user_by_id(user_id))

    def test_delete_nonexistent(self):
        deleted = database.delete_user(999999)
        self.assertFalse(deleted)


if __name__ == "__main__":
    unittest.main()
