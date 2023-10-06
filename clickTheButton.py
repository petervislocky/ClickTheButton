import tkinter as tk

def print_to_console(firstLineText, secondLineText=""):
    #writing to, and refreshing the first line of text. Enables write, clears the line, inserts text, disables write. repeated whenever method is called
    console.config(state=tk.NORMAL)
    console.delete("1.0", "1.end")
    console.insert("1.0", firstLineText + '\n')
    console.config(state=tk.DISABLED)
    #appending a second line of text that refreshes independently from the first line
    if secondLineText:
        console.config(state=tk.NORMAL)
        console.delete("2.0", "2.end")
        console.insert("2.0", secondLineText + '\n')
        console.config(state=tk.DISABLED)

def on_button_click():
    global click_count
    click_count += 1
    if click_count == 69:
        print_to_console("Button clicked 69 times!", "Nice ;)")
    elif click_count == 100:
        print_to_console("Button clicked 100 times!", "Keep going!")
    elif click_count == 200:
        print_to_console("Button clicked 200 times!", "You're a beast!")
    elif click_count == 300:
        print_to_console("Button clicked 300 times!", "Unstoppable!!")
    elif click_count == 400:
        print_to_console("Button clicked 400 times!", "Okay... this is getting absurd")
    elif click_count == 500:
        print_to_console("Button clicked 500 times!", "All right, this is getting excessive, go touch grass")
    else:    
        print_to_console(f"Button clicked {click_count} times!")

click_count = 0

root =  tk.Tk()
root.title("Click the button!")

button = tk.Button(root, text="Click me!", command=on_button_click)
label = tk.Label(root, text="Hello!")
console = tk.Text(root, height=2, width=40, state=tk.DISABLED)

label.pack(padx=12, pady=16)
button.pack(padx=12, pady=16)
console.pack(padx=12, pady=16)


root.mainloop()


