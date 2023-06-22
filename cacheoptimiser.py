# Cache Optimiser v1.0
# Developed by: Edward Deakin
# https://edeakin.xyz

# Import all required libraries
import os
import customtkinter
import time

# Build the GUI
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)
root.wm_title("Cache Optimiser v1.0")
root.geometry("500x400")

def clearCache():
    root.destroy()
    os.system("cls")
    os.system("echo Cache Optimiser v1.0")
    os.system("echo. ")
    os.system("echo Running sfc /scannow:")
    os.system("sfc /scannow")
    os.system("cls")
    os.system("echo Cache Optimiser v1.0")
    os.system("echo. ")
    os.system("echo Running ipconfig /flushdns:")
    os.system("ipconfig /flushdns")
    os.system("cls")
    os.system("echo Cache Optimiser v1.0")
    os.system("echo. ")
    os.system("echo Running ipconfig /registerdns:")
    os.system("ipconfig /registerdns")
    os.system("cls")
    os.system("echo Cache Optimiser v1.0")
    os.system("echo. ")
    os.system("echo Running ipconfig /release:")
    os.system("ipconfig /release")
    os.system("cls")
    os.system("echo Cache Optimiser v1.0")
    os.system("echo. ")
    os.system("echo Running ipconfig /renew:")
    os.system("ipconfig /renew")
    os.system("cls")
    os.system("echo Cache Optimiser v1.0")
    os.system("echo. ")
    os.system("echo Running netsh winsock reset:")
    os.system("netsh winsock reset")
    os.system("cls")
    os.system("echo Complete!")
    time.sleep(2)
    os.system("python finished.py")


frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill="both", expand=True)

label = customtkinter.CTkLabel(master=frame, text="Cache Optimiser v1.0", font=("Arial", 20))
label.pack(pady=12, padx=10)

text = customtkinter.CTkTextbox(master=frame, width=500, font=("Arial", 18))
text.insert("0.0", "Welcome to my Cache Optimiser!\nThis is a wrapper for a set of DNS Cache\nclearing BAT commands.\n\nThe program will start if you click the\nbutton below.")
text.configure(state="disabled")
text.pack(pady=12, padx=10)

button = customtkinter.CTkButton(master=frame, text="Start Clearing", command=clearCache)
button.pack(pady=12, padx=10)

root.mainloop()