# DS605 – Fundamentals of Machine Learning

## Lab 3 – Scikit-learn: Data Preprocessing and Model Performance Evaluation

---

## Student Details

| Detail | Information |
|---|---|
| **Name** | Aastha Sonagara |
| **Student ID** | 202618048 |
| **Course** | DS605 – Fundamentals of Machine Learning |
| **Lab** | Lab 3 |
| **Topic** | Scikit-learn: Data Preprocessing and Model Performance Evaluation |

---

# 1. Lab Objective

The objective of this lab is to use **Scikit-learn** to perform data preprocessing and evaluate machine learning classification models on the **Hotel Booking Demand dataset**.

The lab focuses on understanding how different preprocessing techniques affect machine learning model performance.

Two preprocessing pipelines are created using different numerical scaling methods:

- **Pipeline A:** KNN Imputation + StandardScaler
- **Pipeline B:** KNN Imputation + MinMaxScaler

Two classification models are then trained using both pipelines:

- **Logistic Regression**
- **Decision Tree Classifier**

The complete lab workflow includes:

- Loading and understanding the dataset.
- Identifying the target variable and input features.
- Handling missing values.
- Identifying and preventing data leakage.
- Checking and handling clear/extreme outliers.
- Creating Scikit-learn preprocessing pipelines.
- Training classification models.
- Evaluating model performance.
- Comparing four model-pipeline combinations.
- Plotting confusion matrices.
- Checking possible overfitting.
- Drawing final observations from the results.

---

# 2. Dataset

The dataset used in this lab is the **Hotel Booking Demand Dataset**.

The dataset contains information about hotel bookings, including booking details, guest information, arrival information, room information, and booking status.

# Task 1 – Load and Understand the Dataset

The first task is to load the `hotel_bookings.csv` dataset and understand its basic structure before performing any preprocessing or model training.

The following operations are performed:

- Load the dataset.
- Display the first few rows using `head()`.
- Check the number of rows and columns using `shape`.
- Inspect the dataset structure using `info()`.
- Generate statistical information using `describe()`.
- Check the data type of every column using `dtypes`.
- Check the class distribution of the target variable `is_canceled`.
- Use `is_canceled` as the target variable `y`.
- Create `X` using the remaining usable features.
- Identify numerical and categorical columns.

The purpose of this task is to understand the dataset and identify the types of features that will require different preprocessing methods.


# Task 2 – Missing Values, Leakage, and Outliers

The second task focuses on identifying and handling important data-quality issues before model training.

## Missing Values

For every column, the following are checked:

- Total number of missing values.
- Percentage of missing values.

Columns with very high missingness are identified.

A column is dropped only when there is a valid reason for removing it.

In this dataset, the `company` column has very high missingness and is removed because it provides limited useful information for the modelling process.

## Data Leakage

Columns that directly reveal the final booking outcome must be removed.

The following columns are removed:

- `reservation_status`
- `reservation_status_date`

These columns contain information related to the final booking outcome and could allow the model to indirectly know the target value.

Removing them prevents data leakage.

## Outliers

Selected numerical features are checked for outliers using:

- Boxplots.
- The IQR (Interquartile Range) method.

# Task 3 – Create Two Preprocessing Pipelines

The third task is to create two different preprocessing pipelines using **Scikit-learn**.

The same train-test split must be used for all experiments so that the models can be compared fairly.

## Train-Test Split

The dataset is split using:

```python
train_test_split(
    X,
    y,
    test_size=0.2,
    stratify=y,
    random_state=42
)


# Task 4 – Train Two Classification Models

The fourth task focuses on training two classification models using the two preprocessing pipelines created in Task 3.

The two classification models used are:

- **Logistic Regression**
- **Decision Tree Classifier**

Each model is trained using both preprocessing pipelines so that four model-pipeline combinations are obtained in total.

---

## 4.1 Logistic Regression

The first classification model used is **Logistic Regression**.

The model is created using:

```python
LogisticRegression(max_iter=1000)

# Task 5 – Evaluate and Compare the Four Results

The fifth task focuses on evaluating the performance of all four trained model-pipeline combinations created in Task 4.

For each experiment, the following evaluation metrics are calculated:

- Training Accuracy
- Testing Accuracy
- Precision
- Recall
- F1-score

The results are then combined into one final comparison table. Confusion matrices are also created for the best Logistic Regression result and the best Decision Tree result.

Finally, the training and testing performance are compared to identify possible overfitting.

---

## 5.1 Training Accuracy

Training accuracy measures how accurately the model predicts the observations that were used to train the model.

It helps us understand how well the model fits the training data.

A high training accuracy means that the model is performing well on the data it has already seen.

However, training accuracy alone is not enough to determine whether the model will perform well on new, unseen data.

---

## 5.2 Testing Accuracy

Testing accuracy measures how accurately the trained model predicts the observations in the unseen test dataset.

It is important because it gives an indication of how well the model generalizes to new data.

The testing accuracy is compared with the training accuracy to check whether the model may be overfitting.

---

## 5.3 Precision

Precision measures how correct the model's positive predictions are.

In this project, the positive class is:

```text
is_canceled = 1

# Task 6 – Final Observations

The sixth and final task focuses on interpreting the results obtained from the four model-pipeline experiments.

The observations are based on the **final performance comparison table** and the **confusion matrices** created in Task 5.

---

## 6.1 Best Overall Preprocessing-Model Combination

The four model-pipeline combinations are compared:

- Logistic Regression + Pipeline A
- Logistic Regression + Pipeline B
- Decision Tree + Pipeline A
- Decision Tree + Pipeline B

The best overall combination is identified by comparing the evaluation metrics, especially:

- Testing Accuracy
- Precision
- Recall
- F1-score

The combination with the strongest overall testing performance is considered the best-performing model-pipeline combination.

The conclusion should be supported by the actual values in the final comparison table.

---

## 6.2 Effect of StandardScaler and MinMaxScaler on Logistic Regression

The two Logistic Regression experiments are compared:

```text
Logistic Regression + Pipeline A
        ↓
StandardScaler

Logistic Regression + Pipeline B
        ↓
MinMaxScaler



