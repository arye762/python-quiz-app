import random
import os
import time
import subprocess
import webbrowser  # Import the webbrowser module
from PIL import Image  # Import the PIL library to handle images


def ask_question(question_num, total_questions, question, options, correct_answer, description, image=None):
    os.system('clear')  # Clear the screen before each question

    print(f"Score: {score} | Time: {time_elapsed()}")

    # Randomize the correct answer position
    indices = list(range(len(options)))
    random.shuffle(indices)
    shuffled_options = [options[i] for i in indices]
    
    if isinstance(correct_answer, list):
        shuffled_correct_answer = [indices.index(ans - 1) + 1 for ans in correct_answer]
    else:
        shuffled_correct_answer = indices.index(correct_answer - 1) + 1

    print(f"\nQuestion {question_num} of {total_questions}\n")
    print(f"{question}\n")

    # Display the image if provided and enabled
    if image and image_enabled:
        try:
            print(f"Loading image: {image}")  # Debugging: print the image path

            # Close the Preview app before showing the new image
            subprocess.call(["osascript", "-e", 'tell application "Preview" to quit'])

            # Open the image directly with Preview
            subprocess.call(["open", image])

            time.sleep(1)  # Give time for the image to display

            # Bring terminal back to the foreground
            subprocess.call(["osascript", "-e", 'tell application "Terminal" to activate'])

        except Exception as e:
            print(f"Error loading image: {e}")

    for idx, option in enumerate(shuffled_options, 1):
        print(f"{idx}. {option}")
    print()  # Add a blank line for spacing
    
    answer = input("Choose the correct option (e.g., '1 4' for multiple answers), or 'b' to go back: ").strip()
    
    # Handle back navigation
    if answer.lower() == 'b':
        return None, False  # Go back without saving an answer

    try:
        user_answers = list(map(int, answer.split()))
    except ValueError:
        print("\nInvalid input. Please enter numbers separated by spaces.\n")
        return None, False

    correct_text = [options[i - 1] for i in correct_answer] if isinstance(correct_answer, list) else options[correct_answer - 1]
    is_correct = sorted(user_answers) == sorted(shuffled_correct_answer) if isinstance(correct_answer, list) else user_answers == [shuffled_correct_answer]
    
    if is_correct:
        print("\nCorrect!\n")
    else:
        print("\nWrong!\n")
        print(f"The correct answer is: {correct_text}\n")
    
    print(f"Description: {description}\n")

    input("Press Enter to continue...")  # Pause before moving to the next question

    # Close the image before moving to the next question if images are enabled
    if image_enabled:
        subprocess.call(["osascript", "-e", 'tell application "Preview" to quit'])

    return answer, is_correct


def select_questions_set():
    print("Select the set of questions you want to answer:")
    choice = input("Enter the number of your choice: ").strip()

    if choice == '1':
    elif choice == '2':
    elif choice == '3':
        return questions_set1 + questions_set2
    else:

def choose_ordering():
    print("\nHow would you like the questions to be ordered?")
    print("1. Randomized")
    print("2. In Order")
    choice = input("Enter the number of your choice: ").strip()

    if choice == '1':
        return True  # Randomize
    elif choice == '2':
        return False  # In order
    else:
        print("Invalid choice. Defaulting to randomized order.")
        return True

def enable_images():
    print("\nWould you like to enable images in the questions?")
    print("1. Yes")
    print("2. No")
    choice = input("Enter the number of your choice: ").strip()

    if choice == '1':
        return True
    elif choice == '2':
        return False
    else:
        print("Invalid choice. Defaulting to images enabled.")
        return True

def time_elapsed():
    elapsed_time = time.time() - start_time
    minutes = int(elapsed_time // 60)
    seconds = int(elapsed_time % 60)
    return f"{minutes}m {seconds}s"

def main():
    global score
    global image_enabled
    score = 0
    wrong_questions = []
    global start_time
    start_time = time.time()

    selected_questions = select_questions_set()

    # Choose whether to randomize the questions or keep them in order
    randomize_order = choose_ordering()

    # Enable or disable images
    image_enabled = enable_images()

    if randomize_order:
        random.shuffle(selected_questions)

    answers = [None] * len(selected_questions)  # To keep track of user answers
    total_questions = len(selected_questions)  # Total number of questions
    current_question = 0 

    while current_question < len(selected_questions):
        q = selected_questions[current_question]
        answer, is_correct = ask_question(
            current_question + 1, 
            total_questions, 
            q["question"], 
            q["options"], 
            q["correct_answer"], 
            q["description"],
            q.get("image", None)  # Pass the image path if it exists
        )
        
        if answer is not None:
            if answers[current_question] is None:  # Only add to score if it's the first attempt at the question
                if is_correct:
                    score += 1
                else:
                    wrong_questions.append(current_question)
            elif answers[current_question] != answer:  # Adjust the score if the answer changes on retry
                previous_correct = answers[current_question] == str(q["correct_answer"])
                if is_correct and not previous_correct:
                    score += 1
                elif not is_correct and previous_correct:
                    score -= 1

            answers[current_question] = answer
            current_question += 1  # Move to the next question
        elif current_question > 0:
            current_question -= 1  # Go back to the previous question

    print(f"\nYour final score is {score}/{total_questions}")

    # Offer to retry wrong questions
    if wrong_questions:
        print(f"\nYou got {len(wrong_questions)} questions wrong. Would you like to try them again? (y/n)")
        retry = input().strip().lower()
        if retry == 'y':
            print("\nRepeating wrong questions...\n")
            for i in wrong_questions:
                q = selected_questions[i]
                answer, is_correct = ask_question(
                    i + 1, 
                    total_questions, 
                    q["question"], 
                    q["options"], 
                    q["correct_answer"], 
                    q["description"],
                    q.get("image", None)  # Pass the image path if it exists
                )
                
                # Allow re-answering the question
                if answer is not None:
                    previous_answer = answers[i]
                    previous_correct = previous_answer == str(q["correct_answer"])
                    if previous_answer != answer:
                        if is_correct and not previous_correct:
                            score += 1
                        elif not is_correct and previous_correct:
                            score -= 1
                    answers[i] = answer

            print(f"\nYour final score after retry is {score}/{total_questions}")

if __name__ == "__main__":
    main()
