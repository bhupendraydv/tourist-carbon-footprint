"""Data Processing Module

Handles data cleaning, validation, and preparation for the carbon footprint dashboard.
"""

import pandas as pd
import numpy as np
from datetime import datetime
from typing import List, Dict, Optional


class DataProcessor:
    """Process and clean tourism data for analysis."""
    
    def __init__(self):
        self.trips_data = None
        self.processed_data = None
    
    def load_csv(self, filepath: str) -> pd.DataFrame:
        """Load trip data from CSV file."""
        self.trips_data = pd.read_csv(filepath)
        return self.trips_data
    
    def validate_data(self) -> bool:
        """Validate data integrity."""
        required_columns = ['date', 'activity_type', 'value', 'unit']
        if self.trips_data is None:
            return False
        return all(col in self.trips_data.columns for col in required_columns)
    
    def clean_data(self) -> pd.DataFrame:
        """Clean and prepare data for analysis."""
        df = self.trips_data.copy()
        df['date'] = pd.to_datetime(df['date'])
        df = df.dropna(subset=['value'])
        df['value'] = pd.to_numeric(df['value'], errors='coerce')
        self.processed_data = df
        return df
    
    def aggregate_by_period(self, period: str = 'M') -> pd.DataFrame:
        """Aggregate emissions by time period."""
        if self.processed_data is None:
            return None
        
        df = self.processed_data.copy()
        df.set_index('date', inplace=True)
        return df.resample(period)['emissions_kg'].sum()
    
    def get_activity_summary(self) -> pd.DataFrame:
        """Get summary statistics by activity type."""
        if self.processed_data is None:
            return None
        
        return self.processed_data.groupby('activity_type')['emissions_kg'].agg([
            'sum', 'mean', 'count'
        ]).round(2)
    
    def get_top_activities(self, n: int = 5) -> pd.DataFrame:
        """Get top n activities by emissions."""
        if self.processed_data is None:
            return None
        
        return self.processed_data.nlargest(n, 'emissions_kg')[[
            'date', 'activity_type', 'emissions_kg'
        ]]
    
    def export_to_csv(self, filepath: str):
        """Export processed data to CSV."""
        if self.processed_data is None:
            return False
        self.processed_data.to_csv(filepath, index=False)
        return True
