E-Commerce Automation Framework -- Playwright
A UI test automation framework for the
SauceDemo application, built with
Python, Playwright, and pytest. The project uses the Page Object
Model (POM), reusable pytest fixtures, external test data, HTML
reporting, logging, failure screenshots, and a Jenkins CI pipeline.
Project Overview
The framework automates key e-commerce user journeys and validates
important application behaviours, including authentication, product
selection, cart operations, checkout, sorting, and application-state
reset.
Technology Stack
- Language: Python
- Browser automation: Playwright (Python, synchronous API)
- Test framework: pytest
- Design pattern: Page Object Model (POM)
- Test data: JSON and CSV
- Environment variables: python-dotenv
- Reporting: pytest-html
- CI/CD: Jenkins Declarative Pipeline
- Version control: Git and GitHub
Automated Test Coverage
The project includes the following test scenarios:
  Test case                           Scenario
  TC-01                               Login using predefined users and
JSON test data

  TC-02                               Login with invalid credentials
using CSV test data

  TC-03                               Validate logout functionality

  TC-04                               Verify shopping-cart icon
visibility

  TC-05                               Select products and extract product
details

  TC-06                               Add selected products to the cart
and validate the cart badge

  TC-07                               Validate product details displayed
in the cart

  TC-08                               Complete the end-to-end checkout
flow and validate payment totals

  TC-09                               Validate product sorting options
TC-10                               Validate Reset App State
functionality
The test suite uses pytest markers where appropriate, including
checkout, smoke, regression, and reset-app categories.
Framework Structure
The project is organised to separate page interactions, tests,
configuration, test data, and supporting utilities.
ECommerce_Automation_Playwright/
│
├── config/
│   └── settings.py
│
├── pages/
│   ├── login_page.py
│   ├── product_page.py
│   ├── cart_page.py
│   └── checkout_page.py
│
├── tests/
│   ├── test_login.py
│   ├── test_product.py
│   ├── test_cart.py
│   └── test_checkout.py
│
├── test_data/
│   ├── [JSON test data files]
│   └── [CSV test data files]
│
├── utils/
│   ├── logger.py
│   ├── json_reader.py
│   └── csv_reader.py
│
├── logs/
├── reports/
│   ├── html/
│   └── screenshots/
│
├── conftest.py
├── pytest.ini
├── requirements.txt
├── Jenkinsfile
└── .gitignore

Design and Implementation
Page Object Model
Page classes encapsulate page-specific locators and user interactions.
Tests call page methods instead of repeatedly implementing UI
interactions, helping keep test logic separate from page implementation.
Pytest Fixtures
Shared fixtures in conftest.py create and provide page objects. The
login fixture performs authentication, and the product, cart, and
checkout page objects use the same underlying Playwright Page for a
test.
Data-Driven Testing
JSON and CSV files keep test inputs separate from test logic. This
supports parameterised scenarios such as valid and invalid login
attempts.
Environment Configuration and Secrets
Sensitive values such as login credentials are read from environment
variables using python-dotenv and load_dotenv().

Create a local .env file for local execution. Do not commit the real
.env file to GitHub.

Example structure (use your own permitted test credentials):
VALID_USERNAME=your_test_username
VALID_PASSWORD=your_test_password
For Jenkins, the .env file is stored as a Jenkins Secret file
credential. The pipeline binds it using withCredentials, copies it
into the project directory for the test run, and removes the temporary
copy in a finally block.
Logging and Failure Screenshots
The framework writes execution messages to its log file and console.
Failure screenshots are captured by the pytest reporting hook and saved
under reports/screenshots/.
Reporting
pytest-html generates a self-contained HTML report at:
reports/html/report.html
The Jenkins pipeline archives reports and logs and publishes the HTML
report using the Jenkins HTML Publisher plugin.
Local Setup and Execution
Prerequisites
- Python installed and available on PATH
- Git
- A supported Playwright browser (Chromium is used by this project)
1. Clone the repository
git clone <your-repository-url>
cd Automation_Projects/ECommerce_Automation_Playwright
2. Create and activate a virtual environment
Windows Command Prompt:
python -m venv .venv
.venv\Scripts\activate
3. Install Python dependencies
python -m pip install --upgrade pip
pip install -r requirements.txt
4. Install the Chromium browser
python -m playwright install chromium
5. Configure environment variables
Create a .env file in the project root and add the required test
credentials. Keep this file out of version control.
6. Run the test suite
python -m pytest
The browser and report options are configured through pytest.ini. The
project is configured to run Chromium in headless mode for CI execution.
Jenkins CI Pipeline
The project has its own Jenkinsfile inside
ECommerce_Automation_Playwright/. The Jenkins job is configured to use
Pipeline script from SCM and points to this Script Path:
ECommerce_Automation_Playwright/Jenkinsfile
Because the GitHub repository is a monorepo, Jenkins checks out the
repository and uses dir('ECommerce_Automation_Playwright') to execute
project-specific commands from the correct directory.
Pipeline stages
1. Checkout -- checks out the configured Git repository using
   checkout scm.
2. Setup Python Environment -- creates the project virtual
   environment if it does not already exist.
3. Install Dependencies -- installs the packages from
   requirements.txt and the Playwright Chromium browser.
4. Prepare Report Directory -- ensures report, screenshot, and log
   directories exist.
5. Run Automation Scripts -- retrieves the Jenkins Secret file
   credential, makes .env available for the test run, executes
   pytest, and removes the temporary .env file.
Post-build actions
The pipeline uses post { always { ... } } so reporting and artifact
handling are attempted whether the test stage succeeds or fails.
- archiveArtifacts archives generated reports and logs with the
  Jenkins build.
- publishHTML publishes the pytest HTML report in the Jenkins
  interface. The Jenkins HTML Publisher plugin is required.
Jenkins prerequisites
- Jenkins running on a Windows agent with Python available.
- Git configured for the Jenkins job.
- Credentials Binding plugin for withCredentials.
- HTML Publisher plugin for publishHTML.
- A Jenkins Secret file credential containing the environment
  variables, referenced in the Jenkinsfile by its credential ID.
The pipeline reuses the workspace virtual environment to reduce repeated
setup time. If the workspace or .venv is removed, the environment must
be recreated and dependencies reinstalled.
Git Hygiene and Sensitive Files
The repository should contain framework source code, tests,
configuration, test data, dependency declarations, and the Jenkinsfile.

Do not commit:
- .env or other files containing secrets
- .venv/ or venv/
- Python cache files such as __pycache__/ and *.pyc
- Generated reports, logs, and temporary execution output
A .gitignore should exclude these generated or sensitive files. Keep
requirements.txt and the Jenkinsfile under version control.


Future Enhancements:
Potential future improvements include-
- Parallel test execution with pytest-xdist, after confirming test
  independence and stability.
- Controlled retries for intermittent failures, while investigating
  and fixing root causes.
- JUnit XML publishing for Jenkins test trend visualisation.
- Allure reporting.
- Further framework architecture and maintainability review.
Project Goal
The goal of this project is to demonstrate a maintainable Python
Playwright automation framework and its integration into a Jenkins CI
workflow, from source-code checkout and environment setup through
automated test execution and report publishing.