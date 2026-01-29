# Setup dev

This guide takes you through setting up your development environment, installing local packages, and configuring regression testing.

## 1. Prerequisites & Subsidies

* **GitHub Copilot Pro**: If you are a student, you can apply for GitHub Education to receive Copilot Pro at no cost.

## 2. Project Structure Setup

For project structure, see:
See https://gitlab.cs.unh.edu/cs518-public/spring-2026/class-demo

Before installing dependencies, ensure your project directory is organized as follows:

* `src/requirements.txt`: List of external dependencies.
* `src/user_service/hello.py`: Your primary service logic.
* `pyproject.toml`: Project configuration file located in the root.
* `tests/test_hello.py`: Unit tests that import `user_service.hello`.
* **Note**: Ensure you include `__init__.py` files in your package and test directories to make them discoverable.

## 3. Installing Dependencies

Run these commands from your terminal to set up your environment:

* **External Requirements**: Navigate to the directory containing `requirements.txt` and run:
`pip install -r requirements.txt`.
*(Note: You may need to use `python -m pip` or `python3 -m pip` depending on your setup.)*

<!-- * **Local Project Installation**: From the **project root**, install your project in editable mode so modules can be imported into your tests:
`pip install -e .`. -->

## 4. Configuring Tests in VS Code

Follow these steps to integrate your tests with the VS Code IDE:

1. **Enable Python Context**: Open any `.py` file.
2. **Open Testing Panel**: Click the **Testing icon** (flask icon) in the left sidebar.
3. **Configure**: Click "Configure Python Tests."
4. **Select Framework**: Choose `unittest`.
5. **Set Directory**: Select your `tests` directory.
6. **Pattern**: Ensure your files follow the `test_*.py` naming convention.

## 5. Running Tests

* **Integrated Testing**: You can run all tests from the Testing panel or click the **play icons** that appear next to individual test functions in your code.
* **Regression Testing**: Use these tools to ensure your `test_hello` and other unit tests pass after any changes.