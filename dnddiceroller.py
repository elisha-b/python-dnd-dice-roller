# Owner: elisha-b
# Date: 17-02-2025
# Project: D&D Dice Roller

import random
import tkinter as tk
import tkinter.font as tkFont
from tkinter import *
from tkinter import ttk
from tkinter.ttk import *
from tkinter import messagebox

# Main tkinter window/toplevel
root = tk.Tk()
root.resizable(False, False)
root.title("Python D&D Dice Roller")

# Set fonts
normal_font =  tkFont.Font(family="Arial", size=16, weight=tkFont.NORMAL)
title_font = tkFont.Font(family="Arial",  size=28, weight=tkFont.BOLD)

# Title label
title = Label(root, text="Python D&D Dice Roller", font=title_font).grid(columnspan=2, row=0, column=0, padx=50,pady=5)

# Dice side mapping
dice_sides_map = {"d4": 4, "d6": 6, "d8": 8, "d10": 10, "d12": 12, "d20": 20}
num_sides = tk.IntVar(value=0)

def update_num_sides(event):
    selection = num_sides_combo.get()
    num_sides.set(dice_sides_map.get(selection, 0))

def roll_dice():
    try:
        num_dice = int(num_dice_field.get())
        modifier = int(modifier_field.get())
        sides = num_sides.get()
    
        if num_dice <= 0:
            messagebox.showwarning("Error", "There must be at least 1 die!")
            return
        
        rolls = [random.randint(1, sides) for _ in range(num_dice)]
        total = sum(rolls) + modifier
        result_text = f"Rolls: {rolls}\nTotal (with modifier): {total}"

        messagebox.showinfo("Roll Result", result_text)

    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers.")

# No. of Sides
Label(root, text="No. of Sides", font=normal_font, justify="left").grid(row=1,column=0,padx=5,pady=10)
num_sides_combo = ttk.Combobox(root, values=["d4", "d6", "d8", "d10", "d12", "d20"], state="readonly", font=normal_font)
num_sides_combo.grid(row=1,column=1,padx=0,pady=10)
num_sides_combo.bind("<<ComboboxSelected>>", update_num_sides)

# No. of Dice
Label(root, text="No. of Dice", font=normal_font, justify="left").grid(row=2,column=0,padx=5,pady=10)
num_dice_field = ttk.Spinbox(root, from_=0, to=999, font=normal_font)
num_dice_field.grid(row=2, column=1, padx=0, pady=10)

# Any Modifiers
Label(root, text="Modifier", font=normal_font, justify="left").grid(row=3,column=0,padx=5,pady=10)
modifier_field = ttk.Spinbox(root, from_=-999, to=999, font=normal_font)
modifier_field.grid(row=3, column=1, padx=0, pady=10)

# Roll Button
roll_button = tk.Button(root, text="Roll",  height=1, width=20, font=normal_font, command=roll_dice)
roll_button.grid(row=4,columnspan=2, column=0, padx=0, pady=10)
    
# Start GUI
root.mainloop()
