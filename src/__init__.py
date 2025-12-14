"""Tourist Carbon Footprint Dashboard Package"""

from .carbon_calculator import CarbonCalculator, CarbonEmissionFactors
from .data_processor import DataProcessor

__version__ = '1.0.0'
__author__ = 'Bhupendra Yadav'

__all__ = ['CarbonCalculator', 'CarbonEmissionFactors', 'DataProcessor']
