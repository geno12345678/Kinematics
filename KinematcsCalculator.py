# -*- coding: utf-8 -*-

import tkinter as tk
from tkinter import messagebox

calculation_history = []

# Number Checker Function
def number_checker(question):
    while True:
        try:
            response = float(question)
            return response
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number")
            return None

# Kinematics Solving Function
def kinematic_equation_solver():
    calculation_type = calculation_entry.get().lower()
    
    if calculation_type == "final velocity":
        vi = number_checker(vi_entry.get())
        a = number_checker(a_entry.get())
        t = number_checker(t_entry.get())
        vf = vi + a * t
        calculation_history.append(f"Initial Velocity: {vi}, Acceleration: {a}, Time: {t} - The final velocity is: {vf}")
        messagebox.showinfo("Result", f"The final velocity is: {vf}")
    elif calculation_type == "initial velocity":
        vf = number_checker(vf_entry.get())
        a = number_checker(a_entry.get())
        t = number_checker(t_entry.get())
        vi = vf - a * t
        calculation_history.append(f"Final Velocity: {vf}, Acceleration: {a}, Time: {t} - The initial velocity is: {vi}")
        messagebox.showinfo("Result", f"The initial velocity is: {vi}")
    elif calculation_type == "acceleration":
        vi = number_checker(vi_entry.get())
        vf = number_checker(vf_entry.get())
        t = number_checker(t_entry.get())
        a = (vf - vi) / t
        calculation_history.append(f"Initial Velocity: {vi}, Final Velocity: {vf}, Time: {t} - The acceleration is: {a}")
        messagebox.showinfo("Result", f"The acceleration is: {a}")
    elif calculation_type == "time":
        vi = number_checker(vi_entry.get())
        vf = number_checker(vf_entry.get())
        a = number_checker(a_entry.get())
        t = (vf - vi) / a
        calculation_history.append(f"Initial Velocity: {vi}, Final Velocity: {vf}, Acceleration: {a} - The time is: {t}")
        messagebox.showinfo("Result", f"The time is: {t}")
    elif calculation_type == "distance":
        vi = number_checker(vi_entry.get())
        a = number_checker(a_entry.get())
        t = number_checker(t_entry.get())
        d = vi * t + 0.5 * a * t**2
        calculation_history.append(f"Initial Velocity: {vi}, Acceleration: {a}, Time: {t} - The distance is: {d}")
        messagebox.showinfo("Result", f"The distance is: {d}")
    else:
        messagebox.showerror("Error", "Please enter Final velocity, Initial velocity, Acceleration, Time or Distance under calculation type and try again :)")

# Calculation History Function
def show_history():
    history_message = "\n".join(calculation_history)
    if len(calculation_history) == 0:
        messagebox.showerror("Error", "There is no calculation history")
        
    elif len(calculation_history) > 0:
        messagebox.showinfo("Calculation History", history_message)
        
    else:
        messagebox.showerror("Error", "An unknown error occured")
     

# Create Main Window
root = tk.Tk()
root.title("Kinematics Calculator")
root.attributes("-fullscreen", True)

# Set the window background colour
root.configure(bg="white")

# Create custom title bar frame
title_bar = tk.Frame(root, bg="gray", relief="raised", bd=2)
title_bar.pack(fill="x")

# Title text
title_label = tk.Label(title_bar, text="Kinematics Calculator", bg="gray", fg="white")
title_label.pack(side="left", padx=10, pady=5)

# Close button
close_button = tk.Button(title_bar, text="X", bg="gray", fg="white", command=root.destroy)
close_button.pack(side="right", padx=10, pady=5)

# Windowed button
def window_window():
     if root.attributes('-fullscreen'):
        root.attributes('-fullscreen', False)
        root.geometry("400x400")
     elif not root.attributes('-fullscreen'):
         root.attributes('-fullscreen', True)
     else:
         messagebox.showerror("Error", "An unknown error occured")
         
         
windowed_button = tk.Button(title_bar, text="%", bg="gray", fg="white", command=window_window)
windowed_button.pack(side="right", padx=10, pady=5)

# Minimize button
def minimize_window():
    root.iconify()  # Minimize the main window
        

minimize_button = tk.Button(title_bar, text="_", bg="gray", fg="white", command=minimize_window)
minimize_button.pack(side="right", padx=10, pady=5)

# Create and configure the calculator frame
calculator_frame = tk.Frame(root, padx=20, pady=20)
calculator_frame.pack(padx=20, pady=20, fill=tk.BOTH, expand=True)

# Create input for calculation type
calculation_label = tk.Label(calculator_frame, text="Calculation Type:")
calculation_label.grid(row=0, column=0, sticky="w")
calculation_entry = tk.Entry(calculator_frame)
calculation_entry.grid(row=0, column=1, padx=10, pady=5)
options_label = tk.Label(calculator_frame, text="(Final velocity, Initial velocity, Acceleration, Time, Distance)")
options_label.grid(row=0 , column=2, padx=10, pady=10)

# Create input for initial velocity
vi_label = tk.Label(calculator_frame, text="Initial Velocity (m/s):")
vi_label.grid(row=1, column=0, sticky="w")
vi_entry = tk.Entry(calculator_frame)
vi_entry.grid(row=1, column=1, padx=10, pady=5)

# Create input for final velocity
vf_label = tk.Label(calculator_frame, text="Final Velocity (m/s):")
vf_label.grid(row=2, column=0, sticky="w")
vf_entry = tk.Entry(calculator_frame)
vf_entry.grid(row=2, column=1, padx=10, pady=5)

# Create input for acceleration
a_label = tk.Label(calculator_frame, text="Acceleration (m/s^2):")
a_label.grid(row=3, column=0, sticky="w")
a_entry = tk.Entry(calculator_frame)
a_entry.grid(row=3, column=1, padx=10, pady=5)

# Create input for time
t_label = tk.Label(calculator_frame, text="Time (s):")
t_label.grid(row=4, column=0, sticky="w")
t_entry = tk.Entry(calculator_frame)
t_entry.grid(row=4, column=1, padx=10, pady=5)

# Create and configure the submit button
submit_button = tk.Button(calculator_frame, text="Calculate", command=kinematic_equation_solver)
submit_button.grid(row=5, column=0, pady=10)

# Create and configure the show history button
show_history_button = tk.Button(calculator_frame, text="Show History", command=show_history)
show_history_button.grid(row=5, column=1, pady=10)

# Run the tkinter main loop
root.mainloop()
