# Sales Analysis & Data Visualization

This project consists of an automated Python script to perform Exploratory Data Analysis (EDA) on a retail dataset (`Superstore Sales`). The goal is to transform raw Excel data into visual reports and key metrics to support decision-making.

## 🚀 Features

The `pipeline.py` script automatically performs the following tasks:

1.  **Data Ingestion:** Loads data directly from an Excel file (`.xlsx`), automatically handling date formats and encoding.
2.  **ETL Processing:** Cleans data, parses timestamp columns, and sorts records chronologically.
3.  **Data Visualization:** Generates three key insights saved as PNG images:
    * 📈 **Sales Trend:** Line chart with monthly aggregation (resampling) to visualize growth over time.
    * 📊 **Category Performance:** Bar chart ranked by revenue to identify top-performing categories.
    * 🍰 **Market Share:** Pie chart showing the percentage distribution of sales.
4.  **Executive Summary:** Calculates and prints key metrics (Total Revenue, Top Category, Best Month) to the console.

## 🛠️ Requirements

To run this project, you need **Python 3.x** and the following libraries:

* **Pandas:** For data manipulation and analysis.
* **Matplotlib:** For creating static visualizations.
* **Openpyxl:** Engine required to read Excel (`.xlsx`) files.

### Installation

Run the following command in your terminal to install the dependencies:

```bash
pip install pandas matplotlib openpyxl
