# 📊 Sales Dashboard — Assignment README

## ✅ Project Overview

This repository contains a **Sales Dashboard built with Streamlit**. The dashboard allows you to upload a CSV/Excel file, filter sales data, visualize key metrics, and generate business insights. The project is designed as a **solo assignment**, meaning you are the only contributor working on it.

The main goals of the project are:

- Perform **EDA (Exploratory Data Analysis)** on sales data
- Build an **interactive Streamlit dashboard** with filters, KPIs, and charts
- Provide **actionable insights** based on sales data
- Deploy the dashboard online and share with HR or stakeholders

---

## 📁 Repository Structure

```
├── app.py                 # Main Streamlit dashboard app
├── requirements.txt       # Python dependencies
├── data/
│   └── sample_sales.csv   # Example dataset for testing
├── notebooks/
│   └── EDA.ipynb          # Exploratory Data Analysis notebook
└── README.md              # Project documentation (this file)
```

---

## 🧾 Dataset Format

Your dataset must include the following columns:

- `Sales Date` — date of transaction (e.g., 2022-06-15)
- `Payment Status` — e.g., `paid`, `Initiated`, `refund`
- `Source` — sales channel (e.g., `website`, `offline`)
- `Currency  Code` — e.g., `INR`
- `Product Amount with GST` — numeric sales amount
- `Product Code` — product identifier
- `Customer ID` — optional, used for top customers

If any column is missing, the app will show a helpful message.

---

## 🛠 Setup Instructions

### Prerequisites

- Python 3.9 or higher
- Git installed

### Installation Steps

1. Clone this repository:
   ```bash
   git clone <your-repo-url>
   cd sales-dashboard
   ```
2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate   # Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

---

## ▶️ How to Run the Dashboard

```bash
streamlit run app.py
```

Open the link shown in the terminal (usually `http://localhost:8501`).

---

## 🔁 Assignment Workflow (Step by Step)

### Step 1 — Data Cleaning & EDA

- Load the dataset
- Convert `Sales Date` to datetime
- Handle missing values
- Generate exploratory plots:
  - Sales over time
  - Sales by Source
  - Payment status distribution
  - Top products
  - (Optional) Top customers

**Output**: Save insights and plots in `notebooks/EDA.ipynb`.

### Step 2 — Build the Streamlit Dashboard

- Add file upload (CSV/Excel)
- Apply sidebar filters (date, status, source, currency)
- Show **KPIs**: total sales, paid orders, refunds, conversion rate, avg order value
- Show **charts**: sales trend, sales by source, payment status pie, heatmap
- Show **top products** (Top 10)
- Show **top customers** (if Customer ID available)
- Show **insights & recommendations**

### Step 3 — UI/UX Improvements

- Use Plotly for interactive charts
- Format numbers with commas & currency symbol (₹)
- Add expanders for detailed stats
- Handle missing columns gracefully

### Step 4 — Deployment

- Push code to GitHub
- Deploy on **Streamlit Community Cloud**
  - Connect GitHub repo
  - Select `app.py` as entrypoint
  - Add `requirements.txt`

### Step 5 — Deliverables

- GitHub repo with:
  - `app.py`
  - `requirements.txt`
  - `sample_sales.csv`
  - `EDA.ipynb`
  - Updated README
---

## 📊 Example Features in Dashboard

- **Key Metrics**: Total Sales, Paid Orders, Refund Orders, Conversion Rate, Avg Order Value
- **Charts**: Sales Trend (line chart), Sales by Source (bar chart), Payment Status Distribution (pie), Sales Heatmap
- **Top Products**: Bar chart of top 10 best-selling products
- **Top Customers**: Table of top 5 customers (if available)
- **Insights Tab**: Business insights auto-generated from data

---

## 👨‍💻 Author

This project is developed and maintained by **Vinothkumar** as part of a Data Science assignment.

- GitHub: [your-username](https://github.com/your-username)
- LinkedIn: [your-linkedin](https://linkedin.com/in/vinothkumar20/)

---

🚀 With this README, you can directly share your GitHub repo + deployed app link with HR and showcase your work professionally.

