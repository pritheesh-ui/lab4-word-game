import unittest
from unittest.mock import patch
import main

class TestMain(unittest.TestCase):

    def test_update_game_state_new_correct_guess(self):
        secret_word = "PYTHON"
        guessed_letters = ["P", "Y"]
        guess = "T"
        lives = 6
        new_guessed, new_lives = main.update_game_state(secret_word, guessed_letters, guess, lives)
        self.assertEqual(new_guessed, ["P", "Y", "T"])
        self.assertEqual(new_lives, 6)

    def test_update_game_state_new_incorrect_guess(self):
        secret_word = "PYTHON"
        guessed_letters = ["P", "Y"]
        guess = "Z"
        lives = 6
        new_guessed, new_lives = main.update_game_state(secret_word, guessed_letters, guess, lives)
        self.assertEqual(new_guessed, ["P", "Y", "Z"])
        self.assertEqual(new_lives, 5)

    def test_update_game_state_already_guessed(self):
        secret_word = "PYTHON"
        guessed_letters = ["P", "Y"]
        guess = "P"
        lives = 6
        new_guessed, new_lives = main.update_game_state(secret_word, guessed_letters, guess, lives)
        self.assertEqual(new_guessed, ["P", "Y"])
        self.assertEqual(new_lives, 6)

    def test_update_game_state_case_insensitive(self):
        secret_word = "PYTHON"
        guessed_letters = ["P", "Y"]
        guess = "t"  # lowercase
        lives = 6
        new_guessed, new_lives = main.update_game_state(secret_word, guessed_letters, guess, lives)
        self.assertEqual(new_guessed, ["P", "Y", "T"])
        self.assertEqual(new_lives, 6)

    def test_get_masked_word_no_guesses(self):
        secret_word = "PYTHON"
        guessed_letters = []
        masked = main.get_masked_word(secret_word, guessed_letters)
        self.assertEqual(masked, "_ _ _ _ _ _")

    def test_get_masked_word_some_guesses(self):
        secret_word = "PYTHON"
        guessed_letters = ["P", "Y", "T"]
        masked = main.get_masked_word(secret_word, guessed_letters)
        self.assertEqual(masked, "P Y T _ _ _")

    def test_get_masked_word_all_guessed(self):
        secret_word = "PYTHON"
        guessed_letters = ["P", "Y", "T", "H", "O", "N"]
        masked = main.get_masked_word(secret_word, guessed_letters)
        self.assertEqual(masked, "P Y T H O N")

    def test_is_game_won_false(self):
        secret_word = "PYTHON"
        guessed_letters = ["P", "Y", "T"]
        self.assertFalse(main.is_game_won(secret_word, guessed_letters))

    def test_is_game_won_true(self):
        secret_word = "PYTHON"
        guessed_letters = ["P", "Y", "T", "H", "O", "N"]
        self.assertTrue(main.is_game_won(secret_word, guessed_letters))

    @patch('builtins.input', side_effect=['A', 'Y'])
    def test_play_game_win(self, mock_input):
        with patch('builtins.print'):
            with patch('random.choice', return_value='PYTHON'):
                # This is tricky to test fully without mocking more, but basic structure
                # For now, just ensure it doesn't crash
                try:
                    main.play_game()
                except SystemExit:
                    pass  # Expected if it tries to exit

    # Note: Testing play_game and main fully would require more mocking of input/output
    # For simplicity, focus on unit tests for pure functions

if __name__ == '__main__':
    unittest.main()