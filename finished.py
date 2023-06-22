# Cache Optimiser v1.0
# Developed by: Edward Deakin
# https://edeakin.xyz

# Import all required libraries
import os
import customtkinter
import webbrowser

# Build the GUI
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()

def exitBat():
    root.destroy()
    exit()

def website():
    webbrowser.open("https://edeakin.xyz")

root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)
root.geometry("500x450")
root.wm_title("Cache Optimiser v1.0")

frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill="both", expand=True)

label = customtkinter.CTkLabel(master=frame, text="Cache Optimiser v1.0", font=("Arial", 20))
label.pack(pady=12, padx=10)

text = customtkinter.CTkTextbox(master=frame, width=500, font=("Arial", 18))
text.insert("0.0", "The program has ran successfully.\nTo exit, click the button below or use the\ncross above.")
text.configure(state="disabled")
text.pack(pady=12, padx=10)

button = customtkinter.CTkButton(master=frame, text="Exit", command=exitBat)
button.pack(pady=12, padx=10)
button2 = customtkinter.CTkButton(master=frame, text="Visit My Website", command=website)
button2.pack(pady=12, padx=10)

root.mainloop()
