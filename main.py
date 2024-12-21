import tkinter as tk
from tkinter import messagebox
from tkinter import PhotoImage
import random
import pygame

# Initialize pygame mixer for sound
pygame.mixer.init()
pygame.mixer.music.load(r'assets\kbc.mp3')
pygame.mixer.music.play(-1)  # Loop background music

correct_sound = pygame.mixer.Sound(r'assets\correctans.mp3')

# Questions and point levels
questions = [
    ["What is the output of the following code?\n\nx = 5\ny = 3\nprint(x + y)", "A) 8", "B) 53", "C) 2", "D) Error", 1],
    ["Which of the following is a correct variable name in Python?", "A) 1_variable", "B) variable-1", "C) _variable1", "D) @variable", 3],
    ["What does the len() function do in Python?", "A) It returns the number of elements in a list.", "B) It returns the length of a string or collection.", "C) It finds the minimum value of a list.", "D) It checks if an object is iterable.", 2],
    ["What is the result of the following expression in Python?\n\n10 // 3", "A) 3.33", "B) 3", "C) 3.0", "D) Error", 2],
    ["Which data type is used to store a true or false value in Python?", "A) int", "B) bool", "C) string", "D) list", 2],
    ["What is the purpose of the def keyword in Python?", "A) It defines a class.", "B) It defines a function.", "C) It declares a variable.", "D) It starts a loop.", 2],
    ["Which of the following is used to create a comment in Python?", "A) //", "B) /* */", "C) #", "D) <!-- -->", 3],
    ["How do you create a list in Python?", "A) list = ()", "B) list = {}", "C) list = []", "D) list = \"\"", 3],
    ["What does the input() function do in Python?", "A) It allows the user to enter data from the keyboard.", "B) It prints output to the screen.", "C) It exits the program.", "D) It imports a module.", 1],
    ["Which of the following methods is used to add an element to the end of a list in Python?", "A) append()", "B) add()", "C) insert()", "D) extend()", 1],
]

random.shuffle(questions)

points = 0
current_question = 0
lifelines_used = 0


# Timer function with 10 seconds countdown
def start_timer():
    def countdown(seconds):
        if seconds >= 0:
            timer_label.config(text=f"⏳ Time left: {seconds}s")
            window.after(1000, countdown, seconds - 1)
        else:
            messagebox.showinfo("Time's Up!", "You ran out of time!")
            next_turn()

    countdown(10)  # Start with 10 seconds


# Display the next question
def display_question():
    global current_question

    if current_question >= len(questions):
        messagebox.showinfo("Congratulations!", f"You scored {points} points!")
        quit_game()

    question = questions[current_question]
    question_label.config(text=f"Q: {question[0]}")
    option1_button.config(text=question[1], command=lambda: check_answer(1))
    option2_button.config(text=question[2], command=lambda: check_answer(2))
    option3_button.config(text=question[3], command=lambda: check_answer(3))
    option4_button.config(text=question[4], command=lambda: check_answer(4))

    # Start the timer for this question
    start_timer()


# Check the user's answer
def check_answer(selected_option):
    global current_question, points

    correct_option = questions[current_question][-1]
    if selected_option == correct_option:
        correct_sound.play()
        points_label.config(text=f"🏆 Points: {points + 100}")
        points += 100
        messagebox.showinfo("Correct!", f"You now have {points} points!")
    else:
        messagebox.showerror("Wrong Answer!", f"The correct answer was Option {correct_option}.")
    
    next_turn()


# Move to the next turn (question)
def next_turn():
    global current_question

    current_question += 1
    if current_question < len(questions):
        display_question()
    else:
        messagebox.showinfo("Game Over", f"You scored {points} points. Thank you for playing!")
        quit_game()


# Quit the game
def quit_game():
    window.destroy()


# Initialize Tkinter window
window = tk.Tk()
window.title("Kaun Banega Quiz Champion")
window.geometry("800x600")
window.configure(bg="black")

# Background image
bg_image = PhotoImage(file="assets/background.png")
bg_label = tk.Label(window, image=bg_image)
bg_label.place(relwidth=1, relheight=1)

# Title label with animation
title_label = tk.Label(window, text="KAUN BANEGA QUIZ CHAMPION", font=("Helvetica", 24, "bold"), fg="gold", bg="black")
title_label.pack(pady=10)

# Points label
points_label = tk.Label(window, text="🏆 Points: 0", font=("Arial", 16), fg="white", bg="black")
points_label.pack(pady=10)

# Timer label
timer_label = tk.Label(window, text="⏳ Time left: 10s", font=("Arial", 16), fg="red", bg="black")
timer_label.pack(pady=10)

# Question label
question_label = tk.Label(window, text="", font=("Arial", 18), wraplength=600, fg="white", bg="black", justify="center")
question_label.pack(pady=20)

# Options buttons
option1_button = tk.Button(window, text="", font=("Arial", 14), width=30, bg="blue", fg="white", command=None)
option1_button.pack(pady=5)

option2_button = tk.Button(window, text="", font=("Arial", 14), width=30, bg="blue", fg="white", command=None)
option2_button.pack(pady=5)

option3_button = tk.Button(window, text="", font=("Arial", 14), width=30, bg="blue", fg="white", command=None)
option3_button.pack(pady=5)

option4_button = tk.Button(window, text="", font=("Arial", 14), width=30, bg="blue", fg="white", command=None)
option4_button.pack(pady=5)

# Start game
display_question()

# Run Tkinter event loop
window.mainloop()
