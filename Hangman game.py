import random

def hangman():
    # Categories and words
    word_categories = {
        "Animals": ["elephant", "giraffe", "kangaroo", "dolphin", "penguin"],
        "Fruits": ["watermelon", "strawberry", "pineapple", "blueberry", "raspberry"],
        "Countries": ["australia", "brazil", "canada", "denmark", "ethiopia"]
    }
    
    # Game settings
    max_attempts = 6
    hint_available = True
    
    # Display welcome message
    print("""
    Welcome to Enhanced Hangman!
    ---------------------------
    Features:
    - Multiple word categories
    - Option to get a hint
    - Visual hangman display
    - Score tracking
    """)
    
    # Let player choose a category
    print("\nChoose a category:")
    for i, category in enumerate(word_categories.keys(), 1):
        print(f"{i}. {category}")
    
    while True:
        try:
            choice = int(input("Enter category number: "))
            if 1 <= choice <= len(word_categories):
                selected_category = list(word_categories.keys())[choice-1]
                secret_word = random.choice(word_categories[selected_category])
                break
            else:
                print("Invalid choice. Please enter a number from the list.")
        except ValueError:
            print("Please enter a valid number.")
    
    # Initialize game variables
    guessed_letters = []
    incorrect_guesses = []
    word_progress = ["_"] * len(secret_word)
    attempts_left = max_attempts
    score = 0
    
    # Game loop
    while True:
        # Display game status
        print("\n" + "="*40)
        print(f"Category: {selected_category}")
        print(f"Word: {' '.join(word_progress)}")
        print(f"Incorrect guesses: {', '.join(incorrect_guesses)}")
        print(f"Attempts left: {attempts_left}")
        print_hangman(attempts_left, max_attempts)
        
        # Check for win/lose conditions
        if "_" not in word_progress:
            score = attempts_left * 10  # Bonus points for remaining attempts
            print(f"\nCongratulations! You guessed the word: {secret_word}")
            print(f"Your score: {score}")
            break
            
        if attempts_left <= 0:
            print(f"\nGame over! The word was: {secret_word}")
            print(f"Your score: {score}")
            break
        
        # Player input
        print("\nOptions:")
        print("1. Guess a letter")
        if hint_available:
            print("2. Get a hint (one-time use)")
        print("3. Quit game")
        
        option = input("Choose an option: ")
        
        if option == "1":
            # Letter guessing
            guess = input("Enter a letter: ").lower()
            
            # Validate input
            if len(guess) != 1 or not guess.isalpha():
                print("Please enter a single letter.")
                continue
                
            if guess in guessed_letters:
                print("You already guessed that letter.")
                continue
                
            guessed_letters.append(guess)
            
            # Check if letter is in the word
            if guess in secret_word:
                print("Correct!")
                # Update word progress
                for i in range(len(secret_word)):
                    if secret_word[i] == guess:
                        word_progress[i] = guess
            else:
                print("Incorrect!")
                incorrect_guesses.append(guess)
                attempts_left -= 1
                
        elif option == "2" and hint_available:
            # Provide hint
            hint_available = False
            # Find a letter not yet guessed
            for letter in secret_word:
                if letter not in guessed_letters:
                    print(f"Hint: The word contains the letter '{letter}'")
                    break
                    
        elif option == "3":
            print(f"\nGame ended. The word was: {secret_word}")
            break
            
        else:
            print("Invalid option. Please try again.")

def print_hangman(attempts_left, max_attempts):
    """Visual representation of hangman progress"""
    stages = [
        """
           -----
           |   |
               |
               |
               |
               |
        """,
        """
           -----
           |   |
           O   |
               |
               |
               |
        """,
        """
           -----
           |   |
           O   |
           |   |
               |
               |
        """,
        """
           -----
           |   |
           O   |
          /|   |
               |
               |
        """,
        """
           -----
           |   |
           O   |
          /|\\  |
               |
               |
        """,
        """
           -----
           |   |
           O   |
          /|\\  |
          /    |
               |
        """,
        """
           -----
           |   |
           O   |
          /|\\  |
          / \\  |
               |
        """
    ]
    print(stages[max_attempts - attempts_left])

if __name__ == "__main__":
    hangman()
    print("\nThanks for playing!")
