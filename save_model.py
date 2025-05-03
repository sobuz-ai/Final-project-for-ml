import joblib
from data_prep import model

# Save the model
joblib.dump(model, 'model.joblib')
print('Model saved successfully!') 