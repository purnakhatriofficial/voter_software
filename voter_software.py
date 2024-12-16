from tkinter import Tk, Label, Entry, Button

def voter_age():
    try:
        age = int(age_entry.get())
        if age >= 18:
            result_label.config(text="You are eligible to vote.", font=("Helvetica", 20), fg="green")
        else:
            result_label.config(text="You are not eligible to vote.", font=("Helvetica", 20), fg="red")
    except ValueError:
        result_label.config(text="Please enter a valid age.", font=("Helvetica", 20), fg="orange")

def clear_fields():
    age_entry.delete(0, 'end')
    result_label.config(text="", font=("Helvetica", 14))

# Create a main window
root = Tk()
root.title("Voter Software")
root.geometry("500x500")

# Create a label for the age entry
label_age = Label(root, text="Enter your age:", font=("Helvetica", 14))
label_age.pack(pady=20)
age_entry = Entry(root, font=("Helvetica", 20))
age_entry.pack(pady=10)

# Create a button to check voter age
check_button = Button(root, cursor="hand2", bg="lightblue", text="Check Eligibility", font=("Helvetica", 14), command=voter_age)
check_button.pack(pady=20)

# Create a button to clear the fields
clear_button = Button(root, cursor="hand2", bg="red", width=12, text="Clear", font=("Helvetica", 14), command=clear_fields)
clear_button.pack(pady=10)

# Create a label to display the result
result_label = Label(root, text="", font=("Helvetica", 14))
result_label.pack(pady=20)

# Run the main loop
root.mainloop()
