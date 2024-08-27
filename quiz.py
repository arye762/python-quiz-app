import random
import os
import time
from questions_set1 import questions_set1  # Import the first set of questions
from questions_set2 import questions_set2  # Import the second set of questions

def ask_question(question_num, total_questions, question, options, correct_answer, description):
    os.system('clear')  # Clear the screen before each question
    
    # Display the score and elapsed time
    print(f"Score: {score} | Time: {time_elapsed()}")

    # Randomize the correct answer position while keeping the numbering 1-4
    indices = list(range(len(options)))
    random.shuffle(indices)
    shuffled_options = [options[i] for i in indices]
    
    if isinstance(correct_answer, list):
        shuffled_correct_answer = [indices.index(ans - 1) + 1 for ans in correct_answer]
    else:
        shuffled_correct_answer = indices.index(correct_answer - 1) + 1
    
    # Display the question number and question out of the total
    print(f"\nQuestion {question_num} of {total_questions}\n")
    print(f"{question}\n")
    
    # Display options with correct numbering
    for idx, option in enumerate(shuffled_options, 1):
        print(f"{idx}. {option}")

    print()  # Add a blank line for spacing
    
    answer = input("Choose the correct option (e.g., '1 4' for multiple answers), or 'b' to go back: ").strip()
    
    # Handle back navigation
    if answer.lower() == 'b':
        return None, False  # Go back without saving an answer

    try:
        # Parse the user's answer into a list of integers
        user_answers = list(map(int, answer.split()))
    except ValueError:
        print("\nInvalid input. Please enter numbers separated by spaces.\n")
        return None, False

    # Determine if the answer was correct
    correct_text = [options[i - 1] for i in correct_answer] if isinstance(correct_answer, list) else options[correct_answer - 1]
    if isinstance(correct_answer, list):
        is_correct = sorted(user_answers) == sorted(shuffled_correct_answer)
    else:
        is_correct = user_answers == [shuffled_correct_answer]
    
    if is_correct:
        print("\nCorrect!\n")
    else:
        print("\nWrong!\n")
        print(f"The correct answer is: {correct_text}\n")
    
    # Show the description after the answer is given
    print(f"Description: {description}\n")

    input("Press Enter to continue...")  # Pause before moving to the next question

    return answer, is_correct

def select_questions_set():
    print("Select the set of questions you want to answer:")
    print("1. Question Set 1")
    print("2. Question Set 2")
    print("3. Both Sets of Questions")
    choice = input("Enter the number of your choice: ").strip()

    if choice == '1':
        return questions_set1
    elif choice == '2':
        return questions_set2
    elif choice == '3':
        return questions_set1 + questions_set2
    else:
        print("Invalid choice. Defaulting to both sets of questions.")
        return questions_set1 + questions_set2

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

def time_elapsed():
    elapsed_time = time.time() - start_time
    minutes = int(elapsed_time // 60)
    seconds = int(elapsed_time % 60)
    return f"{minutes}m {seconds}s"

def main():
    global score
    score = 0
    wrong_questions = []
    global start_time
    start_time = time.time()

    selected_questions = select_questions_set()

    # Choose whether to randomize the questions or keep them in order
    randomize_order = choose_ordering()

    if randomize_order:
        random.shuffle(selected_questions)

    answers = [None] * len(selected_questions)  # To keep track of user answers
    total_questions = len(selected_questions)  # Total number of questions
    current_question = 0

    while current_question < len(selected_questions):
        q = selected_questions[current_question]
        answer, is_correct = ask_question(current_question + 1, total_questions, q["question"], q["options"], q["correct_answer"], q["description"])
        
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
                answer, is_correct = ask_question(i + 1, total_questions, q["question"], q["options"], q["correct_answer"], q["description"])
                
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
