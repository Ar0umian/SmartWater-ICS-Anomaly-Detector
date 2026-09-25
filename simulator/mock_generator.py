import random

def generate_sensor_reading(inject_anomaly=False):
    """
    توليد قراءات حساسات المياه.
    إذا كان inject_anomaly صحيحاً، يتم توليد قيم متطرفة (شاذة) تحاكي تلاعباً أو هجوماً على الحساس.
    """
    if inject_anomaly:
        # قيم شاذة (ضغط عالي جداً أو منخفض بطريقة خطرة، أو تدفق متوقف)
        pressure = round(random.choice([15.0, 85.5, 90.0]), 2)
        flow_rate = round(random.choice([30.0, 210.0, 5.0]), 2)
    else:
        # قيم طبيعية وآمنة ضمن النطاق المعتاد
        pressure = round(random.uniform(44.5, 46.5), 2)
        flow_rate = round(random.uniform(119.0, 122.0), 2)
        
    return {"pressure": pressure, "flow_rate": flow_rate}

if __name__ == "__main__":
    # اختبار سريع للمولد
    print("Normal Reading:", generate_sensor_reading(inject_anomaly=False))
    print("Anomalous Reading:", generate_sensor_reading(inject_anomaly=True))