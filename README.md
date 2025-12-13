## 🚀 How to Run Tests (Playwright + Pytest)

### 1️⃣ Create virtual environment
```bash
python3 -m venv .venv
```

### 2️⃣ Activate the virtual environment

#### Linux / MacOS:
```bash
source .venv/bin/activate
```

#### Windows (PowerShell):
```powershell
.\venv\Scripts\activate
```

### 3️⃣ Install all project dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Install Playwright browsers
```bash
playwright install
```

### 5️⃣ Run ALL tests
```bash
pytest -v
```

### 6️⃣ Run a specific test file
```bash
pytest tests/login_page/test_login_invalid.py -v
```

### 7️⃣ Run a single test inside a file
```bash
pytest tests/login_page/test_login_invalid.py::test_invalid_phone_number_format -v
```

### 8️⃣ Run tests in headed mode (browser visible)
```bash
pytest --headed -v
```

### 9️⃣ Run tests with Allure reporting

#### Generate Allure results:
```bash
pytest --alluredir=allure-results
```

#### Show report:
```bash
allure serve allure-results
```

### 🔟 Clean previous test cache
```bash
pytest --cache-clear
```

