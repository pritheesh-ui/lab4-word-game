# Word Game Notes

## App States
- Start Menu / Initialization
- Setup State (for fetching random word)
- Active Gameplay (waiting for input)
- Win State
- Lose State
- Play Again Prompt

## App Variables
- `secret_word` (string)
- `lives` (integer, starts at 6)
- `guessed_letters` (list of strings)
- `incorrect_guesses` (list of strings, for potential hangman visualization)

## App Rules and Invariants
- `lives` can never go below 0.
- A player cannot guess the same letter twice (it shouldn't penalize them twice).
- The game ends when all letters in `secret_word` are in `guessed_letters`, or `lives` == 0.

## App Bugs
- User types a number instead of a letter.
- User types multiple letters at once.
- Case sensitivity (guessing 'p' vs 'P' shouldn't break the game).

## CoPilot Suggestions
*Asked Copilot: "What states does a Word Game like Hangman game need?"* [cite: 142]

Copilot suggested:
- Initialization/Setup: Initialize variables, select a random word, and prepare the game.
- Gameplay/Active: Accept player guesses, update the masked word and lives, and check for win/lose conditions.
- Win: All letters in the secret word have been guessed correctly.
- Lose: Player runs out of lives without guessing the word.
- End/Prompt: Display results and ask if the player wants to play again.

I added an auto_mode flag to the play_game function. If it’s true, the game skips the input() prompt and lets the computer take a turn. This kept the code clean and avoided duplicating the win/loss logic.

To make sure the computer doesn't look "dumb" by guessing the same letter twice, I gave it its own pool of letters (the full alphabet). Every time it picks one, I pop it out of the list. It’s a simple but effective way to meet the "no-repeat" requirement.

refactored the entry point so that once a game ends—whether the computer won or the human lost—it drops you right back at the main menu. This makes the "Auto Play" feel like a repeatable feature rather than a one-off script.
