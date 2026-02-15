# 📋 الأوامر الجاهزة - انسخ والصق مباشرة

## ⚠️ مهم: غير هذه المعلومات قبل التنفيذ

```bash
# غير هذه القيم حسب معلوماتك:
YOUR_GITHUB_USERNAME="اسم_المستخدم_حقك"
YOUR_EMAIL="your.email@example.com"
YOUR_NAME="اسمك الكامل"
```

---

## 🔧 الخطوة 1: تثبيت Git على Termux

```bash
pkg update
pkg install git
```

---

## ⚙️ الخطوة 2: تكوين Git (أول مرة فقط)

```bash
# غير الاسم والإيميل لمعلوماتك
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
```

---

## 📂 الخطوة 3: الانتقال لمجلد المشروع

```bash
cd ~/downloads/medical_records_app
```

---

## 🎯 الخطوة 4: تهيئة Git ورفع المشروع

```bash
# تهيئة repo محلي
git init

# إضافة جميع الملفات
git add .

# عمل commit أولي
git commit -m "Initial commit - Medical Records App"

# تغيير الـ branch الرئيسي لـ main
git branch -M main

# ربط الـ repo البعيد (غير YOUR_USERNAME لاسمك)
git remote add origin https://github.com/YOUR_USERNAME/medical-records-app.git

# رفع الملفات
git push -u origin main
```

**ملاحظة:** راح يطلب منك:
- Username: اسم مستخدمك في GitHub
- Password: استخدم **Personal Access Token** (ليس كلمة المرور العادية)

---

## 🔑 إنشاء Personal Access Token

إذا طلب كلمة مرور:

1. افتح: https://github.com/settings/tokens
2. اضغط "Generate new token" → "Generate new token (classic)"
3. الاسم: `Termux Access`
4. Scope: اختر **repo** فقط
5. اضغط "Generate token"
6. **انسخ الـ token** (لن تراه مرة أخرى!)
7. استخدمه بدلاً من كلمة المرور

---

## 🔄 الخطوة 5: التحديثات المستقبلية

عندما تعدل الكود وتبي ترفع تحديث:

```bash
# إضافة التعديلات
git add .

# عمل commit مع رسالة واضحة
git commit -m "وصف التحديث - مثال: إصلاح خطأ في البحث"

# رفع التحديث
git push origin main
```

---

## 🏷️ إنشاء Release مرقم (اختياري)

```bash
# عدل رقم الإصدار في buildozer.spec أولاً
nano buildozer.spec
# غير version = 1.0 إلى version = 1.1 مثلاً

# ثم:
git add buildozer.spec
git commit -m "v1.1: وصف التحسينات"
git tag v1.1
git push origin main
git push origin v1.1
```

---

## 🔧 حل المشاكل الشائعة

### مشكلة: rejected (non-fast-forward)

```bash
git pull origin main --rebase
git push origin main
```

### مشكلة: remote already exists

```bash
git remote remove origin
git remote add origin https://github.com/YOUR_USERNAME/medical-records-app.git
git push -u origin main
```

### مشكلة: Authentication failed

- تأكد من استخدام Personal Access Token وليس كلمة المرور
- أو ثبت GitHub CLI:

```bash
pkg install gh
gh auth login
```

---

## 📱 تحميل APK بعد البناء

### من المتصفح:

1. اذهب: https://github.com/YOUR_USERNAME/medical-records-app/actions
2. اضغط على آخر workflow ناجح (✅)
3. انزل لـ "Artifacts"
4. حمل "medical-records-apk"
5. فك الضغط وثبت APK

### من Releases (بعد عمل tag):

https://github.com/YOUR_USERNAME/medical-records-app/releases

---

## ✅ تأكد من نجاح الرفع

```bash
# تحقق من الـ remote
git remote -v

# تحقق من الـ branch
git branch

# تحقق من آخر commits
git log --oneline -5
```

---

## 🎯 ملخص سريع (كل الأوامر مع بعض)

```bash
# تثبيت وتكوين Git
pkg update && pkg install git
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"

# الانتقال للمشروع وتهيئة Git
cd ~/downloads/medical_records_app
git init
git add .
git commit -m "Initial commit - Medical Records App"
git branch -M main

# ربط ورفع (غير YOUR_USERNAME)
git remote add origin https://github.com/YOUR_USERNAME/medical-records-app.git
git push -u origin main
```

---

## 📝 ملاحظات مهمة

1. ✅ تأكد من تغيير `YOUR_USERNAME` لاسم مستخدمك الحقيقي
2. ✅ احفظ Personal Access Token في مكان آمن
3. ✅ كل push راح يبدأ بناء APK تلقائياً
4. ✅ البناء الأول يأخذ 30-40 دقيقة
5. ✅ البناءات التالية أسرع (15-25 دقيقة)

---

## 🎉 بعد النجاح

- ✅ افتح صفحة repo في GitHub
- ✅ راقب Actions في تبويب "Actions"
- ✅ انتظر البناء يخلص
- ✅ حمل APK من Artifacts
- ✅ ثبته على هاتفك!

---

صُنع بـ ❤️ لتسهيل العملية عليك
حظاً موفقاً! 🚀
