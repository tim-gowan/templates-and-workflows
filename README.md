# Project Template

This is a template for creating new Python projects.

## Getting Started

To use this template, follow these steps:

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/tim-gowan/templates-and-workflows.git your-project-name
    cd your-project-name
    ```
2.  **Update `pyproject.toml`:**
    Open `pyproject.toml` and replace the placeholder values for `name`, `description`, and `authors` with your project's information.
3.  **Rename the package directory:**
    Rename the `src/your_project_name` directory to match the `name` you set in `pyproject.toml`.
4.  **Install dependencies:**
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
  **Note:** The CI pipeline will skip this step if no tests are found.

## CI/CD Pipeline

This project is configured with a CI/CD pipeline that runs on every push to the `main` branch. The pipeline performs the following checks:

1.  **Linting**: Ensures the code adheres to the style guide.
2.  **Testing**: Runs the test suite to prevent regressions.
3.  **Code Metrics**: Calculates code complexity and test coverage.
4.  **Security Scan**: Scans the code for vulnerabilities using Snyk.
