# Contributing to Tourist Carbon Footprint Dashboard

First off, thank you for considering contributing to the Tourist Carbon Footprint Dashboard! It's people like you that make this project such a great tool.

## Code of Conduct

This project and everyone participating in it is governed by our Code of Conduct. By participating, you are expected to uphold this code. Please report unacceptable behavior to the project maintainers.

## How Can I Contribute?

### Reporting Bugs

Before creating bug reports, please check the issue list as you might find out that you don't need to create one. When you are creating a bug report, please include as many details as possible:

* **Use a clear and descriptive title**
* **Describe the exact steps which reproduce the problem**
* **Provide specific examples to demonstrate the steps**
* **Describe the behavior you observed after following the steps**
* **Explain which behavior you expected to see instead**
* **Include screenshots and animated GIFs if possible**
* **Include your Python version and OS details**

### Suggesting Enhancements

Enhancement suggestions are tracked as GitHub issues. When creating an enhancement suggestion, please include:

* **Use a clear and descriptive title**
* **Provide a step-by-step description of the suggested enhancement**
* **Provide specific examples to demonstrate the steps**
* **Describe the current behavior and expected behavior**
* **Explain why this enhancement would be useful**

## Pull Request Process

1. **Fork the repository** and create your branch from `main`
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. **Clone your fork locally**
   ```bash
   git clone https://github.com/your-username/tourist-carbon-footprint.git
   ```

3. **Install development dependencies**
   ```bash
   pip install -r requirements.txt
   pip install pytest pytest-cov flake8 black
   ```

4. **Make your changes** and ensure your code follows the style guidelines:
   ```bash
   # Format code with Black
   black src/ --line-length=100
   
   # Check code with flake8
   flake8 src/
   ```

5. **Add tests** for any new functionality
   ```bash
   # Run tests
   pytest tests/ -v --cov=src
   ```

6. **Commit your changes** with clear, descriptive messages
   ```bash
   git commit -m "Add descriptive message about changes"
   ```

7. **Push to your branch**
   ```bash
   git push origin feature/your-feature-name
   ```

8. **Create a Pull Request** to the main repository with:
   - Clear title and description
   - Reference to related issues using `#issue-number`
   - Screenshots/GIFs if UI changes
   - Test results showing tests pass

## Styleguides

### Python Code Style

* Use [Black](https://black.readthedocs.io/) for code formatting
* Use [flake8](https://flake8.pycqa.org/) for linting
* Follow [PEP 8](https://pep8.org/) conventions
* Maximum line length: 100 characters
* Use meaningful variable and function names
* Write docstrings for all functions and classes

### Git Commit Messages

* Use the present tense ("Add feature" not "Added feature")
* Use the imperative mood ("Move cursor to..." not "Moves cursor to...")
* Limit the first line to 72 characters or less
* Reference issues and pull requests liberally after the first line
* Use emojis to indicate the type of change:
  - ✨ New feature
  - 🐛 Bug fix
  - 📚 Documentation
  - 🎨 Style/formatting
  - ♻️ Refactoring
  - ✅ Tests
  - 🔧 Configuration

Example:
```
✨ Add carbon offset recommendation feature

Adds AI-powered suggestions for carbon offset options based on user's
travel patterns and emission data. Implements new recommendation engine
using historical data analysis.

Fixes #123
```

## Development Setup

### Prerequisites

* Python 3.8 or higher
* Git
* pip

### Setup Local Development Environment

1. Fork and clone the repository
2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   pip install -e .  # Install in development mode
   ```

4. Create a branch for your changes:
   ```bash
   git checkout -b feature/your-feature-name
   ```

### Running Tests

```bash
# Run all tests
pytest tests/ -v

# Run with coverage
pytest tests/ -v --cov=src --cov-report=html

# Run specific test
pytest tests/test_calculator.py::test_flight_emissions -v
```

### Running the Application Locally

```bash
python src/app.py
```

The application will be available at `http://localhost:5000`

## Documentation

* Keep README.md up to date with new features
* Add docstrings to all public functions and classes
* Update CHANGELOG.md with significant changes
* Include examples and usage instructions for new features

## Community

* **Issues**: Use GitHub issues for bugs and feature requests
* **Discussions**: Use GitHub discussions for questions and general topics
* **Pull Requests**: Make sure your PR description is clear

## Recognition

Contributors will be recognized in:
* The README.md file
* Release notes
* GitHub contributors page

## Questions?

Don't hesitate to contact the project maintainers if you have any questions or need clarification.

---

Thank you for contributing! 🌱
