import tkinter as tk
from tkinter import ttk, scrolledtext
from calculations import calculate_costs
from utils.api_integration import get_distance, API_KEY
from utils.fuel_api import fetch_fuel_data, parse_diesel_price
import requests
diesel_price_per_litre = None

def fetch_and_set_diesel_price():
    global diesel_price_per_litre  # Use the global variable
    url = "https://jetlocal.co.uk/fuel_prices_data.json"  # Replace with actual URL
    fuel_data = fetch_fuel_data(url)
    if fuel_data:
        diesel_price_per_litre = parse_diesel_price(fuel_data)
        if diesel_price_per_litre is None:
            diesel_price_per_litre = "Unavailable"
    else:
        diesel_price_per_litre = "Unavailable"


def launch_gui():
    # Fetch diesel price before setting up the GUI
    fetch_and_set_diesel_price()

    # GUI setup
    root = tk.Tk()
    root.title("Travel Cost Calculator")
    root.geometry("720x800")
    root.config(bg="#2c3e50")

    # Store mode state
    mode = tk.StringVar(value="automatic")  # Default to Automatic Mode

    # Function to toggle between Manual and Automatic modes
    def toggle_mode():
        if mode.get() == "manual":
            # Switch to Manual Mode
            manual_frame.grid()  # Show manual frame
            auto_frame.grid_remove()  # Hide automatic frame
        else:
            # Switch to Automatic Mode
            auto_frame.grid()  # Show automatic frame
            manual_frame.grid_remove()  # Hide manual frame

    # Function to call calculations and display results
    def calculate_and_display_results():
        try:
            if mode.get() == "manual":
                # Manual Mode: Use user-provided values
                distance = float(travel_miles_entry.get())
                diesel_price = float(fuel_cost_entry.get())
            else:
                # Automatic Mode: Use API-based values
                global diesel_price_per_litre
                if not isinstance(diesel_price_per_litre, float):
                    raise ValueError("Diesel price is unavailable.")
                distance = get_distance(API_KEY, origin_entry.get(), destination_entry.get())
                diesel_price = diesel_price_per_litre
            
            # Common inputs for both modes
            number_of_days = float(days_entry.get())
            fuel_efficiency_mpg = float(fuel_efficiency_entry.get())
            fitter_rate = float(fitter_rate_entry.get())
            apprentice_rate = float(apprentice_rate_entry.get())
            travel_option = travel_option_var.get()
            one_way_travel_time = float(travel_time_entry.get())

            # Perform the cost calculations
            result_text = calculate_costs(
                number_of_days=number_of_days,
                daily_distance=distance,
                fuel_efficiency_mpg=fuel_efficiency_mpg,
                diesel_price_per_litre=diesel_price,
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
        except ValueError as e:
            result_textbox.config(state="normal")
            result_textbox.delete("1.0", tk.END)
            result_textbox.insert(tk.END, f"Error: {e}")
            result_textbox.config(state="disabled")

    

    # Style Configurations
    style = ttk.Style()
    style.configure("TLabel", font=("Arial", 12), background="#2c3e50", foreground="#ecf0f1")
    style.configure("TButton", font=("Arial", 12, "bold"), background="#1abc9c", foreground="white", padding=10)
    style.map("TButton", background=[("active", "#16a085")])

    # Header
    header_label = ttk.Label(root, text="Travel Cost Calculator", font=("Arial", 20, "bold"), foreground="#1abc9c", background="#2c3e50")
    header_label.pack(pady=20)

    # Toggle Buttons
    toggle_frame = tk.Frame(root, bg="#2c3e50")
    toggle_frame.pack(pady=10)
    manual_button = tk.Radiobutton(
        toggle_frame, text="Manual Mode", variable=mode, value="manual",
        command=toggle_mode, bg="#2c3e50", fg="white", selectcolor="#1abc9c"
    )
    auto_button = tk.Radiobutton(
        toggle_frame, text="Automatic Mode", variable=mode, value="automatic",
        command=toggle_mode, bg="#2c3e50", fg="white", selectcolor="#1abc9c"
    )
    manual_button.pack(side="left", padx=5)
    auto_button.pack(side="left", padx=5)

    # Input Frame
    input_frame = tk.Frame(root, bg="#2c3e50")
    input_frame.pack(pady=10)

    # Manual Mode Frame
    manual_frame = tk.Frame(input_frame, bg="#2c3e50")
    tk.Label(manual_frame, text="Travel Miles:", bg="#2c3e50", fg="white").grid(row=0, column=0, padx=10, pady=5, sticky="w")
    travel_miles_entry = tk.Entry(manual_frame)
    travel_miles_entry.grid(row=0, column=1, padx=10, pady=5)
    tk.Label(manual_frame, text="Fuel Cost (£ per litre):", bg="#2c3e50", fg="white").grid(row=1, column=0, padx=10, pady=5, sticky="w")
    fuel_cost_entry = tk.Entry(manual_frame)
    fuel_cost_entry.grid(row=1, column=1, padx=10, pady=5)

    # Automatic Mode Frame
    auto_frame = tk.Frame(input_frame, bg="#2c3e50")
    tk.Label(auto_frame, text="Origin Location:", bg="#2c3e50", fg="white").grid(row=0, column=0, padx=10, pady=5, sticky="w")
    origin_entry = tk.Entry(auto_frame)
    origin_entry.grid(row=0, column=1, padx=10, pady=5)
    tk.Label(auto_frame, text="Destination Location:", bg="#2c3e50", fg="white").grid(row=1, column=0, padx=10, pady=5, sticky="w")
    destination_entry = tk.Entry(auto_frame)
    destination_entry.grid(row=1, column=1, padx=10, pady=5)

    # Common Inputs
    tk.Label(input_frame, text="Number of Days:", bg="#2c3e50", fg="white").grid(row=2, column=0, padx=10, pady=5, sticky="w")
    days_entry = tk.Entry(input_frame)
    days_entry.grid(row=2, column=1, padx=10, pady=5)

    tk.Label(input_frame, text="Fuel Efficiency (MPG):", bg="#2c3e50", fg="white").grid(row=3, column=0, padx=10, pady=5, sticky="w")
    fuel_efficiency_entry = tk.Entry(input_frame)
    fuel_efficiency_entry.grid(row=3, column=1, padx=10, pady=5)

    tk.Label(input_frame, text="Fitter Hourly Rate (£):", bg="#2c3e50", fg="white").grid(row=4, column=0, padx=10, pady=5, sticky="w")
    fitter_rate_entry = tk.Entry(input_frame)
    fitter_rate_entry.grid(row=4, column=1, padx=10, pady=5)

    tk.Label(input_frame, text="Apprentice Hourly Rate (£):", bg="#2c3e50", fg="white").grid(row=5, column=0, padx=10, pady=5, sticky="w")
    apprentice_rate_entry = tk.Entry(input_frame)
    apprentice_rate_entry.grid(row=5, column=1, padx=10, pady=5)

    tk.Label(input_frame, text="One-Way Travel Time (hours):", bg="#2c3e50", fg="white").grid(row=6, column=0, padx=10, pady=5, sticky="w")
    travel_time_entry = tk.Entry(input_frame)
    travel_time_entry.grid(row=6, column=1, padx=10, pady=5)

    # Travel Option Dropdown
    travel_option_var = tk.StringVar(value="Return + Overtime")
    ttk.Label(input_frame, text="Travel Scenario:", background="#2c3e50", foreground="white").grid(row=7, column=0, padx=10, pady=5, sticky="w")
    travel_option_dropdown = ttk.Combobox(input_frame, textvariable=travel_option_var, values=["One Way", "Return Trip", "Return + Overtime"], state="readonly")
    travel_option_dropdown.grid(row=7, column=1, padx=10, pady=5)

    # Calculate Button
    calculate_button = tk.Button(root, text="Calculate Costs", command=calculate_and_display_results, bg="#1abc9c", fg="white")
    calculate_button.pack(pady=10)

    # Results Frame
    results_frame = ttk.Frame(root)
    results_frame.pack(pady=10)
    result_textbox = scrolledtext.ScrolledText(results_frame, wrap="word", width=70, height=15, font=("Arial", 11))
    result_textbox.pack()
    result_textbox.config(state="disabled")

    # Default to Automatic Mode
    auto_frame.grid(row=0, column=0, padx=10, pady=10)
    manual_frame.grid_remove()  # Start with Manual Mode hidden

    # Start the GUI Loop
    root.mainloop()