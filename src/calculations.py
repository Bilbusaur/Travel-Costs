def calculate_costs(number_of_days, daily_distance, fuel_cost_per_gallon, fuel_efficiency_mpg,
                    fitter_rate, apprentice_rate, travel_option, one_way_travel_time):
    fitter_overtime = fitter_rate * 1.5
    apprentice_overtime = apprentice_rate * 1.5

    if travel_option == "One Way":
        adjusted_distance = daily_distance / 2
    elif travel_option in ["Return Trip", "Return + Overtime"]:
        adjusted_distance = daily_distance

    daily_fuel_usage = adjusted_distance / fuel_efficiency_mpg
    daily_fuel_cost = daily_fuel_usage * fuel_cost_per_gallon

    if travel_option == "One Way":
        fitter_travel_cost = one_way_travel_time * fitter_rate
        apprentice_travel_cost = one_way_travel_time * apprentice_rate
    elif travel_option == "Return Trip":
        fitter_travel_cost = 2 * one_way_travel_time * fitter_rate
        apprentice_travel_cost = 2 * one_way_travel_time * apprentice_rate
    elif travel_option == "Return + Overtime":
        fitter_travel_cost = (one_way_travel_time * fitter_rate) + (one_way_travel_time * fitter_overtime)
        apprentice_travel_cost = (one_way_travel_time * apprentice_rate) + (one_way_travel_time * apprentice_overtime)

    daily_labor_travel_cost = fitter_travel_cost + apprentice_travel_cost
    daily_total_travel_cost = daily_labor_travel_cost + daily_fuel_cost
    total_travel_cost = daily_total_travel_cost * number_of_days

    return (
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
