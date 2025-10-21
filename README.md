# 🌍 NEO Project - Near Earth Objects Analysis

A comprehensive Python application that demonstrates advanced **Object-Oriented Programming (OOP)** concepts through the analysis of Near-Earth Objects (NEOs) data from NASA's Jet Propulsion Laboratory (JPL).

## 🎯 Project Overview

This project showcases professional Python development practices by implementing a command-line tool that inspects and queries datasets of NEOs and their close approaches to Earth. The application demonstrates mastery of OOP principles, design patterns, and modern Python development techniques.

### ✨ Key Features

- **🔍 Inspect Mode**: Detailed analysis of individual NEOs by designation or name
- **🔎 Query Mode**: Advanced filtering and searching capabilities with multiple criteria
- **📊 Data Export**: Export results to CSV or JSON formats with streaming support
- **🎮 Interactive Mode**: Command-line interface for real-time exploration
- **⚡ Performance Optimized**: Handles large datasets efficiently with streaming JSON output
- **🛡️ Robust Validation**: Comprehensive CLI argument validation with detailed error handling

## 🏗️ Project Architecture

### Core Modules

| Module | Purpose | Key Concepts |
|--------|---------|--------------|
| **`models.py`** | Domain entities and data models | Classes, encapsulation, properties |
| **`extract.py`** | Data loading and parsing | File I/O, error handling |
| **`database.py`** | Data persistence and queries | Collections, lookup operations |
| **`filters.py`** | Advanced filtering system | Strategy pattern, polymorphism |
| **`write.py`** | Data serialization and export | Streaming I/O, format handling |
| **`validation.py`** | CLI argument validation | Input validation, error handling |
| **`main.py`** | Command-line interface | Argument parsing, subcommands |
| **`helpers.py`** | Utility functions | Helper methods, constants |

### Design Patterns Implemented

- **🎨 Strategy Pattern**: Interchangeable filtering algorithms
- **🏭 Factory Pattern**: Dynamic filter creation based on criteria
- **📋 Template Method**: Common structure across filter classes
- **🔄 Iterator Pattern**: Efficient data processing with generators

## 📁 Project Structure

```
neo-project/
├── 📂 data/                    # Dataset files
│   ├── neos.csv               # NEOs dataset (23,967 objects)
│   └── cad.json               # Close approaches dataset (406,785 records)
├── 📂 docs/                    # Comprehensive documentation
│   ├── EXECUTIVE_SUMMARY.md   # High-level project overview
│   ├── CODE_REVIEW.md         # Technical analysis and architecture
│   └── EXERCISES.md           # Learning exercises and challenges
├── 📂 tests/                   # Complete test suite
│   ├── test_database.py       # Database functionality tests
│   ├── test_extract.py        # Data extraction tests
│   ├── test_filters.py        # Filtering system tests
│   ├── test_write.py          # Output functionality tests
│   └── test_query.py         # Query system tests
├── 📄 pyproject.toml          # Project configuration and dependencies
├── 📄 main.py                 # Application entry point
├── 📄 models.py               # Core data models
├── 📄 database.py             # Data management layer
├── 📄 extract.py              # Data loading utilities
├── 📄 filters.py              # Advanced filtering system
├── 📄 write.py                # Data export functionality
├── 📄 validation.py           # CLI validation system
└── 📄 helpers.py              # Utility functions
```

## 🚀 Getting Started

### Prerequisites

- **Python 3.13+** (modern type hints and features)
- **uv** package manager (recommended) or pip

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/FabioCLima/neo-project.git
   cd neo-project
   ```

2. **Set up the environment**
   ```bash
   # Using uv (recommended)
   uv sync
   
   # Or using pip
   pip install -e .
   ```

3. **Verify installation**
   ```bash
   # Run the complete test suite
   uv run python -m pytest tests/ -v
   
   # Check code quality
   uv run ruff check .
   uv run pylint *.py
   uv run pydocstyle *.py
   ```

## 💻 Usage Examples

### Inspect Individual NEOs

```bash
# Inspect by designation
python main.py inspect --pdes 433

# Inspect by name with verbose output
python main.py inspect --name "Halley" --verbose

# Get detailed information about a specific NEO
python main.py inspect --pdes 99942 --verbose
```

### Query Close Approaches

```bash
# Find approaches on a specific date
python main.py query --date 2020-01-01 --limit 5

# Find hazardous approaches within 0.1 AU
python main.py query --hazardous --max-distance 0.1

# Complex query with multiple filters
python main.py query \
  --start-date 2020-01-01 \
  --end-date 2020-12-31 \
  --min-distance 0.01 \
  --max-distance 0.1 \
  --hazardous \
  --limit 10
```

### Export Results

```bash
# Export to CSV
python main.py query --date 2020-01-01 --outfile results.csv

# Export to JSON (with streaming for large datasets)
python main.py query --hazardous --outfile results.json

# Export with custom filters
python main.py query \
  --min-velocity 20 \
  --max-velocity 50 \
  --outfile filtered_results.json
```

### Interactive Mode

```bash
# Launch interactive exploration
python main.py interactive
```

## 🧪 Testing

The project includes a comprehensive test suite with **73 tests** covering all functionality:

```bash
# Run all tests
uv run python -m pytest tests/ -v

# Run with coverage
uv run python -m pytest tests/ --cov=. --cov-report=html

# Run specific test modules
uv run python -m pytest tests/test_database.py -v
uv run python -m pytest tests/test_filters.py -v
```

## 🔧 Code Quality

The project maintains high code quality standards with multiple linting tools:

```bash
# Code formatting and linting
uv run ruff check .          # Fast linting
uv run ruff format .         # Code formatting
uv run pylint *.py           # Comprehensive analysis
uv run pydocstyle *.py       # Docstring compliance (PEP 257)
```

### Quality Metrics

- ✅ **73/73 tests passing** (100% success rate)
- ✅ **0 linting warnings** (ruff, pylint, pydocstyle)
- ✅ **PEP 257 compliant** docstrings throughout
- ✅ **Modern Python 3.13+** type hints
- ✅ **Comprehensive error handling**

## 📊 Dataset Information

The project processes real NASA data:

- **📈 NEOs Dataset**: 23,967 near-Earth objects
- **📈 Close Approaches**: 406,785 close approach records
- **📅 Date Range**: Historical and future predictions
- **🌍 Data Source**: NASA/JPL Center for Near-Earth Object Studies

## 🎓 Educational Value

### For Python Beginners
- **OOP Fundamentals**: Classes, objects, inheritance, polymorphism
- **Encapsulation**: Private data and public interfaces
- **Best Practices**: Clean code, documentation, testing

### For Intermediate Developers
- **Design Patterns**: Strategy, Factory, Template Method, Iterator
- **Software Architecture**: Modular design, separation of concerns
- **Performance**: Streaming I/O, memory efficiency

### For Advanced Developers
- **Modern Python**: Type hints, f-strings, context managers
- **Error Handling**: Comprehensive exception management
- **Testing**: Unit tests, integration tests, edge cases

## 🔮 Advanced Features

### Streaming JSON Output
For large datasets, the application uses streaming JSON output to handle memory efficiently:

```python
# Automatically switches to streaming for large results
if args.limit > 1000:
    write_to_json_streaming(results, args.outfile)
else:
    write_to_json(results, args.outfile)
```

### Robust CLI Validation
Comprehensive argument validation with detailed error messages:

```python
# Validates date ranges, distance ranges, velocity ranges, etc.
validate_query_arguments(args)
validate_file_path(neofile, must_exist=True)
```

## 📚 Documentation

- **📋 [Executive Summary](docs/EXECUTIVE_SUMMARY.md)**: High-level project overview
- **🔍 [Code Review](docs/CODE_REVIEW.md)**: Detailed technical analysis
- **📝 [Exercises](docs/EXERCISES.md)**: Learning challenges and extensions

## 🤝 Contributing

This project serves as an educational example of professional Python development. Feel free to:

- Study the code architecture and design patterns
- Run the tests to understand functionality
- Experiment with different queries and filters
- Extend functionality as learning exercises

## 📄 License

This project is developed for educational purposes as part of Udacity's Intermediate Python course.

## 🏆 Project Achievements

- **✅ Complete OOP Implementation**: All major OOP concepts demonstrated
- **✅ Design Patterns**: Multiple patterns correctly implemented
- **✅ Professional Quality**: Production-ready code standards
- **✅ Comprehensive Testing**: Full test coverage with edge cases
- **✅ Modern Python**: Latest language features and best practices
- **✅ Documentation**: Complete and professional documentation

---

*This project represents a comprehensive example of professional Python development, showcasing advanced OOP concepts, design patterns, and modern development practices suitable for educational and reference purposes.*