# Travel Cost Calculator 🚗💰

**README**

**Travel Cost Calculator**
An intuitive Python application designed to calculate travel costs dynamically using real-world data. This tool integrates with the **Google Maps Distance Matrix API** and live diesel price feeds to provide accurate, actionable results for a plumbing business.

---

**Current Features**
- **Dynamic Distance Calculation**:
   - Automatically fetches distances between locations using the **Google Maps Distance Matrix API**.
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
1. Enter the origin and destination for the journey.
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

---

**Future Goals**
1. **Toggle for One-Way Travel Time**:
   - Add an option to let the Google API calculate travel time dynamically, simplifying input.

2. **Manual Mileage Input**:
   - Provide a fallback for manual mileage input in case of API failures.

3. **Program Polish**:
   - Improve the interface design for clarity and usability.
   - Streamline error handling and provide helpful feedback for incorrect inputs.

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

### **Acknowledgments**
This project wouldn’t be possible without the power of APIs, dynamic problem-solving, and a good bit of perseverance. 🐒🔥✨

---

How does that look, Captain? Let me know if you’d like any tweaks or additions! 🚀✨
