import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo, showerror


def calculate_clicked():
    try:
        bmi = float(weight.get()) / (float(height.get()) ** 2)

        remarks = ''
        if (bmi > 30.0):
            remarks = "Obese"
        elif (bmi >= 25.0 and bmi <= 29.9):
            remarks = "Overweight"
        elif (bmi >= 18.5 and bmi <= 24.9):
            remarks = "Healthy Weight"
        else:
            remarks = "Underweight"

        msg = f"Your BMI is {bmi}, you're {remarks}"
        showinfo(
            title='Result',
            message=msg
        )
    except ValueError:
        showerror(
            title="Incorrect input",
            message="You've had inputted incorrect value"
        )


root = tk.Tk()
root.title("BMI Calculator")

# set the dimension of window
window_width = 300
window_height = 200

# get the screen dimensions
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# find the center point
center_x = int(screen_width/2 - window_width / 2)
center_y = int(screen_height/2 - window_height / 2)

root.geometry(f"{window_width}x{window_height}+{center_x}+{center_y}")
root.resizable(False, False)

bmi_frame = ttk.Frame(root)
bmi_frame.pack(padx=10, pady=10, fill='x', expand=True)

height = tk.StringVar()
weight = tk.StringVar()


# weight
weight_label = ttk.Label(bmi_frame, text="Weight (kg):")
weight_label.pack(fill='x', expand=True)

weight_entry = ttk.Entry(bmi_frame, textvariable=weight)
weight_entry.pack(fill='x', expand=True)
weight_entry.focus()

# height
height_label = ttk.Label(bmi_frame, text="Height (m):")
height_label.pack(fill='x', expand=True)

height_entry = ttk.Entry(bmi_frame, textvariable=height)
height_entry.pack(fill='x', expand=True)

# calculate button
calculate_button = ttk.Button(
    bmi_frame, text="Calculate BMI", command=calculate_clicked)
calculate_button.pack(fill='x', expand=True, pady=10)


root.mainloop()
