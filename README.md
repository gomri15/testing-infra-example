
# **DropIt Home Task**

## **Description**

The DropIt Home Task project is designed to perform two primary functions:

1. **UI Testing**: Automates UI testing using Playwright
2. **Backend Api testing**: Using pet store api and playwright api model

---

## **Features**

- **UI Testing**:
  - Tests the user interface and generates detailed reports.
  - Includes Playwright debugging capabilities.
- **Backend Api testing**: 
  - Using pet store api and playwright api model
  - Model api response using pydantic for easy of use and auto complete functionality


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

