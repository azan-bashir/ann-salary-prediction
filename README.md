# Salary Prediction using Artificial Neural Network

A regression project that predicts an employee's estimated salary using an Artificial Neural Network (ANN) built with TensorFlow/Keras, deployed as an interactive Streamlit web application.

---

## 📌 Project Overview

This project predicts an employee's `EstimatedSalary` based on available input features using a deep learning model.

The original project was designed as a **classification** problem. It has been converted into a **regression** problem, where the model now predicts a continuous numerical value instead of a discrete class label.

---

## 🎯 Problem Type

**Regression**

- **Target Variable:** `EstimatedSalary`
- Since salary is a continuous numerical value, this task is treated as a regression problem rather than classification.

---

## 🧠 Model Architecture

An Artificial Neural Network was developed using TensorFlow/Keras with the following architecture:

| Layer | Units | Activation |
|---|---|---|
| Hidden Layer 1 | 64 | ReLU |
| Hidden Layer 2 | 32 | ReLU |
| Output Layer | 1 | Linear |

- **Optimizer:** Adam
- **Loss Function:** Mean Squared Error (MSE)

> The output layer uses a **linear activation function** since the model needs to predict a continuous salary value rather than a probability or class label.

---

## 📊 Evaluation Metrics

The model is evaluated using the following regression metrics:

| Metric | Description |
|---|---|
| **MAE** (Mean Absolute Error) | Average absolute difference between actual and predicted salary |
| **RMSE** (Root Mean Squared Error) | Prediction error that penalizes larger errors more heavily |
| **R² Score** | Proportion of variance in the target variable explained by the model |

*(Add your final model's actual MAE, RMSE, and R² values here once training is complete.)*

---

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Scikit-learn
- TensorFlow / Keras
- Streamlit

---

## 📁 Project Files

```text
salary_regression.py
salary_model.keras
salary_prediction.ipynb
requirements.txt
README.md
app_screenshots.png
```

| File | Description |
|---|---|
| `salary_regression.py` | Streamlit application for salary prediction |
| `salary_model.keras` | Trained ANN regression model |
| `salary_prediction.ipynb` | Complete notebook with data preprocessing, model training, and evaluation |
| `requirements.txt` | Required Python libraries |
| `README.md` | Project documentation |
| `app_screenshots.png` | Screenshots of the Streamlit application |

---

## 🚀 Streamlit Application

**Live App:** _[Add your Streamlit URL here after deployment]_

**App Screenshot:**

![App Screenshot](<img width="1365" height="588" alt="app_ss png" src="https://github.com/user-attachments/assets/b0871822-37ca-4e07-ae12-0fa39b24084f" />
)

---

## 🔄 Classification vs Regression

The original model was a **classification** model that predicted a class using a sigmoid output and classification metrics (e.g., accuracy, precision, recall).

This project was converted into a **regression** problem because `EstimatedSalary` is a continuous numerical target rather than a category. To support this change:

- The output layer was changed to **1 neuron with linear activation**
- Classification metrics were replaced with **regression metrics** — MAE, RMSE, and R²

---

## ⚙️ How to Run

**1. Install the required libraries:**

```bash
pip install -r requirements.txt
```

**2. Run the Streamlit application:**

```bash
streamlit run salary_regression.py
```

---

## 🔮 Future Improvements

- Hyperparameter tuning (layers, units, learning rate)
- Cross-validation for more robust performance estimates
- Feature engineering to improve prediction accuracy
- Deployment on a cloud platform (e.g., Streamlit Cloud, Hugging Face Spaces)

---

## 👤 Author

**Azan**
BS Software Engineering
University of Karachi
