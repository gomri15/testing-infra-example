

# DropIt Testing Framework

## Overview

The **DropIt Testing Framework** is a robust and scalable automation framework designed for UI and API testing. It leverages Playwright for browser automation and APIRequestContext for API testing, enabling comprehensive end-to-end test coverage. The framework is built for maintainability, reusability, and test isolation, making it ideal for dynamic, large-scale applications.

---

## Features

### 1. Modular Page Object Model (POM)
- Implements the POM design pattern for UI automation.
- Separates test logic from UI interactions, improving maintainability.
- Provides reusable components for interacting with pages such as:
  - `LoginPage`
  - `CatalogPage`
  - `CartPage`
  - `CheckoutPage`

### 2. API Testing Capability
- Integrates API testing using Playwright's `APIRequestContext`.
- Includes an `PetsApiClient` for interacting with the Petstore API:
  - Create, update, and validate pets.
  - Find pets by status or other attributes.
  - Validate API responses using Pydantic models for strict type-checking and data validation.

### 3. Configurable Test Setup
- Uses a centralized `Config` class powered by Pydantic for managing configurations:
  - Dynamic URLs for different environments.
  - Credentials and other static data.
- Supports environment-based configurations through JSON files (e.g., `config_dev.json`).
- Easily extendable to add more configurations for future needs.

### 4. Dynamic Browser Context Management
- Automatically resets browser context and state between tests to ensure test isolation.
- Leverages Playwright’s built-in fixtures for managing context and page lifecycle.
- Simplifies test setup with reusable fixtures.

### 5. Test Isolation and Reusability
- Fresh browser contexts and pages for each test.
- Centralized pre-test setup, including:
  - Automatic login.
  - Cart clearance to ensure consistent starting state for tests.

### 6. Logging and Debugging
- Supports logging for debugging and reporting:
  - API request and response details.
  - Test outcomes and critical assertions.
- Integrates Playwright's trace and screenshot capabilities for debugging failed tests.

### 7. Parallel Test Execution
- Leverages Playwright’s parallel execution support for faster test runs.
- Ensures no state leakage between tests.

### 8. Scalable API and UI Integration
- Combines UI and API testing workflows for seamless end-to-end validation.
- Example: Create a pet via API, verify it appears in the UI, and complete an order.

---

## **Prerequisites**

- **Python Version**: `3.11.5`
- Create a Python virtual environment and install the required dependencies.

---

## **Installation**

1. Clone the repository to your local machine:

   ```bash
   git clone <repository_url>
   cd <repository_folder>
   ```

2. Create a Python virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install the dependencies:

   ```bash
   pip install -r requirements.txt
   playwright install
   ```
---

## **Usage**

### **1. UI Testing**

- Run the UI tests using `pytest`:

  ```bash
  pytest -v tests/test_catalog.py
  ```

- **Output**:
  - A test report will be generated in the `reports` folder.
  - A Playwright `debug.zip` file will be available in the `test-results` folder for detailed debugging.
- **Playwright Debugging Documentation**:
  - [Playwright Debug File Handling Documentation](https://playwright.dev/python/docs/trace-viewer-intro)

---

### **2. Backend Api testing**
    
- Run the Backend Api tests using `pytest`:

  ```bash
  pytest -v test_pets.py
  ```

---

## **License**

This project is licensed under the MIT License. See the `LICENSE` file for details.

---

