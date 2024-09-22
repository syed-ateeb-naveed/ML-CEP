# Car Price Prediction

## Overview

Car Price Prediction is a machine learning project aimed at estimating the price of used cars based on various features like brand, model, year, kilometers driven, etc. The application utilizes multiple machine learning models to provide accurate predictions and is built with a user-friendly interface using **Streamlit**. The project is deployed as a web-based application, allowing users to input car details and receive price estimates.

## Features

- **Real-time Predictions**: Users can input car features and get instant price estimates.
- **Multiple ML Models**: Linear Regression, Decision Tree, and Random Forest models are used for predictions.
- **Streamlit Interface**: A simple and intuitive UI for user interaction and predictions.

### Python Libraries Used:

- **Data Processing**: `numpy`, `pandas`
- **Visualization**: `matplotlib`, `seaborn`
- **Machine Learning**: `scikit-learn`
- **Web App**: `streamlit`, `streamlit-option-menu`

## Development Steps

1. **Data Collection**:
   - The dataset was scraped from **Quikr**, containing used car prices and related features.

2. **Data Preprocessing**:
   - Cleaning: Removed missing or incorrect values.
   - Encoding: Converted categorical variables to numeric using **One Hot Encoder** and **Label Encoder**.

3. **Exploratory Data Analysis (EDA)**:
   - Used histograms, box plots, and scatter plots to visualize the relationships between features and the target variable (price).

4. **Feature Engineering**:
   - Applied scaling to features like `kms_driven` and `year` using the **MinMaxScaler**.

5. **Model Building**:
   - **Linear Regression**: Best for linear relationships.
   - **Decision Tree**: Handles non-linear relationships.
   - **Random Forest**: An ensemble method that improves prediction accuracy.

6. **Model Training**:
   - Used **grid search** and **cross-validation** to optimize hyperparameters for the Decision Tree and Random Forest models.
   - Trained the models using both **scikit-learn** packages and custom implementations without packages.

7. **Model Evaluation**:
   - Evaluated the models based on **R² score**, **Mean Squared Error (MSE)**, **Root Mean Squared Error (RMSE)**, and **Mean Absolute Error (MAE)**.
   - **Linear Regression** performed the best, with an R² score of **91.65%**.

8. **Integration**:
   - Integrated the **Linear Regression** model into a **Streamlit** web application to allow real-time predictions.

## Model Performance

| Model                         | R² Score (%) |
|-------------------------------|--------------|
| Linear Regression (with package) | 91.65        |
| Linear Regression (without package) | 57.88    |
| Random Forest (with package)   | 80.71        |
| Random Forest (without package)| 50.59        |
| Decision Tree (with package)   | 38.69        |
| Decision Tree (without package)| 31.62        |

## Setup Instructions

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/syed-ateeb-naveed/ML-CEP.git
   cd ML-CEP
   ```

2. **Install Required Dependencies**:
   Install the necessary libraries using `pip`:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Streamlit App**:
   Start the Streamlit app to launch the user interface:
   ```bash
   streamlit run app.py
   ```

4. **Access the Web App**:
   Open your browser and go to:
   ```
   http://localhost:8501
   ```

## Conclusion

The Car Price Prediction system successfully leverages machine learning techniques to estimate car prices. Among the various models evaluated, **Linear Regression** was found to provide the highest accuracy. Despite inherent prediction errors due to the scale of car prices, the system provides an effective tool for estimating car values.

## Screenshot

![image](https://github.com/user-attachments/assets/9bb27ac3-da26-4988-9ca5-7661706efa03)
