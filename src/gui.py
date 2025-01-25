import tkinter as tk
from tkinter import ttk, scrolledtext
from calculations import calculate_costs
from utils.api_integration import get_distance_and_time, API_KEY
from utils.fuel_api import fetch_fuel_data, parse_diesel_price
import requests

# Global Variable for Diesel Price
diesel_price_per_litre = None

def fetch_and_set_diesel_price():
    """
    Fetch and calculate the average diesel price per litre from multiple sources.
    """
    global diesel_price_per_litre
    urls = {
        "jetlocal": "https://jetlocal.co.uk/fuel_prices_data.json",
        "applegreen": "https://applegreenstores.com/fuel-prices/data.json",
        "asconagroup": "https://fuelprices.asconagroup.co.uk/newfuel.json",
        "asda": "https://storelocator.asda.com/fuel_prices_data.json",
        "bp": "https://www.bp.com/en_gb/united-kingdom/home/fuelprices/fuel_prices_data.json",
        "esso_tesco_alliance": "https://fuelprices.esso.co.uk/latestdata.json",
        #"karanretail": "https://api2.krlmedia.com/integration/live_price/krl",
        "morrisons": "https://www.morrisons.com/fuel-prices/fuel.json",
        "moto": "https://moto-way.com/fuel-price/fuel_prices.json",
       # "rontec": "https://www.rontec-servicestations.co.uk/fuel-prices/data/fuel_prices_data.json",
        "sainsbury’s": "https://api.sainsburys.co.uk/v1/exports/latest/fuel_prices_data.json",
        "sgn": "https://www.sgnretail.uk/files/data/SGN_daily_fuel_prices.json",
        "shell": "https://www.shell.co.uk/fuel-prices-data.html",
        #"tesco": "https://www.tesco.com/fuel_prices/fuel_prices_data.json",
        
    }

    prices_per_litre = []

    for source_name, url in urls.items():
        fuel_data = fetch_fuel_data(url)
        if fuel_data:
            stations = fuel_data.get("stations", [])
            for station in stations:
                prices = station.get("prices", {})
                diesel_price = prices.get("B7")  # Assuming B7 represents diesel
                if diesel_price is not None:
                    prices_per_litre.append(diesel_price / 100)  # Convert pence to pounds

    if prices_per_litre:
        # Calculate average diesel price across all sources
        diesel_price_per_litre = sum(prices_per_litre) / len(prices_per_litre)
    else:
        diesel_price_per_litre = "Unavailable"



def launch_gui():
    # Main window
    root = tk.Tk()
    root.title("Travel Cost Calculator")
    root.geometry("720x800")
    root.config(bg="#2c3e50")

    # Mode variable (to toggle between Manual and Automatic modes)
    mode = tk.StringVar(value="automatic")  # Default mode

    # Toggle between modes
    def toggle_mode():
        if mode.get() == "manual":
            # Show manual inputs
            travel_miles_label.grid(row=0, column=0, padx=10, pady=5, sticky="e")
            travel_miles_entry.grid(row=0, column=1, padx=10, pady=5, sticky="w")
            fuel_cost_label.grid(row=1, column=0, padx=10, pady=5, sticky="e")
            fuel_cost_entry.grid(row=1, column=1, padx=10, pady=5, sticky="w")
            travel_time_label.grid()
            travel_time_entry.grid()

            # Hide automatic inputs
            origin_label.grid_remove()
            origin_entry.grid_remove()
            destination_label.grid_remove()
            destination_entry.grid_remove()
        else:
            # Hide manual inputs
            travel_miles_label.grid_remove()
            travel_miles_entry.grid_remove()
            fuel_cost_label.grid_remove()
            fuel_cost_entry.grid_remove()
            travel_time_label.grid_remove()
            travel_time_entry.grid_remove()
            

            # Show automatic inputs
            origin_label.grid(row=0, column=0, padx=10, pady=5, sticky="e")
            origin_entry.grid(row=0, column=1, padx=10, pady=5, sticky="w")
            destination_label.grid(row=1, column=0, padx=10, pady=5, sticky="e")
            destination_entry.grid(row=1, column=1, padx=10, pady=5, sticky="w")

    def calculate_and_display_results():
        try:
            global diesel_price_per_litre  # Access the global variable
            if not isinstance(diesel_price_per_litre, float):
                raise ValueError("Diesel price is unavailable.")

            # Collect inputs from GUI
            origin = origin_entry.get()
            destination = destination_entry.get()
            number_of_days = float(days_entry.get())
            fuel_efficiency_mpg = float(fuel_efficiency_entry.get())
            fitter_rate = float(fitter_rate_entry.get())
            apprentice_rate = float(apprentice_rate_entry.get())
            travel_option = travel_option_var.get()
            one_way_travel_time = None
            distance = None
            local_diesel_price = None  # Local variable for diesel price

            if mode.get() == "automatic":

                local_diesel_price = diesel_price_per_litre
                distance, one_way_travel_time = get_distance_and_time(API_KEY, origin, destination)
                if distance is None or one_way_travel_time is None:
                    raise ValueError("Unable to fetch distance or travel time. Please check your locations.")
            
            else:
                # Manual mode inputs
                distance = float(travel_miles_entry.get())
                one_way_travel_time = float(travel_time_entry.get())
                local_diesel_price = float(fuel_cost_entry.get())

            # Perform the cost calculations
            result_text = calculate_costs(
                number_of_days=number_of_days,
                daily_distance=distance,
                fuel_efficiency_mpg=fuel_efficiency_mpg,
                diesel_price_per_litre=local_diesel_price,
                fitter_rate=fitter_rate,
                apprentice_rate=apprentice_rate,
                travel_option=travel_option,
                one_way_travel_time=one_way_travel_time,
            )

            

            # Display the result in the results textbox
            result_textbox.config(state="normal")
            result_textbox.delete("1.0", tk.END)
            result_textbox.insert(tk.END, result_text)
            result_textbox.config(state="disabled")

        except ValueError as e:
            # Handle errors and display them in the results textbox
            result_textbox.config(state="normal")
            result_textbox.delete("1.0", tk.END)
            result_textbox.insert(tk.END, f"Error: {e}")
            result_textbox.config(state="disabled")



    # Header
    header_label = ttk.Label(root, text="Travel Cost Calculator", font=("Arial", 20, "bold"), foreground="#1abc9c", background="#2c3e50")
    header_label.pack(pady=20)

    # Mode Buttons
    mode_frame = tk.Frame(root, bg="#2c3e50")
    mode_frame.pack(pady=10)

    manual_button = tk.Radiobutton(mode_frame, text="Manual Mode", variable=mode, value="manual", command=toggle_mode, bg="#2c3e50", fg="white", selectcolor="#34495e")
    auto_button = tk.Radiobutton(mode_frame, text="Automatic Mode", variable=mode, value="automatic", command=toggle_mode, bg="#2c3e50", fg="white", selectcolor="#34495e")
    manual_button.grid(row=0, column=0, padx=10)
    auto_button.grid(row=0, column=1, padx=10)

    # Input Frame
    input_frame = tk.Frame(root, bg="#2c3e50")
    input_frame.pack(pady=10)

    input_frame.columnconfigure(0, weight=1)  # Column for labels
    input_frame.columnconfigure(1, weight=1)  # Column for inputs

    # Input Labels and Entries
    travel_miles_label = tk.Label(input_frame, text="Travel Miles:", bg="#2c3e50", fg="white")
    travel_miles_entry = tk.Entry(input_frame)
    fuel_cost_label = tk.Label(input_frame, text="Fuel Cost (£ per litre):", bg="#2c3e50", fg="white")
    fuel_cost_entry = tk.Entry(input_frame)

    origin_label = tk.Label(input_frame, text="Start Location:", bg="#2c3e50", fg="white")
    origin_entry = tk.Entry(input_frame)
    destination_label = tk.Label(input_frame, text="Destination Location:", bg="#2c3e50", fg="white")
    destination_entry = tk.Entry(input_frame)

    ttk.Label(input_frame, text="Number of Days:", background="#2c3e50", foreground="white").grid(row=2, column=0, padx=10, pady=5, sticky="e")
    days_entry = ttk.Entry(input_frame)
    days_entry.grid(row=2, column=1, padx=10, pady=5, sticky="w")

    ttk.Label(input_frame, text="Fuel Efficiency (MPG):", background="#2c3e50", foreground="white").grid(row=3, column=0, padx=10, pady=5, sticky="e")
    fuel_efficiency_entry = ttk.Entry(input_frame)
    fuel_efficiency_entry.grid(row=3, column=1, padx=10, pady=5, sticky="w")

    ttk.Label(input_frame, text="Fitter Hourly Rate (£):", background="#2c3e50", foreground="white").grid(row=4, column=0, padx=10, pady=5, sticky="e")
    fitter_rate_entry = ttk.Entry(input_frame)
    fitter_rate_entry.grid(row=4, column=1, padx=10, pady=5, sticky="w")

    ttk.Label(input_frame, text="Apprentice Hourly Rate (£):", background="#2c3e50", foreground="white").grid(row=5, column=0, padx=10, pady=5, sticky="e")
    apprentice_rate_entry = ttk.Entry(input_frame)
    apprentice_rate_entry.grid(row=5, column=1, padx=10, pady=5, sticky="w")

    # Frame for the Travel Time input (manual mode only)
   # Travel Time (Manual Mode Only)
    travel_time_label = ttk.Label(input_frame, text="One-Way Travel Time (minutes):", background="#2c3e50", foreground="white")
    travel_time_label.grid(row=6, column=0, padx=10, pady=5, sticky="e")  # Align label to the right
    travel_time_entry = ttk.Entry(input_frame)
    travel_time_entry.grid(row=6, column=1, padx=10, pady=5, sticky="w")  # Align entry to the left5)

    

    # Travel Option Dropdown
    travel_option_var = tk.StringVar(value="Return + Overtime")
    ttk.Label(input_frame, text="Travel Scenario:", background="#2c3e50", foreground="white").grid(row=7, column=0, padx=10, pady=5, sticky="e")
    travel_option_dropdown = ttk.Combobox(input_frame, textvariable=travel_option_var, values=["One Way", "Return Trip", "Return + Overtime"], state="readonly")
    travel_option_dropdown.grid(row=7, column=1, padx=10, pady=5)

    # Calculate Button
    calculate_button = tk.Button(root, text="Calculate Costs", command=calculate_and_display_results, bg="#1abc9c", fg="white", font=("Arial", 12, "bold"), relief="flat", bd=0)
    calculate_button.pack(pady=20)

    # Results Display
    result_textbox = scrolledtext.ScrolledText(root, wrap="word", width=70, height=16, font=("Arial", 11), bg="#ecf0f1", fg="#2c3e50", relief="flat", bd=0)
    result_textbox.pack(padx=10, pady=10)

    # Initialize toggling
    toggle_mode()
    fetch_and_set_diesel_price()

    # Start GUI loop
    root.mainloop()