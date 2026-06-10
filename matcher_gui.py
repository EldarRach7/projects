import pandas as pd
import tkinter as tk
from tkinter import ttk

df = pd.read_excel("C:/projects/apartments.xlsx")

root = tk.Tk()
root.title("Apartment Matcher")
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root.geometry(f"{screen_width}x{screen_height}")

# Title
title = tk.Label(root, text="Find Your Perfect Apartment", font=("Arial", 16, "bold"))
title.pack(pady=10)

# City
tk.Label(root, text="City:").pack()
city_entry = tk.Entry(root, width=30)
city_entry.pack(pady=5)

# Bedrooms
tk.Label(root, text="Bedrooms:").pack()
bedrooms_entry = tk.Entry(root, width=30)
bedrooms_entry.pack(pady=5)

# Max Price
tk.Label(root, text="Max Price:").pack()
price_entry = tk.Entry(root, width=30)
price_entry.pack(pady=5)

# Furnished
tk.Label(root, text="Furnished:").pack()
furnished_var = tk.StringVar(value="yes")
furnished_menu = ttk.Combobox(root, textvariable=furnished_var, values=["yes", "no", "partially"], state="readonly", width=28)
furnished_menu.pack(pady=5)

# Optional filters checkbox
optional_var = tk.BooleanVar()
optional_check = tk.Checkbutton(root, text="Add optional filters?", variable=optional_var)
optional_check.pack(pady=10)

# Optional filters frame
optional_frame = tk.Frame(root)

tk.Label(optional_frame, text="Optional Filters:", font=("Arial", 9)).pack()

parking_var = tk.BooleanVar()
tk.Checkbutton(optional_frame, text="Parking required", variable=parking_var).pack(anchor="w", padx=20)

elevator_var = tk.BooleanVar()
tk.Checkbutton(optional_frame, text="Elevator required", variable=elevator_var).pack(anchor="w", padx=20)

balcony_var = tk.BooleanVar()
tk.Checkbutton(optional_frame, text="Balcony required", variable=balcony_var).pack(anchor="w", padx=20)

divided_var = tk.BooleanVar()
tk.Checkbutton(optional_frame, text="Must be dividable", variable=divided_var).pack(anchor="w", padx=20)

tk.Label(optional_frame, text="Special traits:", font=("Arial", 9)).pack(anchor="w", padx=20)
special_entry = tk.Entry(optional_frame, width=30)
special_entry.pack(padx=20, pady=2)

optional_frame.pack_forget()

def toggle_optional():
    if optional_var.get():
        optional_frame.pack(pady=10)
    else:
        optional_frame.pack_forget()

optional_check.config(command=toggle_optional)

def search():
    try:
        city = city_entry.get()
        bedrooms = int(bedrooms_entry.get())
        max_price = int(price_entry.get())
        isFurnished = furnished_var.get()
        
        matches = df[(df["City"] == city) & 
                     (df["Bedrooms"] >= bedrooms) & 
                     (df["Price"] <= max_price) &
                     (df["Furnished (Y/N)"].str.strip().str.lower() == isFurnished)]
        
        if optional_var.get():
            if parking_var.get():
                matches = matches[matches["Parking (Y/N)"].str.strip().str.lower() == "yes"]
            if elevator_var.get():
                matches = matches[matches["Elevator (Y/N)"].str.strip().str.lower() == "yes"]
            if balcony_var.get():
                matches = matches[matches["Balcony (Y/N)"].str.strip().str.lower() == "yes"]
            if divided_var.get():
                matches = matches[matches["Divided"].str.strip().str.lower() == "yes"]
            if special_entry.get():
                special_keywords = special_entry.get().strip().lower()
                matches = matches[matches["Special"].str.lower().str.contains(special_keywords, na=False)]
        
        matches = matches.sort_values("Price")
        
        results_text.delete(1.0, tk.END)
        results_text.insert(tk.END, f"Found {len(matches)} apartments:\n\n")
        display_columns = ["Address", "City", "Bedrooms", "Floor", "Price"]
        results_text.insert(tk.END, matches[display_columns].to_string(index=False))
    except Exception as e:
        results_text.delete(1.0, tk.END)
        results_text.insert(tk.END, f"Error: {str(e)}")

search_btn = tk.Button(root, text="Search", command=search, bg="blue", fg="white", width=30)
search_btn.pack(pady=20)

# Results display
results_text = tk.Text(root, height=15, width=80)
results_text.pack(pady=10)

root.mainloop()