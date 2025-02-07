# 📌 Geospatial API باستخدام Django و DRF

🚀 مشروع API جغرافي باستخدام Django Rest Framework مع دعم للبيانات المكانية عبر PostGIS.

## 📚 المحتويات

- [📌 مقدمة](#-مقدمة)
- [🛠️ المتطلبات](#-المتطلبات)
- [🚀 التثبيت والتشغيل](#-التثبيت-والتشغيل)
- [🔍 استخدام الـ API](#-استخدام-ال-api)
- [📂 هيكل المشروع](#-هيكل-المشروع)
- [📛 الرخصة](#-الرخصة)

---

## 📌 مقدمة

هذا المشروع عبارة عن **REST API** يتيح التعامل مع البيانات الجغرافية مثل المباني والفئات باستخدام Django و **PostGIS**. يمكن للمستخدمين تنفيذ عمليات **CRUD** (إضافة، تعديل، حذف، قراءة) على المباني مع دعم **GeoJSON**.

---

## 🛠️ المتطلبات

قبل تشغيل المشروع، تأكد من تثبيت الأدوات التالية:

✅ Python 3.11+\
✅ Django 5+\
✅ Django REST Framework\
✅ PostgreSQL مع **PostGIS**\
✅ GDAL و GEOS

---

## 🚀 التثبيت والتشغيل

### 1️⃣ استنساخ المشروع من GitHub

```bash
git clone https://github.com/HossamHassan999/GeoAPI-WithDjango.git
cd GeoAPI-WithDjango
```

### 2️⃣ إنشاء بيئة افتراضية وتفعيلها

```bash
python -m venv env
source env/bin/activate  # على macOS/Linux
env\Scripts\activate     # على Windows
```

### 3️⃣ تثبيت المتطلبات

```bash
pip install -r requirements.txt
```

### 4️⃣ إعداد قاعدة البيانات

- تأكد من أن **PostgreSQL** يعمل وقم بإنشاء قاعدة بيانات جديدة مع **PostGIS**.
- قم بتحديث \`\` لإضافة معلومات الاتصال بقاعدة البيانات.
- ثم قم بتنفيذ الترحيلات:
  ```bash
  python manage.py migrate
  ```

### 5️⃣ تشغيل السيرفر

```bash
python manage.py runserver
```

📌 **الآن API جاهزة للعمل على**: `http://127.0.0.1:8000/`

---

## 🔍 استخدام الـ API

### 📌 إنشاء مبنى جديد (POST `/API/Building/`)

👤 **طلب (Request)**

```json
{
    "name": "مبنى تجاري",
    "price": 1500000.00,
    "category": 1,
    "geom": {
        "type": "MultiPolygon",
        "coordinates": [
            [
                [
                    [31.4573, 30.0189],
                    [31.4574, 30.0187],
                    [31.4572, 30.0186],
                    [31.4573, 30.0189]
                ]
            ]
        ]
    }
}
```

📥 **استجابة (Response)**

```json
{
    "type": "FeatureCollection",
    "features": [
        {
            "type": "Feature",
            "geometry": {
                "type": "MultiPolygon",
                "coordinates": [
                    [
                        [
                            [31.457307507590098, 30.0189069213852],
                            [31.457470975877055, 30.018780004102084],
                            [31.45730494943802, 30.018637511491004],
                            [31.45725085290047, 30.01865444544764],
                            [31.457216215323207, 30.01871845623198],
                            [31.45721503679648, 30.018794571513403],
                            [31.457201308660647, 30.018811978793014],
                            [31.457307507590098, 30.0189069213852]
                        ]
                    ]
                ]
            },
            "properties": {
                "name": "مبنى ",
                "price": "1500000.00",
                "category": 1
            }
        }
    ]
}
```

🔹 **يمكنك أيضًا تنفيذ عمليات** `GET` و `PUT` و `DELETE` لنقاط البيانات.

---

## 📂 هيكل المشروع

```
GeoAPI-WithDjango/
│── Core/
│   ├── models.py      # نماذج البيانات
│   ├── serializers.py # تحويل البيانات إلى JSON
│   ├── views.py       # منطق API
│   ├── urls.py        # روابط API
│── GeospatialAPI/
│── env/               # البيئة الافتراضية (يتم تجاهلها في Git)
│── db.sqlite3         # قاعدة البيانات (إذا كنت تستخدم SQLite)
│── requirements.txt   # المكتبات المطلوبة
│── manage.py          # أداة إدارة Django
│── .gitignore         # لمنع رفع الملفات غير المرغوب بها
│── README.md          # ملف التوثيق (أنت هنا!)
```

---

## 📛 الرخصة

🔹 **هذا المشروع مفتوح المصدر** بموجب رخصة **MIT**، يمكنك استخدامه بحرية مع ذكر المصدر.

👨‍💻 **تم التطوير بواسطة:** [Hossam Hassan](https://github.com/HossamHassan999)

🚀 **استمتع ببناء تطبيقات Geospatial باستخدام Django!** 🌍🔥

