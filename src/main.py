import tkinter as tk
from tkinter import ttk, scrolledtext

# Function to calculate costs
def calculate_costs():
    try:
        number_of_days = float(days_entry.get())
        daily_distance = float(distance_entry.get())
        fuel_cost_per_gallon = float(fuel_cost_entry.get())
        fuel_efficiency_mpg = float(fuel_efficiency_entry.get())
        fitter_rate = float(fitter_rate_entry.get())
        apprentice_rate = float(apprentice_rate_entry.get())
        travel_option = travel_option_var.get()
        one_way_travel_time = float(travel_time_entry.get())

        fitter_overtime = fitter_rate * 1.5
        apprentice_overtime = apprentice_rate * 1.5

        # Adjust fuel cost based on travel scenario
        if travel_option == "One Way":
            adjusted_distance = daily_distance / 2  # Half the distance
        elif travel_option in ["Return Trip", "Return + Overtime"]:
            adjusted_distance = daily_distance  # Full distance

        # Fuel calculations
        daily_fuel_usage = adjusted_distance / fuel_efficiency_mpg
        daily_fuel_cost = daily_fuel_usage * fuel_cost_per_gallon

        # Labour travel cost calculations
        if travel_option == "One Way":
            fitter_travel_cost = one_way_travel_time * fitter_rate
            apprentice_travel_cost = one_way_travel_time * apprentice_rate
        elif travel_option == "Return Trip":
            fitter_travel_cost = 2 * one_way_travel_time * fitter_rate
            apprentice_travel_cost = 2 * one_way_travel_time * apprentice_rate
        elif travel_option == "Return + Overtime":
            fitter_travel_cost = (one_way_travel_time * fitter_rate) + (one_way_travel_time * fitter_overtime)
            apprentice_travel_cost = (one_way_travel_time * apprentice_rate) + (one_way_travel_time * apprentice_overtime)

        # Totals
        daily_labor_travel_cost = fitter_travel_cost + apprentice_travel_cost
        daily_total_travel_cost = daily_labor_travel_cost + daily_fuel_cost
        total_travel_cost = daily_total_travel_cost * number_of_days

        # Result breakdown
        result_text = (
            f"=== Travel Cost Breakdown ===\n"
            f"Travel Scenario: {travel_option}\n"
            f"Adjusted Daily Distance: {adjusted_distance} miles\n"
            f"Fuel Efficiency: {fuel_efficiency_mpg} MPG\n"
            f"Fuel Cost per Gallon: £{fuel_cost_per_gallon:.2f}\n"
            f"Daily Fuel Cost: £{daily_fuel_cost:.2f}\n\n"
            f"--- Labour Costs ---\n"
            f"Fitter Travel Cost (Daily): £{fitter_travel_cost:.2f}\n"
            f"Apprentice Travel Cost (Daily): £{apprentice_travel_cost:.2f}\n"
            f"Total Daily Labour Travel Cost: £{daily_labor_travel_cost:.2f}\n\n"
            f"--- Totals ---\n"
            f"Daily Travel Overhead (Labour + Fuel): £{daily_total_travel_cost:.2f}\n"
            f"Total Travel Cost for {number_of_days} Days: £{total_travel_cost:.2f}"
        )
        result_textbox.config(state="normal")
        result_textbox.delete("1.0", tk.END)
        result_textbox.insert(tk.END, result_text)
        result_textbox.config(state="disabled")
    except ValueError:
        result_textbox.config(state="normal")
        result_textbox.delete("1.0", tk.END)
        result_textbox.insert(tk.END, "Invalid input! Please enter numeric values.")
        result_textbox.config(state="disabled")


# GUI Setup
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
    ("Number of Days:", "days_entry"),
    ("Daily Round Trip Distance (miles):", "distance_entry"),
    ("Fuel Cost per Gallon (£):", "fuel_cost_entry"),
    ("Fuel Efficiency (MPG):", "fuel_efficiency_entry"),
    ("Fitter Hourly Rate (£):", "fitter_rate_entry"),
    ("Apprentice Hourly Rate (£):", "apprentice_rate_entry"),
    ("One-Way Travel Time (hours):", "travel_time_entry")
]

entries = {}
for i, (label, var_name) in enumerate(fields):
    ttk.Label(input_frame, text=label).grid(row=i, column=0, sticky="w", padx=10, pady=5)
    entry = tk.Entry(input_frame, font=("Arial", 11), bg="#ecf0f1", fg="#333333", relief="flat", bd=0)
    entry.grid(row=i, column=1, padx=10, pady=5, ipady=6, ipadx=8)
    entries[var_name] = entry

# Assign variables
days_entry = entries["days_entry"]
distance_entry = entries["distance_entry"]
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
calculate_button = tk.Button(root, text="Calculate Costs", command=calculate_costs, font=("Arial", 12, "bold"), bg="#1abc9c", fg="white", activebackground="#16a085", activeforeground="white", relief="flat", bd=0)
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

