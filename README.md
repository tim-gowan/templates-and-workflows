# Project Template

This is a template for creating new Python projects using a self-service action in Port.

-----

## Prerequisites

Before the CI/CD pipeline can run, you must configure the following secrets in your new repository's settings under **Settings \> Secrets and variables \> Actions**:

  * **`PORT_CLIENT_ID`**: Your Port Client ID.
  * **`PORT_CLIENT_SECRET`**: Your Port Client Secret.
  * **`SNYK_TOKEN`**: Your Snyk API token for security scanning.

The scaffolding action also requires a **`PAT_TOKEN`** to be configured in the template repository's secrets.

-----

## Getting Started

To create a new project from this template, do not clone this repository directly. Instead, follow these steps:

1.  **Navigate to the Port UI:**
    Go to [https://app.port.io/self-serve](https://app.port.io/self-serve).
2.  **Run the Scaffolding Action:**
    Find and run the **"Scaffold Python UV Project"** action.
3.  **Provide a Repository Name:**
    Enter a name for your new repository when prompted.
4.  **Access Your New Repository:**
    Once the action is complete, your new repository will be created and ready to use.

-----

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

-----

## CI/CD Pipeline

This project is configured with a CI/CD pipeline that runs on every push to the `main` branch. The pipeline performs the following checks:

1.  **Linting**: Ensures the code adheres to the style guide.
2.  **Testing**: Runs the test suite to prevent regressions.
3.  **Code Metrics**: Calculates code complexity and test coverage.
4.  **Security Scan**: Scans the code for vulnerabilities using Snyk.
