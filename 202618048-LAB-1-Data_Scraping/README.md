# DS605 – Fundamentals of Machine Learning
## Lab 1 – Web Data Scraping, Preprocessing, Visualization and Analysis

### Student Information

- **Name:** Aastha Sonagara
- **Student ID:** 202618048
- **Course:** DS605 – Fundamentals of Machine Learning
- **Lab:** Lab 1 – Data Scraping

---

# Project Overview

The objective of this project is to collect book-related data from the **Books to Scrape** website using the Scrapy framework. The collected data is then preprocessed, analyzed, visualized, and interpreted to identify meaningful insights.

The project demonstrates the complete machine learning data preparation pipeline, including web scraping, data cleaning, feature engineering, exploratory data analysis, visualization, and interpretation.

---

# Website Used

**Books to Scrape**

https://books.toscrape.com/

---

# Objectives

- Scrape book information using Scrapy.
- Collect at least 100 books.
- Clean and preprocess the scraped dataset.
- Perform feature engineering.
- Generate meaningful visualizations.
- Create a Word Cloud using book descriptions.
- Analyze the dataset and extract useful insights.

---

# Data Collected

The following information was extracted for every book:

- Title
- Category
- Price
- Rating
- Availability
- Available Stock
- Product Description
- UPC
- Number of Reviews
- Product URL

---

# Data Preprocessing

The preprocessing steps include:

- Loading the scraped dataset
- Handling missing values
- Removing duplicate records
- Converting price to numeric format
- Mapping ratings (One–Five) to integer values
- Extracting available stock count
- Checking data types
- Saving the cleaned dataset

---

# Feature Engineering

The following new features were created:

- **description_word_count** – Number of words in the product description.
- **price_band** – Categorizes books into Budget, Economy, Premium, and Luxury groups.
- **affordability_score** – Indicates how affordable a book is based on its price.
- **value_score** – Combines rating and affordability to identify better-value books.
- **recommended** – Indicates whether a book is recommended based on its rating and price.

---

# Visualizations

The following visualizations were generated:

1. Price Distribution
2. Rating Distribution
3. Number of Books by Category
4. Average Price by Category
5. Price vs Rating
6. Genre-wise Price Distribution
7. Word Cloud of Book Descriptions

---

# Project Structure

```
202618048-LAB-1-Data_Scraping
│
├── data
│   ├── books.csv
│   └── books_cleaned.csv
│
├── notebook
│   ├── Task2_Preprocessing.ipynb
│   ├── Task_3_Visualization_Analysis.ipynb
│   └── Task_4_Insights_Interpretation.ipynb
│
├── plots
│   ├── distribution of books prices.png
│   ├── distribution of book ratings.png
│   ├── number of books i each category.png
│   ├── avg price by category.png
│   ├── price vs rating.png
│   ├── genere wise price distribution.png
│   └── word cloud.png
│
├── scrapy_project
│   └── bookscraper
│
└── README.md
```

---

# Technologies Used

- Python
- Scrapy
- Pandas
- NumPy
- Matplotlib
- WordCloud
- Jupyter Notebook
- Git
- GitHub

---

# Key Findings

- Most books fall within the medium price range.
- Book ratings are fairly balanced across all five rating levels.
- Sequential Art is the most represented category in the dataset.
- Historical Fiction has one of the highest average prices.
- No strong relationship was observed between book price and rating.
- Word Cloud analysis highlights common themes such as life, story, love, family, and world.

---

# Repository Contents

This repository includes:

- Complete Scrapy source code
- Raw dataset
- Cleaned dataset
- Data preprocessing notebook
- Visualization notebook
- Generated plots
- Word Cloud
- Insights and interpretation

---

# Author

**Aastha Sonagara**

**Student ID:** 202618048
