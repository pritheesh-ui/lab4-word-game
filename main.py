import random
import string
import time
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


def play_game(auto_mode: bool = False) -> None: 
    secret_word = random.choice(WORDS)
    guessed_letters: list[str] = []
    lives = INITIAL_LIVES
    
    available_letters = list(string.ascii_uppercase)

    print(f"\n--- {'AUTO PLAY' if auto_mode else 'MANUAL'} MODE ---")

    game_active = True
    while game_active and lives > 0:
        print(f"\nWord: {get_masked_word(secret_word, guessed_letters)}")

        if auto_mode:
            guess = random.choice(available_letters)
            available_letters.remove(guess) 
            print(f"Computer guessed: {guess}")
            time.sleep(0.5) 
        else:
            guess = input("Guess a letter: ").strip().upper()
            if len(guess) != 1 or not guess.isalpha() or guess in guessed_letters:
                print("Invalid or duplicate guess.")
                continue

        guessed_letters, lives = update_game_state(secret_word, guessed_letters, guess, lives)
        
def main() -> None:
    while True:
        print("\n1. Play Game")
        print("2. Auto Play")
        print("3. Quit")
        choice = input("Select (1/2/3): ").strip()

        if choice == '1':
            play_game(auto_mode=False)
        elif choice == '2':
            play_game(auto_mode=True)
        elif choice == '3':
            break

if __name__ == "__main__":
    main()

