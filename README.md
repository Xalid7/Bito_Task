🚀 How to Run Tests (Playwright + Pytest)
1️⃣ Create virtual environment
python3 -m venv .venv

2️⃣ Activate the virtual environment
Linux / MacOS:
source .venv/bin/activate

Windows (PowerShell):
.\venv\Scripts\activate

3️⃣ Install all project dependencies
pip install -r requirements.txt

4️⃣ Install Playwright browsers
playwright install

5️⃣ Run ALL tests
pytest -v

6️⃣ Run a specific test file
pytest tests/login_page/test_login_invalid.py -v

7️⃣ Run a single test inside a file
pytest tests/login_page/test_login_invalid.py::test_invalid_phone_number_format -v

8️⃣ Run tests in headed mode (browser visible)
pytest --headed -v

9️⃣ Run tests with Allure reporting
Generate Allure results:
pytest --alluredir=allure-results

Show report:
allure serve allure-results

🔟 Clean previous test cache
pytest --cache-clear

