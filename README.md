# Tourist Carbon Footprint Dashboard

A data-driven application to track, calculate, and visualize carbon emissions from tourism activities. This dashboard helps travelers understand their environmental impact and make sustainable travel choices.

## Features

- **Carbon Calculation Engine**: Compute CO2 emissions based on:
  - Flight distances and class (economy, business, first)
  - Hotel accommodation duration and type
  - Ground transportation (car, train, bus)
  - Activity types and frequency

- **Interactive Dashboard**: 
  - Real-time carbon footprint tracking
  - Comparison across different travel methods
  - Historical data analysis
  - Visual breakdown of emissions by category

- **Data Visualization**:
  - Pie charts for emissions distribution
  - Line graphs for trend analysis
  - Bar charts for transportation comparison
  - Interactive filtering and date range selection

- **Sustainability Tips**: Personalized recommendations based on travel patterns

## Tech Stack

- **Python 3.8+**
- **Pandas**: Data manipulation and analysis
- **NumPy**: Numerical computations
- **Matplotlib & Seaborn**: Data visualization
- **Flask**: Web framework for dashboard
- **SQLite**: Local database for travel records

## Installation

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Steps

1. Clone the repository:
```bash
git clone https://github.com/bhupendraydv/tourist-carbon-footprint.git
cd tourist-carbon-footprint
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Project Structure

```
tourist-carbon-footprint/
├─ data/
├─ src/
│  ├─ carbon_calculator.py
│  ├─ data_processor.py
│  ├─ visualizations.py
│  ├─ database.py
│  ├─ app.py
├─ notebooks/
│  ├─ analysis.ipynb
│  ├─ data_exploration.ipynb
├─ tests/
├─ requirements.txt
├─ README.md
├─ LICENSE
└─ .gitignore
```

## Usage

### Running the Dashboard

```bash
python src/app.py
```

The dashboard will be available at `http://localhost:5000`

### Using the Carbon Calculator

```python
from src.carbon_calculator import CarbonCalculator

calc = CarbonCalculator()

# Calculate flight emissions
flight_co2 = calc.calculate_flight(distance_km=2000, passengers=1, class='economy')

# Calculate accommodation
hotel_co2 = calc.calculate_accommodation(days=5, type='standard')

# Total footprint
total = calc.calculate_total_footprint(flights=[flight_co2], accommodation=hotel_co2)
print(f"Total CO2: {total} kg")
```

## Key Modules

### carbon_calculator.py
Core calculation logic for carbon emissions:
- Flight emissions based on IPCC methodology
- Hotel stay calculations
- Transportation modes
- Activity-based emissions

### data_processor.py
Handles data cleaning and preparation:
- CSV import/export
- Data validation
- Time-series processing
- Aggregation functions

### visualizations.py
Creates interactive visualizations:
- Matplotlib plots
- Statistical charts
- Comparison visualizations

### database.py
Database management:
- SQLite operations
- CRUD operations for travel records
- Data persistence

## Emission Factors

This project uses widely accepted carbon emission factors:
- **Flights**: 0.255 kg CO2 per km (economy)
- **Hotels**: 15-30 kg CO2 per night (based on category)
- **Car**: 0.21 kg CO2 per km (average)
- **Train**: 0.041 kg CO2 per km
- **Bus**: 0.089 kg CO2 per km

## Analysis Results

The dashboard provides insights into:
- Monthly carbon emissions trends
- Comparison of different travel methods
- Seasonal travel patterns
- Environmental impact statistics

## Contributing

Contributions are welcome! Please feel free to submit pull requests or open issues for bugs and feature suggestions.

## Future Enhancements

- [ ] Real-time weather data integration
- [ ] Carbon offset recommendations
- [ ] Integration with travel booking APIs
- [ ] Multi-user support
- [ ] Mobile app version
- [ ] Advanced ML predictions

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## References

- IPCC Guidelines for Carbon Accounting
- Global Sustainable Tourism Council Standards
- Carbon Trust Methodology

## Contact

For questions or suggestions, feel free to reach out at [your email].

---

**Last Updated**: December 2025
