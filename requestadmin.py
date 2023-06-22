# Cache Optimiser v1.0
# Developed by: Edward Deakin
# https://edeakin.xyz

# Import all required libraries
import os
import customtkinter

# Build the GUI
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()

def checkIfWindows():
    root.destroy()
    if(os.name != "nt"):
        os.system("clear")
        print("\nSorry! This program is not yet supported by your operating system.")
        print("Currently, only Windows machines are supported.")
        input("\nPlease press any key to exit the program. ")
    else:
        root.destroy()

root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)
root.geometry("500x400")
root.wm_title("Cache Optimiser v1.0")

frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill="both", expand=True)

label = customtkinter.CTkLabel(master=frame, text="Cache Optimiser v1.0", font=("Arial", 20))
label.pack(pady=12, padx=10)

text = customtkinter.CTkTextbox(master=frame, width=500, font=("Arial", 18))
text.insert("0.0", "To run this program, it needs\nadministrative priveleges. Click the button below to give access to the program.")
text.configure(state="disabled")
text.pack(pady=12, padx=10)

button = customtkinter.CTkButton(master=frame, text="Request Admin", command=checkIfWindows)
button.pack(pady=12, padx=10)

root.mainloop()
