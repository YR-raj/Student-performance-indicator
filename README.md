# Student Performance in Exams – Model Training Report

## 📊 Dataset
- **Source:** [Kaggle – Students Performance in Exams](https://www.kaggle.com/datasets/spscientist/students-performance-in-exams?datasetId=74977)  
- **Description:**  
  This dataset records the performance of students in math, reading, and writing exams, along with demographic and social factors such as gender, race/ethnicity, parental education level, lunch type, and test preparation course.  
- **Goal:**  
  To analyze what variables affect students' exam performance.

---

## 🧪 Models and Results

### Linear Regression
**Training Set:**
- RMSE: **5.3274**
- MAE: **4.2788**
- R²: **0.8741**

**Test Set:**
- RMSE: **5.4096**
- MAE: **4.2259**
- R²: **0.8797**

---

### Lasso Regression
**Training Set:**
- RMSE: **6.5938**
- MAE: **5.2063**
- R²: **0.8071**

**Test Set:**
- RMSE: **6.5197**
- MAE: **5.1579**
- R²: **0.8253**

---

## 📈 Model Choice
Among all tested regression models, the best-performing model was **Ridge Regression**.  
The **second-best model was Linear Regression (R² = 0.8797)**, which gave consistent and interpretable results.  
👉 I chose to proceed with **Linear Regression** for further analysis and conclusions.

---

## ✅ Insights
- Student performance is **influenced by lunch type, race/ethnicity, and parental education level**.  
- **Females** have higher pass percentages and also score better on average.  
- Performance is **not strongly linked** to taking a test preparation course.  
- However, **completing** the preparation course shows some **positive effect** on scores.  

---

## 📌 Notes
- Models were evaluated using RMSE, MAE, and R² metrics.  
- Further improvements may involve feature engineering, advanced regularization, or ensemble methods.
