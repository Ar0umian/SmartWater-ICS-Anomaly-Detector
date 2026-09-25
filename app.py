from flask import Flask, jsonify, render_template, Response
import pickle
import os
from datetime import datetime
from pymodbus.client import ModbusTcpClient
import csv
import io

app = Flask(__name__)

MODEL_PATH = os.path.join(os.path.dirname(__file__), 'model/isolation_forest.pkl')
if os.path.exists(MODEL_PATH):
    with open(MODEL_PATH, 'rb') as f:
        model = pickle.load(f)
else:
    model = None

MODBUS_SERVER_IP = "127.0.0.1"
MODBUS_SERVER_PORT = 5020

# قائمة لحفظ السجل الكامل في ذاكرة السيرفر منذ لحظة التشغيل
server_full_history = []

def read_from_modbus_server():
    try:
        client = ModbusTcpClient(MODBUS_SERVER_IP, port=MODBUS_SERVER_PORT)
        connection = client.connect()
        if not connection:
            return 45.0, 120.0, 0, False
            
        result = client.read_holding_registers(0, 3, slave=1)
        if result.isError():
            result = client.read_holding_registers(0, 3, slave=0)
            
        client.close()
        
        if result and not result.isError():
            regs = result.registers
            pressure = regs[0] / 10.0
            flow_rate = regs[1] / 10.0
            plc_status_flag = regs[2]
            return pressure, flow_rate, plc_status_flag, True
    except Exception as e:
        print(f"[!] Modbus Connection Error: {e}")
        
    return 45.0, 120.0, 0, False

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/stream')
def api_stream():
    pressure, flow_rate, plc_status_flag, plc_connected = read_from_modbus_server()
    
    if plc_status_flag == 1:
        status = "ALERT"
        message = "⚠️ تنبيه أمني خطير: تم رصد انحراف أو هجوم تم حقنه في مسجلات الـ PLC!"
    else:
        status = "SAFE"
        message = "✅ قراءات الحساسات الصناعية مستقرة وآمنة ضمن الحدود التشغيلية."
    
    current_time = datetime.now().strftime("%H:%M:%S")

    # حفظ القراءة الجديدة في السجل الكامل للسيرفر
    new_record = {
        'timestamp': current_time,
        'pressure': pressure,
        'flow_rate': flow_rate,
        'status': status
    }
    server_full_history.append(new_record)
        
    return jsonify({
        "timestamp": current_time,
        "pressure": pressure,
        "flow_rate": flow_rate,
        "plc_connected": plc_connected,
        "status": status,
        "message": message
    })

# المسار الصحيح لإرجاع البيانات للرسم الهندسي الشامل بصيغة JSON
@app.route('/api/full-telemetry-history')
def full_telemetry_history():
    return jsonify(server_full_history)

if __name__ == '__main__':
    print("[*] Starting Professional SCADA Dashboard on http://127.0.0.1:5000")
    app.run(debug=True, port=5000)