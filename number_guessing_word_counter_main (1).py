import random
from collections import Counter
import re


def number_guessing_game():
    """Play a random number guessing game with attempts and scoring."""
    print("\n" + "=" * 45)
    print("        NUMBER GUESSING GAME")
    print("=" * 45)
    print("I have selected a number between 1 and 100.")
    print("Try to guess it!")

    secret_number = random.randint(1, 100)
    attempts = 0
    score = 100

    while True:
        user_input = input("Enter your guess (1-100): ").strip()

        try:
            guess = int(user_input)
        except ValueError:
            print("Invalid input. Please enter a whole number.")
            continue

        if guess < 1 or guess > 100:
            print("Please enter a number between 1 and 100.")
            continue

        attempts += 1

        if guess < secret_number:
            print("Too low! Try again.")
            score = max(0, score - 10)
        elif guess > secret_number:
            print("Too high! Try again.")
            score = max(0, score - 10)
        else:
            print("\nCongratulations! You guessed the number.")
            print(f"Number: {secret_number}")
            print(f"Attempts: {attempts}")
            print(f"Final Score: {score}")
            break


def create_sample_text_file(filename="sample.txt"):
    """Create a sample text file for word-count testing."""
    sample_text = (
        "Python is easy to learn. "
        "Python is useful for automation. "
        "Learning Python helps beginners understand programming."
    )

    try:
        with open(filename, "w", encoding="utf-8") as file:
            file.write(sample_text)
        print(f"Sample file '{filename}' created successfully.")
    except OSError as error:
        print(f"Error creating file: {error}")


def word_counter():
    """Read a text file and display word count and word frequency."""
    print("\n" + "=" * 45)
    print("           WORD COUNTER")
    print("=" * 45)

    filename = input("Enter text file name (e.g. sample.txt): ").strip()

    try:
        with open(filename, "r", encoding="utf-8") as file:
            text = file.read()
    except FileNotFoundError:
        print(f"File '{filename}' was not found.")
        create_choice = input(
            "Would you like to create a sample.txt file? (y/n): "
        ).strip().lower()

        if create_choice == "y":
            create_sample_text_file()
            filename = "sample.txt"

            try:
                with open(filename, "r", encoding="utf-8") as file:
                    text = file.read()
            except OSError as error:
                print(f"Error reading sample file: {error}")
                return
        else:
            return
    except OSError as error:
        print(f"Error reading file: {error}")
        return

    words = re.findall(
        r"\b[a-zA-Z0-9]+(?:'[a-zA-Z0-9]+)?\b",
        text.lower()
    )
    frequency = Counter(words)

    print("\n--- Word Count Results ---")
    print(f"File: {filename}")
    print(f"Total words: {len(words)}")
    print(f"Unique words: {len(frequency)}")

    if frequency:
        print("\nWord Frequency:")
        for word, count in frequency.most_common():
            print(f"{word}: {count}")
    else:
        print("The file does not contain any words.")


def show_menu():
    """Display the main menu."""
    print("\n" + "=" * 45)
    print("      NUMBER GUESSING GAME & WORD COUNTER")
    print("=" * 45)
    print("1. Play Number Guessing Game")
    print("2. Count Words in a Text File")
    print("3. Create Sample Text File")
    print("4. Exit")
    print("=" * 45)


def main():
    """Run the application."""
    print("Welcome to the Number Guessing Game & Word Counter!")

    while True:
        show_menu()
        choice = input("Enter your choice (1-4): ").strip()

        if choice == "1":
            number_guessing_game()
        elif choice == "2":
            word_counter()
        elif choice == "3":
            create_sample_text_file()
        elif choice == "4":
            print("Thank you for using the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 4.")


if __name__ == "__main__":
    main()
