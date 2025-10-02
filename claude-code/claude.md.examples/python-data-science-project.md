# Project: Customer Analytics Pipeline

## Development Standards
- **Language**: Python 3.11+
- **Code Style**: Follow PEP 8 strictly, use Black for formatting
- **Type Hints**: Required for all function signatures and class definitions
- **Documentation**: Docstrings required for all public functions and classes

## Workflow Requirements
1. Create feature branch: `analysis-[description]` or `model-[description]`
2. Write unit tests for all data processing functions
3. Run `pytest` and ensure all tests pass
4. Run `black .` and `flake8` before committing
5. Update relevant documentation in `/docs` if adding new features

## Project Structure
- `/src/data`: Data ingestion and preprocessing modules
- `/src/models`: ML model definitions and training scripts  
- `/src/analysis`: Exploratory analysis notebooks and scripts
- `/src/utils`: Shared utility functions
- `/tests`: Comprehensive test suite
- `/configs`: Configuration files for different environments

## Data Handling Standards
- Use Pandas for data manipulation, prefer vectorized operations
- All data files must be documented in `/data/README.md`
- Use Pydantic models for data validation and serialization
- Never commit raw data files to version control
- Use environment variables for database connections and API keys

## ML/Analysis Guidelines
- Use scikit-learn for standard ML algorithms
- Notebook naming: `YYYY-MM-DD-[initials]-[description].ipynb`
- Save all trained models with versioning in `/models/trained`
- Use MLflow for experiment tracking
- Include model performance metrics in commit messages

## Dependencies
- Core: pandas, numpy, scikit-learn, matplotlib, seaborn
- ML: xgboost, lightgbm, optuna
- Data: sqlalchemy, pydantic, requests
- Testing: pytest, pytest-cov