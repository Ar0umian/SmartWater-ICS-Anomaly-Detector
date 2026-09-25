# 📂 Project Directory Structure (SmartWater-ICS)

This document outlines the architectural organization of the **SmartWater-ICS** repository, separating data ingestion, machine learning models, simulation environments (mock and industrial protocols), and the core web application.

```text
SmartWater-ICS-Anomaly-Detector/
│
├── data/
│   └── sensor_data.csv            # Historical dataset used for training the anomaly detection model
│
├── model/
│   ├── train_model.py             # Python script for training the Isolation Forest ML model
│   └── isolation_forest.pkl       # Serialized trained model file (generated after training)
│
├── simulator/
│   ├── mock_generator.py          # Fast mock data generator for rapid web UI testing
│   └── modbus_server.py           # Industrial OT/ICS simulation server (PLC / Modbus protocol)
│
├── templates/
│   └── index.html                 # System Display Interface
│
├── app.py                         # Main Flask application and dashboard API endpoints
├── requirements.txt               # Project dependencies (Flask, scikit-learn, pymodbus, pandas, numpy)
├── DIRECTORY.md                   # Repository architectural tree documentation
└── README.md                      # Comprehensive project overview and deployment guide