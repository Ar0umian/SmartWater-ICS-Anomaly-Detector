# 🌊 SmartWater-ICS: Edge-Based Anomaly Detection for Municipal Water Infrastructure
## نظام "رافد-أمان": للكشف الذكي عن الاختراقات في شبكات المياه البلدية

> مشروع مقدم ضمن **المسار الرابع: تحديات تبني التقنيات الناشئة وإدارة البيانات** (توظيف الذكاء الاصطناعي وإنترنت الأشياء، وسيادة البيانات).

---

## 📌 نبذة عن المشروع (Overview)
تعتمد المدن الذكية الحديثة على أنظمة تحكم ومستشعرات إنترنت أشياء (IoT) لتدفقات المياه، والتي تكون عرضة غالباً لمخاطر التلاعب بالبيانات أو الاختراقات في البنى التشغيلية (OT/ICS). 

يقدم نظام **"رافد-أمان"** حلماً برمجياً ذكياً لمحاكاة ومراقبة بيانات الحساسات التشغيلية (مبني باستخدام Python و Flask)، ويعتمد على خوارزميات تعلم الآلة المتقدمة (مثل **Isolation Forest** مدعومة بمعالجة الحافة **Edge Computing**) لاكتشاف الشذوذ أو محاولات التلاعب في الوقت الفعلي عند حافة الشبكة، مما يضمن سيادة البيانات وحماية البنى التحتية الحرجة.

---

## 📸 معاينة النظام (System Demo)

<p align="center">
  <img src="https://github.com/Ar0umian/demo/blob/main/SmartWater-ICS.gif" alt="SmartWater-ICS Demo">
</p>

---

## ⚙️ التقنيات المستخدمة (Tech Stack)
* **Backend & Web Server:** Python, Flask
* **Machine Learning & AI:** Scikit-Learn (Isolation Forest Algorithm)
* **Data Processing:** Pandas, NumPy
* **Frontend & Visualization:** HTML5, CSS3, JavaScript, Chart.js (بواجهة رسم بياني احترافية ذات خلفية بيضاء نقية للتقارير الهندسية)
* **Architecture:** Edge Computing Simulation for OT/ICS Networks

---

## 🚀 الأثر المتوقع (Expected Impact)
1. **حماية البنى التحتية الحرجة:** تأمين شبكات المياه في المدن الكبرى ومناطق الكثافة العالية (مثل مكة المكرمة والمنطقة الشرقية) ضد التلاعب والأعطال التشغيلية.
2. **دقة القرار وسيادة البيانات:** ضمان صحة الأدلة والبيانات المرفوعة لمتخذ القرار ورفع كفاءة الاستجابة الفورية لفرق الصيانة والأمانات.
3. **التوافق الوطني:** دعم مستهدفات استراتيجية الأمن السيبراني الوطني وأمن الأنظمة التشغيلية (OT/ICS Security) للقطاع البلدي.

---

## 🛠️ طريقة التشغيل المحلية (Getting Started)

تأكد من تثبيت بايثون على جهازك، ثم اتبع الخطوات التالية لتشغيل المشروع محلياً:

1. **استنساخ المستودع (Clone Repository):**
   ```bash
   git clone [https://github.com/Ar0umian/SmartWater-ICS-Anomaly-Detector.git](https://github.com/Ar0umian/SmartWater-ICS-Anomaly-Detector.git)
   cd SmartWater-ICS-Anomaly-Detector

2. **إنشاء وتفعيل البيئة الافتراضية (Virtual Environment):**
    python -m venv venv
    # على نظام Mac/Linux:
    source venv/bin/activate
    # على نظام Windows:
    # venv\Scripts\activate

3. **تثبيت المكتبات المطلوبة:**
    pip install -r requirements.txt

4. **تشغيل محاكي سيرفر Modbus (في نافذة Terminal مستقلة):**
    python simulator/modbus_server.py

5. **تشغيل تطبيق الويب الرئيسي (في نافذة Terminal الأساسية):**
    python app.py

6. **فتح المتصفح :**
    http://127.0.0.1:5000

---


## 📄 الترخيص (License)
هذا المشروع مُطوّر لأغراض الابتكار وتطوير المدن الذكية وحماية البنى التحتية.

