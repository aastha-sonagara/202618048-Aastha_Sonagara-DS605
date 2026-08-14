# DS605: Fundamentals of Machine Learning

## Lab Assignment - 2

### Vectorized Programming with NumPy and Data Wrangling with Pandas

**Name:** Aastha Sonagara
**ID:** 202618048
**Course:** DS605 - Fundamentals of Machine Learning
**Lab:** Lab Assignment - 2

---

## 1. About the Project

This project is part of the **DS605: Fundamentals of Machine Learning** course. The main purpose of this lab is to practice basic data manipulation and analysis using **NumPy** and **Pandas**.

The assignment is divided into two major parts:

* **Part A:** Vectorized Programming with NumPy
* **Part B:** Data Wrangling with Pandas using the Titanic dataset

In Part A, I worked with NumPy arrays, statistical calculations, matrix operations, normal distributions, and histograms.

In Part B, I used the Titanic `train.csv` dataset to practice loading and inspecting data, filtering records, grouping and aggregation, handling missing values, detecting outliers, creating new features, making pivot tables, and creating visualizations.

The main focus of this lab was to understand how numerical and tabular data can be processed efficiently using Python libraries instead of writing unnecessary loops.

---

# 2. Objectives

The main objectives of this lab were:

* To understand NumPy arrays and their properties.
* To perform statistical calculations using NumPy.
* To understand vectorized arithmetic operations.
* To perform matrix operations using NumPy.
* To generate data from a normal distribution.
* To create and understand histograms.
* To load and inspect a CSV dataset using Pandas.
* To filter data using Boolean conditions.
* To use `groupby()` and aggregation functions.
* To identify and handle missing values.
* To detect outliers using the IQR method.
* To create new features from existing columns.
* To create and analyze pivot tables.
* To visualize relationships between different variables.
* To extract meaningful observations from the data.

---

# 3. Dataset

For Part B, the **Titanic train.csv dataset** was used.

The dataset contains information about passengers who travelled on the Titanic.

Some of the important columns are:

| Column        | Description                       |
| ------------- | --------------------------------- |
| `PassengerId` | Unique passenger ID               |
| `Survived`    | Survival status: 0 = No, 1 = Yes  |
| `Pclass`      | Passenger class: 1, 2, or 3       |
| `Name`        | Passenger name                    |
| `Sex`         | Passenger gender                  |
| `Age`         | Passenger age                     |
| `SibSp`       | Number of siblings/spouses aboard |
| `Parch`       | Number of parents/children aboard |
| `Ticket`      | Ticket number                     |
| `Fare`        | Passenger fare                    |
| `Cabin`       | Cabin number                      |
| `Embarked`    | Port of embarkation               |

The dataset was loaded using Pandas:

```python
import pandas as pd

df = pd.read_csv("train.csv")
```

---

# 4. Part A - Vectorized Programming with NumPy

## Task 1 - Arrays, Statistics, and Indexing

In the first task, I worked with basic NumPy arrays and statistical operations.

The following activities were performed:

* Generated an array containing 100 random integers.
* Used a random seed so that the results are reproducible.
* Calculated:

  * Minimum
  * Maximum
  * Median
  * Mean
  * Standard deviation
* Created an array of exactly 100 values using `np.arange()`.
* Created arrays using `np.zeros()` and `np.ones()`.
* Checked the shape and data type of arrays.
* Used `np.linspace()` to generate equally spaced values.
* Created 2D and 3D arrays.
* Practiced indexing, row selection, column selection, and slicing.
* Used `reshape()` to change the shape of an array.
* Used `flatten()` to convert a matrix back to a 1D array.

Some of the main NumPy functions used were:

```python
np.random.randint()
np.min()
np.max()
np.median()
np.mean()
np.std()
np.arange()
np.zeros()
np.ones()
np.linspace()
reshape()
flatten()
```

---

## Task 2 - Vectorized Arithmetic and Linear Algebra

In this task, two matrices were created and different matrix operations were performed.

The following operations were implemented:

* Matrix addition
* Element-wise multiplication
* Matrix multiplication
* Transpose
* Determinant
* Matrix inverse
* Verification of the inverse

The `@` operator was used for matrix multiplication.

For example:

```python
A @ B
```

Element-wise multiplication was performed using:

```python
A * B
```

The inverse was verified using:

```python
np.allclose(A @ np.linalg.inv(A), np.eye(2))
```

`np.allclose()` was used because floating-point calculations can sometimes produce very small numerical differences.

No explicit Python loops were used for these operations. NumPy performed the operations directly on the arrays using vectorized operations.

---

## Task 3 - Normal Distribution and Histogram

For this task, 1,000 values were generated from a normal distribution.

The chosen parameters were:

```text
Mean = 50
Standard Deviation = 10
```

The data was generated using:

```python
np.random.normal(50, 10, 1000)
```

The sample mean and sample standard deviation were then calculated.

For the sample standard deviation, `ddof=1` was used:

```python
np.std(data, ddof=1)
```

The calculated sample values were compared with the originally chosen mean and standard deviation.

A histogram was also created to visualize the distribution of the generated data.

---

# 5. Part B - Data Wrangling with Pandas

## Task 4 - Load and Inspect Data

The Titanic dataset was loaded using:

```python
df = pd.read_csv("train.csv")
```

The following Pandas functions and properties were used:

```python
df.head()
df.tail()
df.shape
df.columns
df.info()
df.describe()
```

These were used to understand:

* First and last rows
* Number of rows and columns
* Column names
* Data types
* Missing values
* Statistical summary

I also used both `loc` and `iloc` for selecting specific rows and columns.

### Difference between `loc` and `iloc`

`loc` selects data using labels or column names.

```python
df.loc[0:4, ["Name", "Age"]]
```

`iloc` selects data using integer positions.

```python
df.iloc[0:5, 3:5]
```

A simple way to remember this is:

```text
loc  → labels
iloc → integer positions
```

---

# 6. Task 5 - Filtering and Querying

Boolean indexing was used to answer different questions about the Titanic passengers.

The following conditions were analyzed:

### Male passengers older than 50

The dataset was filtered using:

```python
(df["Sex"] == "male") & (df["Age"] > 50)
```

### Female first-class passengers

The following conditions were used:

```python
(df["Sex"] == "female") & (df["Pclass"] == 1)
```

The survival percentage was calculated using the mean of the `Survived` column.

### Age 20-40, Fare above median, and survived

The overall median Fare was first calculated and then passengers were filtered based on:

* Age between 20 and 40
* Fare above the overall median
* Survived = 1

### Travelling alone, age below 30, and did not survive

A passenger was considered to be travelling alone when:

```text
SibSp = 0
Parch = 0
```

This condition was combined with:

```text
Age < 30
Survived = 0
```

### Southampton passengers in Pclass 2 or 3

The Southampton median Fare was calculated first.

Passengers were then filtered using:

* `Embarked = 'S'`
* `Pclass = 2 or 3`
* Fare above the Southampton median

This task helped me understand how multiple Boolean conditions can be combined to filter a DataFrame.

---

# 7. Task 6 - Groupby and Aggregation

The `groupby()` function was used to calculate different summary statistics.

The following analyses were performed:

### Survival rate by Sex

```python
df.groupby("Sex")["Survived"].mean()
```

### Survival rate by Pclass

```python
df.groupby("Pclass")["Survived"].mean()
```

### Average Age and Fare by Pclass

```python
df.groupby("Pclass")[["Age", "Fare"]].mean()
```

### Passenger count and survival rate by Sex-Pclass

The data was grouped using both:

```python
["Sex", "Pclass"]
```

and aggregation functions were used to calculate:

* Passenger count
* Survival rate

### Passenger count, average Fare, and survival rate by Embarked

The data was grouped by `Embarked` and the following values were calculated:

* Passenger count
* Average Fare
* Survival rate

This task helped in understanding how `groupby()` can be combined with aggregation functions such as `mean()` and `count()`.

---

# 8. Task 7 - Missing Values and Fare Outliers

## Missing Values

The number of missing values in every column was calculated using:

```python
df.isnull().sum()
```

The missing-value percentage was calculated using:

```python
(df.isnull().sum() / len(df)) * 100
```

A bar chart was created to visualize the number of missing values in each column.

## Age Imputation

Missing Age values were filled using the mean Age.

The number of missing Age values was checked both before and after imputation.

Four different imputation approaches were also tried:

1. Mean
2. Median
3. Mode
4. Random value

This helped compare different simple ways of handling missing data.

---

## Fare Outliers

Fare outliers were identified using the IQR method.

The following values were calculated:

```text
Q1
Q3
IQR
Lower Bound
Upper Bound
```

The formula used was:

```text
IQR = Q3 - Q1
```

The outlier limits were calculated as:

```text
Lower Bound = Q1 - 1.5 × IQR

Upper Bound = Q3 + 1.5 × IQR
```

Any Fare value below the lower bound or above the upper bound was considered an outlier.

---

# 9. Task 8 - Features and Pivot Table

Two new features were created from the existing Titanic columns.

## FamilySize

The formula used was:

```text
FamilySize = SibSp + Parch + 1
```

The `+1` represents the passenger themselves.

## IsAlone

A new binary feature was created:

```text
FamilySize = 1 → IsAlone = 1
FamilySize > 1 → IsAlone = 0
```

A pivot table was also created using:

```text
Rows    → Sex
Columns → Pclass
Values  → Mean Survived
```

This was used to compare the survival rate of different Sex and Pclass groups.

The highest and lowest survival groups were then identified from the pivot table.

---

# 10. Task 9 - Visualizations and Observations

Three main visualizations were created.

## Correlation Heatmap

A correlation matrix was calculated for relevant numerical columns including:

* Survived
* Pclass
* Age
* SibSp
* Parch
* Fare

A heatmap was created using Seaborn.

The heatmap helps to understand positive and negative relationships between numerical variables.

The strongest positive relationship was approximately between:

```text
SibSp and Parch ≈ 0.41
```

The strongest negative relationship was approximately between:

```text
Pclass and Fare ≈ -0.55
```

When looking specifically at relationships with `Survived`, `Fare` had a positive correlation of approximately `0.26`, while `Pclass` had a negative correlation of approximately `-0.34`.

---

## Survival Rate by Sex

A bar chart was created to compare survival rates between male and female passengers.

The calculated survival rates were approximately:

```text
Female → 74.20%
Male   → 18.89%
```

This shows a large difference in survival rate between the two groups.

---

## Age vs Fare

A scatter plot was created using:

```text
X-axis → Age
Y-axis → Fare
```

The passengers were separated based on:

```text
Survived = 0
Survived = 1
```

This visualization helped compare the distribution of fares and ages for passengers who survived and those who did not.

---

# 11. Key Observations

Based on the numerical results and visualizations, the following observations were made:

1. **Female passengers had a much higher survival rate than male passengers.** The female survival rate was approximately 74.20%, compared with approximately 18.89% for males.

2. **Passenger class was related to survival.** The correlation between Pclass and Survived was negative, indicating that higher numerical Pclass values were associated with lower survival rates.

3. **Fare had a positive relationship with survival.** Passengers who paid higher fares generally had a higher chance of survival.

4. **SibSp and Parch had the strongest positive relationship among the selected family-related variables**, with a correlation of approximately 0.41.

5. **Pclass and Fare had a relatively strong negative relationship**, with a correlation of approximately -0.55.

6. **The Age vs Fare plot shows a wide range of fares across different passenger ages.** The survived and non-survived groups were distributed differently across the plot.

7. **The Titanic dataset contains missing values**, particularly in columns such as Age and Cabin, so missing-value handling is an important part of the preprocessing process.

---

# 12. Libraries Used

The main Python libraries used in this project were:

### NumPy

Used for:

* Arrays
* Statistics
* Random number generation
* Matrix operations
* Normal distribution

```python
import numpy as np
```

### Pandas

Used for:

* Loading the Titanic CSV
* Data inspection
* Filtering
* Grouping
* Aggregation
* Missing-value handling
* Feature creation
* Pivot tables

```python
import pandas as pd
```

### Matplotlib

Used for:

* Histograms
* Bar charts
* Other visualizations

```python
import matplotlib.pyplot as plt
```

### Seaborn

Used mainly for:

* Correlation heatmap
* Scatter plot

```python
import seaborn as sns
```

---

# 13. Project Structure

The repository can be organized as follows:

```text
DS605-Lab-2/
│
├── README.md
│
├── Lab2_NumPy_Pandas.ipynb
│
├── train.csv
│
├── figures/
│   ├── normal_distribution_histogram.png
│   ├── missing_values.png
│   ├── correlation_heatmap.png
│   ├── survival_by_sex.png
│   └── age_vs_fare.png
│
└── cleaned_titanic.csv
```

The exact filenames can be changed depending on how the notebook and generated files are saved.

---

# 14. How to Run the Project

### Step 1: Clone the repository

```bash
git clone <your-github-repository-link>
```

### Step 2: Open the project folder

Open the folder in VS Code or Jupyter Notebook.

### Step 3: Install the required libraries

```bash
pip install numpy pandas matplotlib seaborn
```

### Step 4: Open the notebook

Open:

```text
Lab2_NumPy_Pandas.ipynb
```

### Step 5: Make sure the dataset is available

Keep:

```text
train.csv
```

in the appropriate project directory.

### Step 6: Run the notebook

Run the cells from beginning to end.

---

# 15. Conclusion

This lab helped me understand the basic use of **NumPy and Pandas for data analysis and preprocessing**.

In Part A, I learned how to work with arrays, perform statistical calculations, use vectorized operations, perform matrix calculations, generate random data, and visualize a normal distribution.

In Part B, I worked with the Titanic dataset and practiced different data-wrangling techniques such as filtering, grouping, aggregation, missing-value handling, outlier detection, feature engineering, and pivot tables.

The visualizations also helped me understand the relationships between different variables and identify patterns in passenger survival.

Overall, this assignment gave me practical experience with the basic tools and techniques that are commonly used at the beginning of a machine learning and data analysis workflow.

---

## Author

**Aastha Sonagara**
**ID:** 202618048
**DS605 - Fundamentals of Machine Learning**
