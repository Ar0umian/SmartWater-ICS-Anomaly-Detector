import asyncio
import random
from pymodbus.server import StartAsyncTcpServer
from pymodbus.datastore import ModbusSequentialDataBlock, ModbusSlaveContext, ModbusServerContext

# تهيئة مخزن البيانات للـ Modbus باستخدام ModbusSlaveContext (الإصدار الحديث)
store = ModbusSlaveContext(
    di=ModbusSequentialDataBlock(0, [100]*100),
    co=ModbusSequentialDataBlock(0, [100]*100),
    hr=ModbusSequentialDataBlock(0, [452, 1205, 1]), # [الضغط * 10, التدفق * 10, حالة الشذوذ]
    ir=ModbusSequentialDataBlock(0, [100]*100)
)
context = ModbusServerContext(slaves=store, single=True)

async def update_sensor_registers():
    """تحديث قراءات الحساسات في خادم الـ Modbus بشكل دوري لمحاكاة بيئة تشغيلية حقيقية"""
    while True:
        # توليد قيم طبيعية أو شاذة عشوائياً
        is_anomaly = random.random() < 0.2 # 20% فرصة حدوث شذوذ
        if is_anomaly:
            pressure = int(random.choice([150, 850, 900]))
            flow_rate = int(random.choice([300, 2100, 50]))
            status = 1 # خطر / شذوذ
        else:
            pressure = int(random.uniform(445, 465))
            flow_rate = int(random.uniform(1190, 1220))
            status = 0 # آمن

        # تحديث المسجلات في الـ Modbus
        slave_id = 0
        context[slave_id].setValues(3, 0, [pressure, flow_rate, status])
        
        
        print(f"[Modbus PLC Server] Updated -> Pressure: {pressure/10.0}, Flow: {flow_rate/10.0}, Status Alert: {status}")
        await asyncio.sleep(3)

async def run_modbus_server():
    # تشغيل خادم Modbus TCP على المنفذ 5020
    loop = asyncio.get_running_loop()
    loop.create_task(update_sensor_registers())
    print("[*] Starting Modbus ICS Server on port 5020...")
    await StartAsyncTcpServer(context, address=("127.0.0.1", 5020))

if __name__ == "__main__":
    try:
        asyncio.run(run_modbus_server())
    except KeyboardInterrupt:
        print("\n[!] Modbus Server stopped by user.")