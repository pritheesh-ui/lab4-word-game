import random

# Game constants
WORDS = ["PYTHON", "FLASK", "DEVELOPMENT", "INTERFACE", "VARIABLE", "SOFTWARE"]
INITIAL_LIVES = 6

def update_game_state(secret_word: str, guessed_letters: list[str], guess: str, lives: int) -> tuple[list[str], int]:
    
    guess = guess.upper()

    if guess in guessed_letters:
        return guessed_letters, lives

    updated_guessed_letters = guessed_letters + [guess]
    updated_lives = lives if guess in secret_word else lives - 1

    return updated_guessed_letters, updated_lives

def get_masked_word(secret_word: str, guessed_letters: list[str]) -> str:
  
    return " ".join([char if char in guessed_letters else "_" for char in secret_word])

def is_game_won(secret_word: str, guessed_letters: list[str]) -> bool:
      return all(char in guessed_letters for char in secret_word)

def play_game() -> None:
      secret_word = random.choice(WORDS)
    guessed_letters: list[str] = []
    lives = INITIAL_LIVES

    print("\n--- Welcome to Guess The Word! ---")

    game_active = True
    while game_active and lives > 0:
        print(f"\nWord: {get_masked_word(secret_word, guessed_letters)}")
        print(f"Guessed so far: {', '.join(guessed_letters) if guessed_letters else 'None'}")
        print(f"Lives remaining: {lives}")

        guess = input("Guess a letter: ").strip().upper()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single valid letter.")
            continue

        if guess in guessed_letters:
            print(f"You already guessed '{guess}'. Try a different letter.")
            continue

        guessed_letters, lives = update_game_state(secret_word, guessed_letters, guess, lives)

        if is_game_won(secret_word, guessed_letters):
            print(f"\nCongratulations! You guessed the word: {secret_word}")
            game_active = False

    if lives == 0:
        print(f"\nGame Over! You ran out of lives. The word was: {secret_word}")

def main() -> None:
    
    play_again = 'Y'
    while play_again == 'Y':
        play_game()
        play_again = input("\nWould you like to play again? (Y/N): ").strip().upper()

    print("Thanks for playing!")

if __name__ == "__main__":
    main()
