import unittest
import app

class TestNotesFunctions(unittest.TestCase):
    def setUp(self):
        self.notes_dict = {'Note 1': 'Content 1', 'Note 2': 'Content 2'}

    def test_add_note(self):
        app.add_note(self.notes_dict, 'Note 3', 'Content 3')
        self.assertIn('Note 3', self.notes_dict)
        self.assertEqual(self.notes_dict['Note 3'], 'Content 3')

    def test_remove_note(self):
        removed_note = app.remove_note(self.notes_dict)
        self.assertIsNotNone(removed_note)
        self.assertNotIn(removed_note[0], self.notes_dict)

    def test_remove_empty_notes(self):
        notes_dict = {}
        with self.assertRaises(ValueError):
            app.remove_note(notes_dict)

    def test_display_notes(self):
        expected_output = "Список нотаток:\nNote 1: Content 1\nNote 2: Content 2\n"
        self.assertEqual(app.display_notes(self.notes_dict), expected_output)

    def test_get_amount(self):
        amount = app.get_amount(self.notes_dict)
        self.assertEqual(amount, 2)

if __name__ == '__main__':
    unittest.main()