# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- Comprehensive project documentation with professional README
- GitHub Actions CI/CD workflow for automated testing and linting
- Contributing guidelines with development setup instructions
- Support for multiple Python versions (3.8, 3.9, 3.10, 3.11)
- Code coverage reporting with Codecov integration
- Emission factors table for flights, hotels, cars, trains, and buses
- Project structure documentation
- Comprehensive usage examples
- Key modules documentation

### Changed
- Enhanced README with emoji formatting and better organization
- Improved project structure documentation
- Updated feature descriptions with more details

### Fixed
- Code quality checks with flake8
- Code formatting with Black

## [0.1.0] - 2025-12-14

### Added
- Initial project release
- Carbon calculation engine with IPCC methodology
  - Flight emissions calculation based on distance and class
  - Hotel accommodation emission tracking
  - Ground transportation emissions (car, train, bus)
  - Activity-based emissions tracking
- Interactive Flask dashboard for carbon footprint tracking
- Real-time carbon footprint visualization
- Comparative analysis across transportation methods
- Historical data analysis capabilities
- Data visualization with matplotlib and seaborn
  - Pie charts for emissions distribution
  - Line graphs for trend analysis
  - Bar charts for transportation comparison
- SQLite database for travel records storage
- CSV import/export functionality
- Sample trip data for testing and analysis
- Project structure with modular design
  - `carbon_calculator.py` - Core calculation logic
  - `data_processor.py` - Data handling and preparation
  - `visualizations.py` - Chart generation
  - `database.py` - Database operations
  - `app.py` - Flask web application
- MIT License
- .gitignore configuration for Python projects

---

## Guide for this Changelog

### Types of Changes

- **Added** for new features.
- **Changed** for changes in existing functionality.
- **Deprecated** for soon-to-be removed features.
- **Removed** for now removed features.
- **Fixed** for any bug fixes.
- **Security** in case of vulnerabilities.

### How to Update

Keep an `Unreleased` section at the top for tracking ongoing work.
When releasing a new version:

1. Change the `Unreleased` heading to the version number
2. Add the release date
3. Add a new `Unreleased` section for future changes
4. Update links at the bottom

### Example Version Format

`[1.2.0] - 2024-12-25`

---

## Future Releases

Planned enhancements for upcoming versions:

- Real-time weather data integration
- AI-powered carbon offset recommendations
- Integration with travel booking APIs
- Multi-user support with authentication
- Mobile app version
- Advanced ML predictions for trip planning
- Social sharing features
- Integration with carbon offset platforms

---

**Last Updated:** December 2025
