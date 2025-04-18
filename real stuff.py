# Notes:
#   Code was written manually except for where noted, comments and docstrings generated by Codeium
#   Unicode characters found and implemented by OpenAI's ChatGPT 4

# ----- Imports ----- #
import tkinter as tk
from tkinter import messagebox as mb
import math_functions as math
import sys

# ----- Global Variables ----- #
ans1 = 1
ans2 = 2
a_value = 1
b_value = 2
c_value = 3
d_value = 4
num = 1
device = ""

# ----- Functions ----- #
def set_demension_type():
    """
    Makes the window geometry change based on the device type either mac or windows
    """
    global device
    if sys.platform == "darwin": # mac
        device="mac"
    else: # windows
        device="windows"

def raise_main():
    """
    Raises the 'frame_main' frame to the top of the stacking order.\n
    Also, all the text entry fields will be cleared, and the global variables related to the quadratic equation will be reset to their default values.
    """
    global ans1, ans2, a_value, b_value, c_value, d_value, num, device
    frame_main.tkraise()
    if device=="mac":
        root.wm_geometry("250x325")
    else:
        root.wm_geometry("300x325")
    
    # Clear the text entry fields for the quadratic equation
    ent_a_factor.delete(0, tk.END)
    ent_b_factor.delete(0, tk.END)
    ent_c_factor.delete(0, tk.END)
    
    # Clear the text entry fields for the FOIL method
    ent_a_foil.delete(0, tk.END)
    ent_b_foil.delete(0, tk.END)
    ent_c_foil.delete(0, tk.END)
    ent_d_foil.delete(0, tk.END)

    # Clear the text entry fields for the get factors
    ent_gf_num.delete(0, tk.END)
    
    # Reset the global variables for the quadratic equation
    ans1 = 1
    ans2 = 2
    a_value = 1
    b_value = 2
    c_value = 3
    d_value = 4
    num = 1

def raise_factor():
    """
    Raises the 'frame_factor' frame to the top of the stacking order, making it visible in the GUI.
    """
    global device
    frame_factor.tkraise()
    if device=="mac":
        root.wm_geometry("250x385")
    else:
        root.wm_geometry("300x385")
    update_ans_factor("")

def raise_foil():
    """
    Raises the 'frame_foil' frame to the top of the stacking order, making it visible in the GUI.
    """
    global device
    frame_foil.tkraise()
    if device=="mac":
        root.wm_geometry("250x460")
    else:
        root.wm_geometry("300x460")
    update_ans_foil("")

def raise_gf():
    """
    Raises the 'frame_gf' frame to the top of the stacking order, making it visible in the GUI.
    """
    global device
    frame_gf.tkraise()
    if device=="mac":
        root.wm_geometry("250x300")
    else:
        root.wm_geometry("300x300")
    update_ans_gf("")

def update_ans_factor(text):
    """
    Updates the answer in the 'answer_factor' Text widget with the given text and centers it.
    Clears any existing text before inserting the new text and disables the widget to prevent editing.
    """
    answer_factor.config(state="normal")
    answer_factor.delete("1.0", tk.END)
    answer_factor.insert("1.0", text)
    answer_factor.tag_configure("center", justify='center')
    answer_factor.tag_add("center", 1.0, "end")
    answer_factor.pack()
    answer_factor.config(state="disabled")

def update_ans_foil(text):
    """
    Updates the answer in the 'answer_foil' Text widget with the given text and formats it to be centered.
    """
    answer_foil.config(state="normal")
    answer_foil.delete("1.0", tk.END)
    answer_foil.insert("1.0", text)
    answer_foil.tag_configure("center", justify='center')
    answer_foil.tag_add("center", 1.0, "end")
    answer_foil.pack()
    answer_foil.config(state="disabled")

def update_ans_gf(text):
    """
    Updates the answer in the 'answer_gf' Text widget with the given text and formats it to be centered.
    Resizes the text widget height based on the number of lines in the text.
    """
    global device
    # Enable the text widget to allow editing
    answer_gf.config(state="normal")
    
    # Delete any existing text
    answer_gf.delete("1.0", tk.END)
    
    # Insert the new text
    answer_gf.insert("1.0", text)
    
    # Resize the text widget height based on the number of lines in the text
    # Note: generated by ai but fixed to work by humans
    # Calculate the number of lines based on the number of commas and newlines
    lines = text.count("\n") + (text.count(",") + 1) // 2 + 1
    
    # Note: The height of the text widget is set to the number of lines minus 2
    # because the text widget is created with a height of 1, which is the
    # default height, and the height is incremented by 1 to account for the
    # border around the text widget.
    answer_gf.configure(height=lines-3)
    
    # Format the text to be centered
    answer_gf.tag_configure("center", justify='center', wrap="word")
    answer_gf.tag_add("center", 1.0, "end")
    
    # Pack the text widget to make it visible
    answer_gf.pack()
    
    # Disable the text widget to prevent editing
    answer_gf.config(state="disabled")
    
    # Resize the window based on the height of the text widget
    # Note: The width of the window is kept constant at 250, and the height is
    # increased by 11 pixels for each line of text to account for the border
    # around the text widget.
    if device=="mac":
        root.wm_geometry("250x" + str(250 + lines * 11))
    else:
        root.wm_geometry("300x" + str(300 + lines * 11))
    

def get_factor_answer():
    """
    Retrieves the values for a, b, and c from their respective entry fields, validates them,
    and uses the quadratic equation to calculate the roots of the equation. Updates the
    'answer_factor' Text widget with the formatted quadratic equation.

    If any value is invalid, an error message is displayed and the function returns early.

    This function relies on global variables to store and update the coefficients and roots.
    """
    global ans1, ans2, a_value, b_value, c_value
    answer_factor = []
    # Retrieve the values from the entry fields
    a_value = ent_a_factor.get()
    b_value = ent_b_factor.get()
    c_value = ent_c_factor.get()
    # Set the values in the math_functions module
    result = math.set_values(a_value, b_value,c_value)
    if result == "e":
        # If the values are invalid, update the answer text with an error message and display an error popup
        update_ans_factor("Error, Try again")
        mb.showerror("Value Error", "All values must be integers")
        return
    # Calculate the roots
    # Store the roots in the variables ans1 and ans2
    if (math.get_root_type() == "r"):
        answer_factor = math.quadratic_equation()
        # If the roots are real, format them and update the answer text
        ans1 = answer_factor[0]
        ans2 = answer_factor[1]
        if (ans1 > 0):
            # If the first root is positive, use the format "(x - root)"
            ans1 = "(x - " + str(ans1) + ")"
        elif (ans1 == 0):
            # If the first root is zero, use the format "(x)"
            ans1 = "(x)"
        else:
            # If the first root is negative, use the format "(x + root)"
            ans1 = "(x + " + str(abs(ans1)) + ")"

        if (ans2 > 0):
            # If the second root is positive, use the format "(x - root)"
            ans2 = "(x - " + str(ans2) + ")"
        elif (ans2 == 0):
            # If the second root is zero, use the format "(x)"
            ans2 = "(x)"
        else:
            # If the second root is negative, use the format "(x + root)"
            ans2 = "(x + " + str(abs(ans2)) + ")"

        # Update the answer text with the formatted quadratic equation
        update_ans_factor(str(ans1) + str(ans2))
    else:
        answer_factor = math.quadratic_imaginary()
        # If the roots are imaginary'
        equation = answer_factor[0]
        bottom_value = answer_factor[1]

        equation = f"{equation}\u2044{bottom_value}"
        update_ans_factor(equation)

        #https://superuser.com/questions/1816633/what-is-the-correct-way-to-write-fractions-in-unicode

        #equation = f"{a_value}x\u00b2 "
        #equation += f"{'+ ' if b_value >= 0 else '- '}{abs(b_value)}x "
        #equation += f"{'+ ' if c_value >= 0 else '- '}{abs(c_value)}"


def get_foil_answer():
    """
    Retrieves the values for a, b, c, and d from their respective entry fields,
    validates them, and uses the FOIL method to calculate the coefficients of a
    quadratic equation. Updates the 'answer_foil' Text widget with the formatted
    quadratic equation.

    If any value is invalid, an error message is displayed and the function
    returns early.

    This function relies on global variables to store and update the
    coefficients.
    """

    # Get the values from the entry fields as integers. The math module's
    # validate_input function is used to ensure the values are valid integers
    a_value = math.validate_input(ent_a_foil.get())
    b_value = math.validate_input(ent_b_foil.get())
    c_value = math.validate_input(ent_c_foil.get())
    d_value = math.validate_input(ent_d_foil.get())

    # If any of the values are invalid (False), display an error message and
    # return early
    if a_value is False or b_value is False or c_value is False or d_value is False:
        # Update the answer text with an error message
        update_ans_foil("Error, Try again")
        # Show an error popup
        mb.showerror("Value Error", "All values must be integers")
        # Return early to prevent further execution of the function
        return

    # Calculate the coefficients using the FOIL method
    answer_foil = math.calculate_foil(a_value, b_value, c_value, d_value)

    # Store the coefficients in the global variables
    a_value = answer_foil[0]
    b_value = answer_foil[1]
    c_value = answer_foil[2]

    # Format the equation string with appropriate signs. Generated by ChatGPT with human fixing
    equation = f"{a_value}x\u00b2 "
    equation += f"{'+ ' if b_value >= 0 else '- '}{abs(b_value)}x "
    equation += f"{'+ ' if c_value >= 0 else '- '}{abs(c_value)}"

    # Update the answer text with the formatted quadratic equation
    update_ans_foil(equation)

def get_gf_answer():
    """
    Retrieves the value from the entry field for the number to be factored,
    validates it, and uses the get_factors function to calculate the factors of the number.
    Updates the 'answer_gf' Text widget with the formatted list of factors.

    If the value is invalid, an error message is displayed and the function returns early.
    """
    global num  # Use the global variable 'num' to store the input number

    factors = ""  # Initialize an empty string to accumulate the factors

    # Validate the input from the entry field
    num = math.validate_input(ent_gf_num.get())
    if num is False:  # Check if the input is not a valid integer
        update_ans_gf("Error, Try again")  # Update the GUI with an error message
        mb.showerror("Value Error", "The number must be an integer")  # Show an error popup
        return  # Exit the function early due to invalid input

    # Retrieve the input number from the entry field
    num = ent_gf_num.get()

    # Use the get_factors function to calculate the factors of the number
    answer_gf = math.get_factors(int(num))

    # Iterate over the factors and format them as a comma-separated string
    for i in range(len(answer_gf)):
        # Check if the current factor is the last in the list
        if i == (len(answer_gf) - 1):
            factors += str(answer_gf[i])  # Append the last factor without a trailing comma
            break  # Exit the loop
        factors += str(answer_gf[i]) + ", "  # Append the factor followed by a comma and space
    
    # Update the GUI with the formatted list of factors
    update_ans_gf(factors)

# ----- Main Window Setup ----- #
root = tk.Tk() 
root.title("Factorer Program")
set_demension_type()
if device=="mac":
    root.wm_geometry("250x325")
elif device=="windows":
    root.wm_geometry("300x325")

# ----- Frames Setup ----- #
frame_main = tk.Frame(root)
frame_main.grid(row=0, column=0, sticky="news")

frame_factor = tk.Frame(root)
frame_factor.grid(row=0, column=0, sticky="news")

frame_foil = tk.Frame(root)
frame_foil.grid(row=0, column=0, sticky="news")

frame_gf = tk.Frame(root)
frame_gf.grid(row=0, column=0, sticky="news")

# ----- Main Screen Elements ----- #
lbl_title = tk.Label(frame_main, text="Factorer", font=("Arial Rounded MT Bold", 36), )
lbl_title.pack(padx=50, pady=40)

# ----- Factoring Screen Elements ----- #
lbl_factor_form = tk.Label(frame_factor, text= "Enter Quadratic in form: Ax\u00b2 + Bx + C", font= "Archivo")
lbl_factor_form.pack(padx=5, pady=5)

lbl_a_factor= tk.Label(frame_factor, text="A Value", font="Archivo")
lbl_a_factor.pack(padx=5, pady=5)
ent_a_factor = tk.Entry(frame_factor, textvariable= a_value)
ent_a_factor.pack(padx= 5, pady= 5)

lbl_b_factor= tk.Label(frame_factor, text="B Value", font="Archivo")
lbl_b_factor.pack(padx=40, pady=5)
ent_b_factor = tk.Entry(frame_factor, textvariable= b_value)
ent_b_factor.pack(padx= 5, pady= 5)

lbl_c_factor= tk.Label(frame_factor, text="C Value", font="Archivo")
lbl_c_factor.pack(padx=5, pady=5)
ent_c_factor = tk.Entry(frame_factor, textvariable= c_value)
ent_c_factor.pack(padx= 5, pady= 5)

btn_get_factor_answer = tk.Button(frame_factor, bd= 3, text="Get Answer", command= get_factor_answer)
btn_get_factor_answer.pack(padx= 5, pady= 5)

lbl_factor = tk.Label(frame_factor, text="The factored form is..." , font= 'Roboto')
lbl_factor.pack(padx= 5, pady= 5 )

answer_factor = tk.Text(frame_factor, state= "disabled")
answer_factor.configure(height= 1, width= 20)
answer_factor.pack(padx=5, pady=5)

# ----- Foil Screen Elements ----- #
lbl_foil_form = tk.Label(frame_foil, text= "Enter Equation in form: (a + b)(c + d)", font= "Archivo")
lbl_foil_form.pack(padx=5, pady=5)

lbl_a_foil= tk.Label(frame_foil, text="A Value", font="Archivo")
lbl_a_foil.pack(padx=5, pady=5)
ent_a_foil = tk.Entry(frame_foil, textvariable= a_value)
ent_a_foil.pack(padx= 5, pady= 5)

lbl_b_foil= tk.Label(frame_foil, text="B Value", font="Archivo")
lbl_b_foil.pack(padx=5, pady=5)
ent_b_foil = tk.Entry(frame_foil, textvariable= b_value)
ent_b_foil.pack(padx= 5, pady= 5)

lbl_c_foil= tk.Label(frame_foil, text="C Value", font="Archivo")
lbl_c_foil.pack(padx=5, pady=5)
ent_c_foil = tk.Entry(frame_foil, textvariable= c_value)
ent_c_foil.pack(padx= 5, pady= 5)

lbl_d_foil= tk.Label(frame_foil, text="D Value", font="Archivo")
lbl_d_foil.pack(padx=5, pady=5)
ent_d_foil = tk.Entry(frame_foil, textvariable= d_value)
ent_d_foil.pack(padx= 5, pady= 5)

lbl_factorized = tk.Label(frame_foil, text="The foiled form answer is ", font= 'Roboto')
lbl_factorized.pack(padx= 5, pady= 5 )

answer_foil= tk.Text(frame_foil, state= "disabled")
answer_foil.configure(height= 1, width= 20)
answer_foil.pack(padx=5, pady=5)

# ----- Get Factors Frame ----- #
lbl_gf = tk.Label(frame_gf, text="Get factors of (eg. 12)", font= 'Roboto')
lbl_gf.pack(padx= 5, pady= 5 )

ent_gf_num= tk.Entry(frame_gf, textvariable= num)
ent_gf_num.pack(padx=5, pady=5)

gf_button = tk.Button(frame_gf, bd= 3, text="Get Factors", command= get_gf_answer)
gf_button.pack(padx= 5, pady= 5)

answer_gf = tk.Text(frame_gf, state= "disabled")
answer_gf.configure(height= 3, width= 20)
answer_gf.pack()

# ----- Navigation Buttons ----- #
btn_gf = tk.Button(frame_main, bd= 3, text="Factor Number", command= raise_gf)
btn_gf.pack(padx= 5, pady= 15)

btn_factor = tk.Button(frame_main, bd=3, text="Factor Quadratic", command= raise_factor)
btn_factor.pack(padx=50, pady=15)

btn_factorized = tk.Button(frame_main, bd=3, text="Foil", command= raise_foil)
btn_factorized.pack(padx=50, pady=15)

btn_back = tk.Button(frame_factor, bd= 3, text="Back", command= raise_main)
btn_back.pack(padx= 5, pady= 5)

btn_get_foil_answer = tk.Button(frame_foil, bd= 3, text="Get Answer", command= get_foil_answer)
btn_get_foil_answer.pack(padx= 5, pady= 5)

btn_back = tk.Button(frame_foil, bd= 3, text="Back", command= raise_main)
btn_back.pack(padx= 5, pady= 5)

btn_back = tk.Button(frame_gf, bd= 3, text="Back", command= raise_main)
btn_back.pack(padx= 5, pady= 5)


# ----- Start GUI Loop ----- #
frame_main.tkraise()
root.mainloop()
