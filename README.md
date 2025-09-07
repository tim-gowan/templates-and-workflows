# {{ cookiecutter.project_name }}

{{ cookiecutter.project_description }}

This project was automatically generated from a template using Port.io.

## Getting Started

### Prerequisites

- Python 3.10+
- [uv](https://github.com/astral-sh/uv) - The fast Python package manager used in this project.

### Setup

1.  **Install Dependencies**:
    ```bash
    uv pip install -e ".[dev]"
    ```

## Local Development

This project comes with a set of tools to ensure code quality and consistency.

- **Formatting**: We use `black` for code formatting. To format your code, run:
  ```bash
  black .
  ```
- **Linting**: We use `flake8` to check for code style issues. To run the linter, use:
  ```bash
  flake8 .
  ```
- **Testing**: We use `pytest` for running tests. To run the test suite, use:
  ```bash
  pytest
  ```

## CI/CD Pipeline

This project is configured with a CI/CD pipeline that runs on every push to the `main` branch. The pipeline performs the following checks:

1.  **Linting**: Ensures the code adheres to the style guide.
2.  **Testing**: Runs the test suite to prevent regressions.
3.  **Code Metrics**: Calculates code complexity and test coverage, then sends the report to Port.io.
4.  **Security Scan**: Scans the code for vulnerabilities using Snyk.
