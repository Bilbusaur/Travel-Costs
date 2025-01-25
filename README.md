# Travel Cost Calculator 🚗💰

**README**

**Travel Cost Calculator**
An intuitive Python application designed to calculate travel costs dynamically using real-world data. This tool integrates with the **Google Maps Distance Matrix API** and live diesel price feeds to provide accurate, actionable results for a plumbing business.

---

**Current Features**
- **Dynamic Distance Calculation**:
   - Automatically fetches distances and travel times between locations using the **Google Maps Distance Matrix API**.
   - Adjusts distances based on travel scenarios (e.g., One Way, Return Trip, or Return + Overtime).

- **Live Fuel Price Integration**:
   - Fetches and converts diesel prices per liter directly from a government fuel price API.
   - Accurately calculates fuel costs based on real-time prices and vehicle efficiency.

- **Comprehensive Travel Cost Breakdown**:
   - Calculates fuel costs, labor travel costs, and total travel overhead for configurable scenarios.
   - Supports one-way and round-trip calculations with flexible overtime options.

- **GUI Integration**:
   - A user-friendly interface built with Tkinter, allowing simple input and instant results.

---

**How It Works**
1. Enter the start and destination for the journey.
2. Input details such as:
   - Number of days.
   - Fuel efficiency (in MPG).
   - Labor rates for fitters and apprentices.
3. Select the travel scenario:
   - **One Way**
   - **Return Trip**
   - **Return + Overtime**
4. View the detailed cost breakdown:
   - Daily and total costs for fuel, labor, and travel.
5. Manual & Automatic mode 
   - Automatic mode - collects the fuel price, ditstance miles and minutes as inputs.
   - Manual back up mode, manually enter one-way distance and fuel prices and travel time for the calculations.

---

**Tech Stack**
- **Python**: Core logic and API integrations.
- **Tkinter**: User interface design.
- **Google Maps Distance Matrix API**: Dynamic distance and time calculations.
- **Government Fuel API**: Real-time diesel price data.

---

**Setup**
1. Clone the repository:
   ```bash
   git clone https://github.com/Bilbusaur/Travel-Costs
   cd Travel-Costs
   ```
2. Install required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the program:
   ```bash
   python src/main.py
   ```

---

🐒🔥✨

---
## License

**All Rights Reserved**

This project and its associated code are protected under copyright law. Redistribution, modification, or commercial use is strictly prohibited without prior written consent from the author.

Copyright © 2025 Billy. All Rights Reserved.


