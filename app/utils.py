import pandas as pd




def parse_input_json(data: dict):
# Expecting keys matching training features (example):
# 'gender','age','hypertension','heart_disease','ever_married','work_type','Residence_type','avg_glucose_level','bmi','smoking_status'
df = pd.DataFrame([data])
return df