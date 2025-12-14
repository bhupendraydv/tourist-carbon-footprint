"""Carbon Calculator Module

This module contains the core calculation logic for computing carbon emissions
from various tourism-related activities.
"""

import pandas as pd
import numpy as np
from typing import Dict, List, Tuple


class CarbonEmissionFactors:
    """Emission factors for different modes of transportation and activities."""
    
    # Flight emissions (kg CO2 per km)
    FLIGHT_ECONOMY = 0.255
    FLIGHT_BUSINESS = 0.680
    FLIGHT_FIRST = 1.215
    
    # Hotel emissions (kg CO2 per night)
    HOTEL_BUDGET = 15.5
    HOTEL_STANDARD = 22.8
    HOTEL_LUXURY = 35.2
    
    # Transportation emissions (kg CO2 per km)
    CAR_AVERAGE = 0.210
    TRAIN = 0.041
    BUS = 0.089
    TAXI = 0.250
    
    # Activities (kg CO2 per activity per day)
    ACTIVITY_HIGH_IMPACT = 12.5  # Skiing, water sports
    ACTIVITY_MEDIUM_IMPACT = 6.2  # Hiking, sightseeing
    ACTIVITY_LOW_IMPACT = 2.1  # Museum visits, local tours


class CarbonCalculator:
    """Main class for calculating carbon footprint from tourism activities."""
    
    def __init__(self):
        self.emissions_data = []
        self.total_emissions = 0.0
    
    def calculate_flight_emissions(self, distance_km: float, 
                                   passengers: int = 1, 
                                   flight_class: str = 'economy') -> float:
        """Calculate CO2 emissions from flight.
        
        Args:
            distance_km: Distance of flight in kilometers
            passengers: Number of passengers
            flight_class: Class of flight ('economy', 'business', 'first')
        
        Returns:
            Total CO2 emissions in kg
        """
        class_factor = {
            'economy': CarbonEmissionFactors.FLIGHT_ECONOMY,
            'business': CarbonEmissionFactors.FLIGHT_BUSINESS,
            'first': CarbonEmissionFactors.FLIGHT_FIRST
        }
        
        factor = class_factor.get(flight_class.lower(), 
                                 CarbonEmissionFactors.FLIGHT_ECONOMY)
        emissions = distance_km * passengers * factor
        
        self.emissions_data.append({
            'activity': 'Flight',
            'value': distance_km,
            'unit': 'km',
            'emissions_kg': emissions
        })
        
        return emissions
    
    def calculate_hotel_emissions(self, nights: int, 
                                 hotel_type: str = 'standard') -> float:
        """Calculate CO2 emissions from hotel stay.
        
        Args:
            nights: Number of nights
            hotel_type: Type of hotel ('budget', 'standard', 'luxury')
        
        Returns:
            Total CO2 emissions in kg
        """
        type_factor = {
            'budget': CarbonEmissionFactors.HOTEL_BUDGET,
            'standard': CarbonEmissionFactors.HOTEL_STANDARD,
            'luxury': CarbonEmissionFactors.HOTEL_LUXURY
        }
        
        factor = type_factor.get(hotel_type.lower(), 
                                CarbonEmissionFactors.HOTEL_STANDARD)
        emissions = nights * factor
        
        self.emissions_data.append({
            'activity': 'Accommodation',
            'value': nights,
            'unit': 'nights',
            'emissions_kg': emissions
        })
        
        return emissions
    
    def calculate_transport_emissions(self, distance_km: float, 
                                     mode: str = 'car') -> float:
        """Calculate CO2 emissions from ground transportation.
        
        Args:
            distance_km: Distance traveled in kilometers
            mode: Transportation mode ('car', 'train', 'bus', 'taxi')
        
        Returns:
            Total CO2 emissions in kg
        """
        mode_factor = {
            'car': CarbonEmissionFactors.CAR_AVERAGE,
            'train': CarbonEmissionFactors.TRAIN,
            'bus': CarbonEmissionFactors.BUS,
            'taxi': CarbonEmissionFactors.TAXI
        }
        
        factor = mode_factor.get(mode.lower(), 
                                CarbonEmissionFactors.CAR_AVERAGE)
        emissions = distance_km * factor
        
        self.emissions_data.append({
            'activity': f'Transport ({mode})',
            'value': distance_km,
            'unit': 'km',
            'emissions_kg': emissions
        })
        
        return emissions
    
    def calculate_activity_emissions(self, num_days: int, 
                                    activity_type: str = 'medium') -> float:
        """Calculate CO2 emissions from activities.
        
        Args:
            num_days: Number of days of activity
            activity_type: Type of activity ('low', 'medium', 'high')
        
        Returns:
            Total CO2 emissions in kg
        """
        type_factor = {
            'low': CarbonEmissionFactors.ACTIVITY_LOW_IMPACT,
            'medium': CarbonEmissionFactors.ACTIVITY_MEDIUM_IMPACT,
            'high': CarbonEmissionFactors.ACTIVITY_HIGH_IMPACT
        }
        
        factor = type_factor.get(activity_type.lower(), 
                                CarbonEmissionFactors.ACTIVITY_MEDIUM_IMPACT)
        emissions = num_days * factor
        
        self.emissions_data.append({
            'activity': f'Activity ({activity_type})',
            'value': num_days,
            'unit': 'days',
            'emissions_kg': emissions
        })
        
        return emissions
    
    def get_total_emissions(self) -> float:
        """Get total emissions calculated so far.
        
        Returns:
            Total CO2 emissions in kg
        """
        return sum([item['emissions_kg'] for item in self.emissions_data])
    
    def get_emissions_breakdown(self) -> pd.DataFrame:
        """Get detailed breakdown of emissions by activity.
        
        Returns:
            DataFrame with emissions breakdown
        """
        if not self.emissions_data:
            return pd.DataFrame()
        
        df = pd.DataFrame(self.emissions_data)
        return df.sort_values('emissions_kg', ascending=False)
    
    def reset(self):
        """Reset the calculator for a new trip."""
        self.emissions_data = []
        self.total_emissions = 0.0
    
    def get_carbon_offset_trees(self) -> int:
        """Calculate number of trees needed to offset emissions.
        
        Returns:
            Number of trees (assuming 1 tree offsets ~25 kg CO2/year)
        """
        total = self.get_total_emissions()
        return int(np.ceil(total / 25))
    
    def get_comparison_to_average(self) -> Dict[str, float]:
        """Compare trip emissions to average tourist footprint.
        
        Returns:
            Dictionary with comparison metrics
        """
        total = self.get_total_emissions()
        avg_trip = 2500  # kg CO2 for average trip
        
        return {
            'your_footprint_kg': total,
            'average_trip_kg': avg_trip,
            'difference_kg': total - avg_trip,
            'percentage_of_average': (total / avg_trip) * 100
        }
