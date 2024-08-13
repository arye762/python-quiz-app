import random
import os
from questions_set1 import questions_set1  # Import the first set of questions
from questions_set2 import questions_set2  # Import the second set of questions

def ask_question(question_num, question, options, correct_answer, description):
    os.system('clear')  # Clear the screen before each question
    
    # Randomize the correct answer position while keeping the numbering 1-4
    indices = [1, 2, 3, 4]
    random.shuffle(indices)
    new_correct_answer = indices.index(1) + 1  # The correct answer will have index 1 in the original list
    
    # Display the question number and question
    print(f"\nQuestion {question_num}\n")
    print(f"{question}\n")
    
    # Display options with correct numbering
    for idx, original_idx in enumerate(indices, 1):
        print(f"{idx}. {options[original_idx - 1]}")

    print()  # Add a blank line for spacing
    # Prompt the user to choose an option
    answer = input("Choose the correct option (1-4): ")
    
    # Determine if the answer was correct
    correct_text = options[correct_answer - 1]
    if answer == str(new_correct_answer):
        print("\nCorrect!\n")
    else:
        print("\nWrong!\n")
        print(f"The correct answer is: {correct_text}\n")
    
    # Show the description after the answer is given
    print(f"Description: {description}\n")

    input("Press Enter to continue...")  # Pause before moving to the next question

    return answer == str(new_correct_answer)

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

def main():
    score = 0
    wrong_questions = []

    selected_questions = select_questions_set()

    # Choose whether to randomize the questions or keep them in order
    randomize_order = choose_ordering()

    if randomize_order:
        random.shuffle(selected_questions)

    for i, q in enumerate(selected_questions, 1):  # Enumerate to get the question number
        correct = ask_question(i, q["question"], q["options"], q["correct_answer"], q["description"])
        if correct:
            score += 1
        else:
            wrong_questions.append(q)

    print(f"\nYour final score is {score}/{len(selected_questions)}")

    # If there are wrong answers, offer to repeat them
    if wrong_questions:
        print(f"\nYou got {len(wrong_questions)} questions wrong. Would you like to try them again? (y/n)")
        retry = input().strip().lower()
        if retry == 'y':
            print("\nRepeating wrong questions...\n")
            if randomize_order:
                random.shuffle(wrong_questions)
            for i, q in enumerate(wrong_questions, 1):
                ask_question(i, q["question"], q["options"], q["correct_answer"], q["description"])

if __name__ == "__main__":
    main()
