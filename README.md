# 🌍 Tourist Carbon Footprint Dashboard

<div align="center">
  <p>
    <strong>A data-driven dashboard to calculate and visualize carbon footprint impact from tourism activities</strong>
  </p>
  <p>
    <em>Track emissions from flights, accommodation, and transportation. Make sustainable travel choices.</em>
  </p>
</div>

---

## 🎯 About

Tourist Carbon Footprint Dashboard is a comprehensive application designed to help travelers understand and minimize their environmental impact. By tracking and calculating CO2 emissions from various tourism activities, this dashboard empowers users to make informed, sustainable travel decisions.

## ✨ Features

### 📊 Carbon Calculation Engine
- **Flight Emissions**: Calculate CO2 based on distance, class (economy, business, first)
- **Accommodation**: Track emissions from hotel stays by duration and type
- **Ground Transportation**: Support for car, train, and bus emissions
- **Activity-Based Emissions**: Track emissions from various travel activities

### 📈 Interactive Dashboard
- **Real-time Tracking**: Monitor your carbon footprint in real-time
- **Travel Method Comparison**: Compare emissions across different transportation modes
- **Historical Analysis**: Analyze trends in your travel patterns
- **Visual Breakdown**: Pie charts, line graphs, and bar charts for emissions by category
- **Advanced Filtering**: Filter by date range, activity type, and more

### 🎨 Data Visualization
- Interactive matplotlib and seaborn visualizations
- Statistical charts for trend analysis
- Comparison visualizations across transportation methods
- Custom filtering and date range selection

### 💡 Sustainability Recommendations
- Personalized tips based on your travel patterns
- Suggestions for carbon offset opportunities
- Best practices for sustainable travel

## 🛠️ Tech Stack

- **Python 3.8+** - Core programming language
- **Pandas & NumPy** - Data manipulation and numerical computations
- **Matplotlib & Seaborn** - Data visualization
- **Flask** - Web framework for the dashboard
- **SQLite** - Lightweight database for travel records
- **Jupyter Notebooks** - Interactive analysis and exploration

## 📋 Emission Factors

This project uses scientifically-backed carbon emission factors:

| Category | Emission Factor | Notes |
|----------|-----------------|-------|
| **Flights** | 0.255 kg CO2/km | Economy class average |
| **Hotels** | 15-30 kg CO2/night | Varies by category |
| **Car** | 0.21 kg CO2/km | Average vehicle |
| **Train** | 0.041 kg CO2/km | Low emission transport |
| **Bus** | 0.089 kg CO2/km | Efficient group transport |

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/bhupendraydv/tourist-carbon-footprint.git
cd tourist-carbon-footprint
```

2. **Create a virtual environment**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Run the dashboard**
```bash
python src/app.py
```

The dashboard will be available at `http://localhost:5000`

## 📖 Usage Examples

### Using the Carbon Calculator

```python
from src.carbon_calculator import CarbonCalculator

calc = CarbonCalculator()

# Calculate flight emissions
flight_co2 = calc.calculate_flight(
    distance_km=2000,
    passengers=1,
    class='economy'
)

# Calculate accommodation emissions
hotel_co2 = calc.calculate_accommodation(
    days=5,
    type='standard'
)

# Calculate total footprint
total = calc.calculate_total_footprint(
    flights=[flight_co2],
    accommodation=hotel_co2
)

print(f"Total CO2: {total} kg")
```

### Loading and Analyzing Trip Data

```python
from src.data_processor import DataProcessor

processor = DataProcessor()
trip_data = processor.load_trips('data/trips.csv')

# Get emissions summary
summary = processor.get_emissions_summary(trip_data)
print(summary)

# Export analysis
processor.export_to_csv(summary, 'output/emissions_analysis.csv')
```

## 📁 Project Structure

```
tourist-carbon-footprint/
├── data/
│   ├── sample_trips.csv
│   └── historical_data.csv
├── src/
│   ├── carbon_calculator.py      # Core calculation logic
│   ├── data_processor.py         # Data cleaning and preparation
│   ├── visualizations.py         # Chart and graph generation
│   ├── database.py               # Database operations
│   └── app.py                    # Flask web application
├── notebooks/
│   ├── analysis.ipynb            # Data analysis notebook
│   ├── data_exploration.ipynb    # Exploratory analysis
│   └── visualization_examples.ipynb
├── tests/
│   ├── test_calculator.py
│   └── test_processor.py
├── .github/
│   └── workflows/
│       ├── python-app.yml        # CI/CD pipeline
│       └── code-quality.yml
├── requirements.txt              # Python dependencies
├── README.md
├── LICENSE
└── .gitignore
```

## 🔧 Key Modules

### `carbon_calculator.py`
Core calculation engine with IPCC-based methodology:
- Flight emissions computation
- Accommodation impact calculation
- Transportation mode analysis
- Activity-based emissions

### `data_processor.py`
Data handling and preparation:
- CSV import/export functionality
- Data validation and cleaning
- Time-series data processing
- Aggregation functions

### `visualizations.py`
Visual analytics generation:
- Interactive matplotlib plots
- Statistical visualizations
- Comparative analysis charts

### `database.py`
Data persistence layer:
- SQLite database operations
- CRUD operations for travel records
- Query optimization

### `app.py`
Flask-based web dashboard:
- REST API endpoints
- User interface
- Real-time data updates

## 📊 Analysis Capabilities

The dashboard provides comprehensive insights:

- **Monthly Trends**: Visualize carbon emissions trends over time
- **Mode Comparison**: Compare emissions across different transportation methods
- **Seasonal Patterns**: Identify seasonal travel and emission patterns
- **Impact Statistics**: Comprehensive environmental impact metrics
- **Export Reports**: Generate detailed reports for further analysis

## 🤝 Contributing

Contributions are welcome! To contribute:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

Please ensure your code follows the existing style and includes tests.

## 🚀 Future Enhancements

- [ ] Real-time weather data integration for accuracy
- [ ] AI-powered carbon offset recommendations
- [ ] Integration with travel booking APIs (Amadeus, Google Flights)
- [ ] Multi-user support with authentication
- [ ] Mobile app version for on-the-go tracking
- [ ] Machine learning predictions for trip planning
- [ ] Social features to compare and share footprints
- [ ] Integration with carbon offset platforms

## 📚 References

- [IPCC Guidelines for Carbon Accounting](https://www.ipcc.ch/)
- [Global Sustainable Tourism Council Standards](https://www.gstcouncil.org/)
- [Carbon Trust Methodology](https://www.carbontrust.com/)
- [Our World in Data - Carbon Emissions](https://ourworldindata.org/co2-and-greenhouse-gas-emissions)

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Author

**Bhupendra Yadav**
- GitHub: [@bhupendraydv](https://github.com/bhupendraydv)
- LinkedIn: [linkedin.com/in/bhupendra-yadav](https://linkedin.com/in/bhupendra-yadav-962836380/)

## 💬 Support

If you have any questions or suggestions, feel free to:

- Open an [issue](https://github.com/bhupendraydv/tourist-carbon-footprint/issues)
- Start a [discussion](https://github.com/bhupendraydv/tourist-carbon-footprint/discussions)
- Reach out via email

---

<div align="center">
  <p><strong>🌱 Every sustainable choice counts! Help reduce your carbon footprint today.</strong></p>
  <p>⭐ If this project helped you, please consider giving it a star!</p>
  <p>Last Updated: December 2025</p>
</div>
