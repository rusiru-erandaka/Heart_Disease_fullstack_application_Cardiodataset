# 🫀 Cardio Risk Prediction Using Feedforward Neural Network (FFNN)

This project demonstrates the development and training of a Feedforward Neural Network (FFNN) for predicting cardiovascular risk using a structured tabular dataset. The model is built using Keras and trained with various machine learning best practices including dropout regularization, custom callbacks, and model checkpointing.

## 📁 Project Structure

```
flask-back/
├── Training_the_FFNN_for_Cardio_dataset.ipynb  # Main model training notebook
├── models/
│   ├── model-XXX.keras                         # Checkpointed models saved during training
│   ├── scaler_data.sav                         # Saved input scaler
│   └── scaler_target.sav                       # Saved target scaler
├── templates/                                  # HTML templates for Flask UI
│   ├── index.html
│   ├── result.html
│   └── details.html
└── main.py                                     # Flask backend to serve predictions
```

---

## 📊 Dataset Overview

- **Inputs**: 7 features selected from the cardio dataset  
- **Target**: A continuous value representing cardiovascular health risk (scaled between 0 and 1)

The dataset is preprocessed using `MinMaxScaler` from Scikit-learn for both input features and the target variable.

---

## 🧠 Model Architecture

The FFNN is designed with the following architecture:


```python
model = Sequential()
model.add(Dense(128, input_dim=7, activation='sigmoid', kernel_initializer='normal'))
model.add(Dropout(0.5))
model.add(Dense(64, activation='sigmoid'))
model.add(Dropout(0.5))
model.add(Dense(10, activation='sigmoid'))
model.add(Dense(1, activation='linear'))
```

### 🔒 Why Use Dropout Layers?

Dropout is a regularization technique used to prevent overfitting. In this project, we apply a dropout rate of 0.5 after the first and second hidden layers. This helps ensure the model generalizes well by randomly deactivating 50% of the neurons during training, encouraging the network to learn more robust features.

---

## 🔁 Training Configuration

- **Optimizer**: Adam  
- **Loss Function**: Mean Squared Error (MSE)  
- **Metrics**: MSE and MAE  
- **Epochs**: 200  
- **Validation Split**: 20%

```python
model.compile(optimizer='adam', loss='mse', metrics=['mse', 'mae'])
```

---

## 🔔 CustomCallback Function

A custom Keras callback is implemented to calculate and log the R² score at the end of each training epoch:

```python
class CustomCallback(keras.callbacks.Callback):
    def on_epoch_end(self, epoch, logs=None):
        predicted_result = model.predict(test_data)
        r2 = r2_score(test_target, predicted_result)
        print('Epoch', epoch, '- R² score:', r2)
```

