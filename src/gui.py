import tkinter as tk
from tkinter import ttk, scrolledtext
from calculations import calculate_costs
from utils.api_integration import get_distance, API_KEY
import requests


def launch_gui():
    # Function to call calculations and display results
    def calculate_and_display_results():
        try:
            # Collect inputs from GUI
            origin = origin_entry.get()
            destination = destination_entry.get()
            number_of_days = float(days_entry.get())
            fuel_cost_per_gallon = float(fuel_cost_entry.get())
            fuel_efficiency_mpg = float(fuel_efficiency_entry.get())
            fitter_rate = float(fitter_rate_entry.get())
            apprentice_rate = float(apprentice_rate_entry.get())
            travel_option = travel_option_var.get()
            one_way_travel_time = float(travel_time_entry.get())

            #Fetch distance from the API
            distance = get_distance(API_KEY, origin, destination)
            if distance is None:
                raise ValueError("Unable to fetch distance. Please check your locations")

            # Call calculate_costs from calculations.py
            result_text = calculate_costs(
            number_of_days=number_of_days,
            daily_distance=distance,
            fuel_cost_per_gallon=fuel_cost_per_gallon,
            fuel_efficiency_mpg=fuel_efficiency_mpg,
            fitter_rate=fitter_rate,
            apprentice_rate=apprentice_rate,
            travel_option=travel_option,
            one_way_travel_time=one_way_travel_time,
            )

            # Display the result
            result_textbox.config(state="normal")
            result_textbox.delete("1.0", tk.END)
            result_textbox.insert(tk.END, result_text)
            result_textbox.config(state="disabled")
        except ValueError:
            result_textbox.config(state="normal")
            result_textbox.delete("1.0", tk.END)
            result_textbox.insert(tk.END, "Invalid input! Please enter numeric values.")
            result_textbox.config(state="disabled")

    # GUI setup
    root = tk.Tk()
    root.title("Travel Cost Calculator")
    root.geometry("720x800")
    root.config(bg="#2c3e50")  # Dark Blue Background

    # Style Configurations
    style = ttk.Style()
    style.configure("TLabel", font=("Arial", 12), background="#2c3e50", foreground="#ecf0f1")
    style.configure("TButton", font=("Arial", 12, "bold"), background="#1abc9c", foreground="white", padding=10)
    style.map("TButton", background=[("active", "#16a085")])

    # Header
    header_label = ttk.Label(root, text="Travel Cost Calculator", font=("Arial", 20, "bold"), foreground="#1abc9c", background="#2c3e50")
    header_label.pack(pady=20)

    # Input Frame
    input_frame = tk.Frame(root, bg="#2c3e50")
    input_frame.pack(pady=10)

    fields = [
            ("Origin Location:", "origin_entry"),
            ("Destination Location:", "destination_entry"),
            ("Number of Days:", "days_entry"),
            ("Fuel Cost per Gallon (£):", "fuel_cost_entry"),
            ("Fuel Efficiency (MPG):", "fuel_efficiency_entry"),
            ("Fitter Hourly Rate (£):", "fitter_rate_entry"),
            ("Apprentice Hourly Rate (£):", "apprentice_rate_entry"),
            ("One-Way Travel Time (hours):", "travel_time_entry"),
]


    entries = {}
    for i, (label, var_name) in enumerate(fields):
        ttk.Label(input_frame, text=label).grid(row=i, column=0, sticky="w", padx=10, pady=5)
        entry = tk.Entry(input_frame, font=("Arial", 11), bg="#ecf0f1", fg="#333333", relief="flat", bd=0)
        entry.grid(row=i, column=1, padx=10, pady=5, ipady=6, ipadx=8)
        entries[var_name] = entry


    # Assign variables
    origin_entry = entries["origin_entry"]
    destination_entry = entries["destination_entry"]
    days_entry = entries["days_entry"]
    fuel_cost_entry = entries["fuel_cost_entry"]
    fuel_efficiency_entry = entries["fuel_efficiency_entry"]
    fitter_rate_entry = entries["fitter_rate_entry"]
    apprentice_rate_entry = entries["apprentice_rate_entry"]
    travel_time_entry = entries["travel_time_entry"]


    # Travel Option Dropdown
    travel_option_var = tk.StringVar(value="Return + Overtime")
    ttk.Label(input_frame, text="Travel Scenario:").grid(row=len(fields), column=0, sticky="w", padx=10, pady=5)
    travel_option_dropdown = ttk.Combobox(input_frame, textvariable=travel_option_var, values=["One Way", "Return Trip", "Return + Overtime"], state="readonly", font=("Arial", 11), width=19)
    travel_option_dropdown.grid(row=len(fields), column=1, padx=10, pady=5)

    # Calculate Button
    calculate_button = tk.Button(root, text="Calculate Costs", command=calculate_and_display_results, font=("Arial", 12, "bold"), bg="#1abc9c", fg="white", activebackground="#16a085", activeforeground="white", relief="flat", bd=0)
    calculate_button.pack(pady=15, ipady=6, ipadx=20)

    # Results Frame
    results_frame = ttk.Frame(root, style="TFrame")
    results_frame.pack(pady=10)

    # Scrollable Text Output
    result_textbox = scrolledtext.ScrolledText(results_frame, wrap="word", width=70, height=15, font=("Arial", 11), background="#ecf0f1", foreground="#2c3e50", relief="flat", bd=0)
    result_textbox.pack(padx=10, pady=10)
    result_textbox.config(state="disabled")

    # Footer
    footer_label = ttk.Label(root, text="Bilbo's Travel Cost Calculator", font=("Arial", 10), foreground="#95a5a6", background="#2c3e50")
    footer_label.pack(pady=10)

    # Start the GUI Loop
    root.mainloop()

