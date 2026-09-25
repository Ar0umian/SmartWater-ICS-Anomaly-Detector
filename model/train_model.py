import pandas as pd
from sklearn.ensemble import IsolationForest
import pickle
import os

def train_anomaly_detector():
    print("[*] Starting model training process...")
    
    # 1. قراءة بيانات الحساسات التاريخية
    data_path = os.path.join(os.path.dirname(__file__), '../data/sensor_data.csv')
    if not os.path.exists(data_path):
        raise FileNotFoundError(f"Dataset not found at {data_path}")
    
    df = pd.read_csv(data_path)
    print(f"[+] Loaded {len(df)} records from sensor_data.csv")
    
    # 2. إعداد وتدريب نموذج Isolation Forest
    # نحدد نسبة الشذوذ المتوقعة contamination بنسبة قليلة جداً
    model = IsolationForest(contamination=0.1, random_state=42)
    model.fit(df[['pressure', 'flow_rate']])
    
    # 3. حفظ النموذج المدرب
    model_output_path = os.path.join(os.path.dirname(__file__), 'isolation_forest.pkl')
    with open(model_output_path, 'wb') as file:
        pickle.dump(model, file)
        
    print(f"[+] Model successfully trained and saved to: {model_output_path}")

if __name__ == '__main__':
    train_anomaly_detector()