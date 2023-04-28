import tkinter as tk
import openai
from tkinter import font as tkfont
from PIL import ImageTk, Image
import time


# Apply the API Key
openai.api_key = "" #Your API key

# Generate a response using OpenAI GPT-3
def generate_response(prompt):
    completions = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )

    message = completions.choices[0].text
    return message

# GUI interface
def display_response():
    input_text = input_field.get()
    response = generate_response(input_text)
    output_field.config(state='normal')
    output_field.delete(1.0, tk.END)
    output_field.insert(tk.END, response)
    output_field.config(state='disabled')

# Create the main window
root = tk.Tk()
root.title("Akshay's Chatbot")
root.wm_attributes('-fullscreen',True)
root.configure(bg="black")
root.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")

#create a canvas
canvas = tk.Canvas(root, width=700, height=3500)
canvas.pack(fill="both", expand=True)

#Add image
img = Image.open("Akshay's Chatbot.png")
img = img.resize((800, 600), Image.LANCZOS)
bg_img = ImageTk.PhotoImage(img)
canvas.create_image(0, 0, image=bg_img, anchor="nw")


def resize_bg(event):
    new_width = event.width
    new_height = event.height
    bg_img_resize = img.resize((new_width, new_height), Image.LANCZOS)
    canvas.bg_img = ImageTk.PhotoImage(bg_img_resize)
    canvas.itemconfig(bg, image=canvas.bg_img)

bg = canvas.create_image(0, 0, image=bg_img, anchor="nw")
canvas.bind('<Configure>', resize_bg)

# Create the input field
input_field = tk.Entry(root, font=("Helvetica", 14),relief = "solid",width=50,bg="black",fg="#08FAA3",highlightthickness=2)
input_field.config(highlightbackground="#08CD86",insertbackground="#08FAA3")
input_field.place(x=390,y=115)

# Create the submit button
submit_button = tk.Button(root, text="Submit", font=("Helvetica", 17),relief = "solid", command=display_response,bg="#0C6D4A",width=8)
submit_button.place(x=1220,y=690)
# Create the output field
output_field = tk.Text(root, font=("Helvetica", 14), state='disabled',relief = "solid",bg="black",fg="#11DA91",highlightthickness=2)
output_field.config(highlightbackground="#08CD86",insertbackground="#08FAA3")
output_field.place(x=230,y=215)

# Button for closing
exit_button = tk.Button(root, text="Exit", font=("Helvetica", 17),relief = "solid", command=root.destroy,bg="#0C6D4A",width=7)
exit_button.place(x=20,y=690)

# Start the GUI event loop
root.mainloop()

