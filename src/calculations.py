def calculate_costs(number_of_days, daily_distance, fuel_efficiency_mpg, diesel_price_per_litre,
                    fitter_rate, apprentice_rate, travel_option, one_way_travel_time, manual_mode=False,):
    travel_time_in_hours = one_way_travel_time / 60
    fitter_overtime = fitter_rate * 1.5
    apprentice_overtime = apprentice_rate * 1.5

    if travel_option == "One Way":
        adjusted_distance = daily_distance 
    elif travel_option == "Return Trip": 
        adjusted_distance = daily_distance * 2
    elif travel_option == "Return + Overtime":
        adjusted_distance = daily_distance * 2

    mpl = fuel_efficiency_mpg / 4.546
    liters_per_mile = 1 / mpl
    daily_fuel_usage = adjusted_distance * liters_per_mile
    daily_fuel_cost = daily_fuel_usage * diesel_price_per_litre 

    if travel_option == "One Way":
        fitter_travel_cost = travel_time_in_hours * fitter_rate
        apprentice_travel_cost = travel_time_in_hours * apprentice_rate
    elif travel_option == "Return Trip":
        fitter_travel_cost = 2 * travel_time_in_hours * fitter_rate
        apprentice_travel_cost = 2 * travel_time_in_hours * apprentice_rate
    elif travel_option == "Return + Overtime":
        fitter_travel_cost = (travel_time_in_hours * fitter_rate) + (travel_time_in_hours * fitter_overtime)
        apprentice_travel_cost = (travel_time_in_hours * apprentice_rate) + (travel_time_in_hours * apprentice_overtime)

    daily_labor_travel_cost = fitter_travel_cost + apprentice_travel_cost
    daily_total_travel_cost = daily_labor_travel_cost + daily_fuel_cost
    total_travel_cost = daily_total_travel_cost * number_of_days

    if manual_mode:
        travel_time = one_way_travel_time
    else:
        travel_time = one_way_travel_time 
    

    return (
        f"=== Travel Cost Breakdown ===\n"
        f"Travel Scenario: {travel_option}\n" #I think I need to add minutes it in here and the logic for manual, auto above?
        f"Adjusted Daily Distance: {adjusted_distance} miles\n"
        f"One-Way Travel Time: {travel_time:.1f} minutes\n"
        f"Fuel Efficiency: {fuel_efficiency_mpg} MPG\n"
        f"Diesel Per Ltr: £{diesel_price_per_litre:.2f}\n"
        f"Daily Fuel Cost: £{daily_fuel_cost:.2f}\n\n"
        f"--- Labour Costs ---\n"
        f"Fitter Travel Cost (Daily): £{fitter_travel_cost:.2f}\n"
        f"Apprentice Travel Cost (Daily): £{apprentice_travel_cost:.2f}\n"
        f"Total Daily Labour Travel Cost: £{daily_labor_travel_cost:.2f}\n\n"
        f"--- Totals ---\n"
        f"Daily Travel Overhead (Labour + Fuel): £{daily_total_travel_cost:.2f}\n"
        f"Total Travel Cost for {number_of_days} Days: £{total_travel_cost:.2f}"
    )
