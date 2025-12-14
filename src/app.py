"""Flask Web Application for Carbon Footprint Dashboard"""

from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import json
from .carbon_calculator import CarbonCalculator
from .data_processor import DataProcessor

app = Flask(__name__)
CORS(app)

calculator = CarbonCalculator()
processor = DataProcessor()


@app.route('/', methods=['GET'])
def index():
    """Serve the main dashboard page."""
    return jsonify({'message': 'Tourist Carbon Footprint Dashboard API'})


@app.route('/api/calculate-flight', methods=['POST'])
def calculate_flight():
    """Calculate emissions from a flight."""
    try:
        data = request.get_json()
        distance = float(data.get('distance_km', 0))
        passengers = int(data.get('passengers', 1))
        flight_class = data.get('class', 'economy')
        
        emissions = calculator.calculate_flight_emissions(
            distance, passengers, flight_class
        )
        
        return jsonify({
            'success': True,
            'emissions_kg': emissions,
            'distance_km': distance,
            'class': flight_class
        })
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 400


@app.route('/api/calculate-hotel', methods=['POST'])
def calculate_hotel():
    """Calculate emissions from hotel stay."""
    try:
        data = request.get_json()
        nights = int(data.get('nights', 1))
        hotel_type = data.get('type', 'standard')
        
        emissions = calculator.calculate_hotel_emissions(nights, hotel_type)
        
        return jsonify({
            'success': True,
            'emissions_kg': emissions,
            'nights': nights,
            'type': hotel_type
        })
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 400


@app.route('/api/summary', methods=['GET'])
def get_summary():
    """Get summary of total emissions."""
    total = calculator.get_total_emissions()
    breakdown = calculator.get_emissions_breakdown()
    trees_needed = calculator.get_carbon_offset_trees()
    comparison = calculator.get_comparison_to_average()
    
    return jsonify({
        'total_emissions_kg': total,
        'trees_needed': trees_needed,
        'comparison': comparison
    })


@app.route('/api/reset', methods=['POST'])
def reset():
    """Reset the calculator."""
    calculator.reset()
    return jsonify({'success': True, 'message': 'Calculator reset'})


@app.errorhandler(404)
def not_found(error):
    """Handle 404 errors."""
    return jsonify({'error': 'Endpoint not found'}), 404


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
