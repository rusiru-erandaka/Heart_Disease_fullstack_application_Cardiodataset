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

