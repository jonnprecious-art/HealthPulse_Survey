# HealthPulse Survey — Income & Spending Analysis

A full-stack web application built to collect and analyze participant income and spending data in preparation for a new product launch in the healthcare industry.

## Live Application

🌐 **URL:** `healthcare-survey-env.eba-dxhpumwp.us-east-1.elasticbeanstalk.com`

## Project Structure

```
HealthPulse_Survey/
├── application.py          # Flask web application + User class
├── requirements.txt        # Python dependencies
├── Procfile                # Gunicorn entry point for AWS
├── README.md               # Project documentation
├── templates/
│   └── index.html          # Survey form webpage
├── charts/
│   ├── chart1_income_by_age.png
│   ├── chart2_gender_spending.png
│   ├── chart3_healthcare_vs_income.png
│   └── chart4_expense_share.png
├── survey_results.csv      # Exported participant data
└── HealthPulse_Analysis.ipynb  # Jupyter notebook with visualizations
```
## Technologies Used

| Technology | Purpose |
|------------|---------|
| Python 3.11 | Backend programming language |
| Flask | Web framework for survey form |
| MongoDB Atlas | Cloud database for storing responses |
| PyMongo | Python driver for MongoDB |
| Pandas | Data processing and CSV export |
| Matplotlib | Data visualization and charts |
| AWS Elastic Beanstalk | Cloud hosting and deployment |
| Google Colab | Jupyter notebook environment |
| Gunicorn | Production WSGI server |

## Features

- **Survey Form** — Collects Age, Gender, Total Income, and Expenses across 5 categories:
  - Utilities
  - Entertainment
  - School Fees
  - Shopping
  - Healthcare
- **MongoDB Storage** — All responses saved to MongoDB Atlas cloud database
- **Python User Class** — Processes collected data into structured format
- **CSV Export** — Visit `/export` to generate a CSV file from all responses
- **Data Visualizations** — 4 charts generated from real survey data
- **AWS Deployment** — Live on Amazon Web Services Elastic Beanstalk

## API Endpoints

| Method | Route | Description |
|--------|-------|-------------|
| GET | `/` | Survey form |
| POST | `/submit` | Save response to MongoDB |
| GET | `/export` | Export all data as CSV |
| GET | `/debug` | Check MongoDB connection status |

## Data Schema (MongoDB)

```json
{
  "age": 34,
  "gender": "Female",
  "income": 80000,
  "expenses": {
    "utilities": 10000,
    "entertainment": 5000,
    "school_fees": 20000,
    "shopping": 13000,
    "healthcare": 15000
  }
}
```
## Setup Instructions (Local)

### Prerequisites
- Python 3.11+
- MongoDB Atlas account (or local MongoDB)
- Google Colab or Jupyter Notebook

### 1. Clone or unzip the project
```bash
cd HealthPulse_Survey
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Set environment variables
```bash
export MONGO_URI="mongodb+srv://username:password@cluster.mongodb.net/healthcare_survey"
export SECRET_KEY="your-secret-key"
```

### 4. Run the Flask app
```bash
python application.py
# Visit http://localhost:5000
```

### 5. Export data to CSV
```
Visit http://localhost:5000/export
```

### 6. Open Jupyter Notebook
Open `HealthPulse_Analysis.ipynb` in Google Colab or Jupyter and run all cells to generate charts.

## AWS Deployment Instructions

### Prerequisites
- AWS account
- AWS CLI: `pip install awscli`
- EB CLI: `pip install awsebcli`
- MongoDB Atlas URI

### Steps

```bash
# 1. Configure AWS credentials
aws configure

# 2. Initialize Elastic Beanstalk
eb init -p python-3.11 healthcare-survey --region us-east-1

# 3. Create environment
eb create healthcare-survey-env

# 4. Set environment variables
eb setenv MONGO_URI="your-mongodb-atlas-uri" SECRET_KEY="your-secret-key"

# 5. Deploy
eb deploy

# 6. Open live app
eb open
```

## Data Visualizations

| Chart | Description |
|-------|-------------|
| Chart 1 | Average monthly income by age group — highlights the age group with highest income |
| Chart 2 | Average spending per category broken down by gender |
| Chart 3 | Scatter plot of healthcare spend vs total income with trend line |
| Chart 4 | Pie chart showing total spending distribution across all categories |

All charts are exported as PNG files and embedded in the Zipped project file
## MongoDB Atlas Setup

1. Create a free account at [cloud.mongodb.com](https://cloud.mongodb.com)
2. Create a new cluster
3. Go to **Database Access** → create a database user
4. Go to **Network Access** → Add IP `0.0.0.0/0` to allow all connections
5. Get your connection URI from **Connect** → **Drivers**

## Python User Class

The `User` class in `application.py` handles data processing:

```python
class User:
    def __init__(self, age, gender, income, expenses):
        self.age = age
        self.gender = gender
        self.income = income
        self.expenses = expenses
```

Data is looped through and stored in CSV format for analysis.

## Submission

- **Live URL:** `healthcare-survey-env.eba-dxhpumwp.us-east-1.elasticbeanstalk.com`
- **GitHub/ZIP:** Contains all source code, notebook, charts, and this README
- **Presentation:** PowerPoint with all 4 charts embedded

## Author

**Donald Precious**
Data Analysis — Healthcare Product Launch Research
Washington, DC
