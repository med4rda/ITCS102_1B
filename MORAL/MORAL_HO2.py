import tkinter as tk
window = tk.Tk()

window.title("MORAL_HO2")
window.geometry("600x600")
window.resizable(False, True)
window.configure(bg="gray")

label = tk.Label(window, text="STUDENT PROFILE", font=("Arial", 24, "bold"), bg="gray",fg="black")
label.pack(pady=20)

label = tk.Label(window, text="Full Name: Jose Paulo V. Moral", font=("Arial", 24), bg="gray",fg="white")
label.pack(pady=20, padx=20,anchor="w")

label = tk.Label(window, text="Age: 23 years old", font=("Arial", 24), bg="gray",fg="white", justify= "left")
label.pack(pady=20, padx=20,anchor="w")

label = tk.Label(window, text="Course: BSIT", font=("Arial", 24), bg="gray",fg="white", justify= "left")
label.pack(pady=20, padx=20, anchor="w")

label = tk.Label(window, text="Birthday: January 26, 2003", font=("Arial", 24), bg="gray",fg="white", justify= "left")
label.pack(pady=20,padx=20, anchor="w")

label = tk.Label(window, text="Motto:", font=("Arial", 24), bg="gray",fg="white", justify= "left")
label.pack(pady=20, padx=20, anchor="w")

label = tk.Label(window, text=f"We do it not because it was easy, but because we thought it would be easy.", font=("Arial", 24), bg="gray",fg="red", justify= "left")
label.pack(pady=20, padx=20, anchor="w")


label = tk.Label(window, text=f"""
                 Twinkle, twinkle, little star, 
                 how I wonder what you are. 
                 Up above the world so high,
                 like a diamond in the sky. 
                 Twinkle, twinkle, little star,
                 how I wonder what you are.
                 When the blazing sun is set, 
                 and the grass with dew is wet.
                 Then you show your little
                 light, twinkle, twinkle all the night. 
                 Twinkle, twinkle little star, 
                 how I wonder what you are.
""", font=("Arial", 24), bg="gray",fg="red", justify= "left")
label.pack(anchor="center")
window.mainloop()