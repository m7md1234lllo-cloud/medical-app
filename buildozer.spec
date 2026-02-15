[app]

# اسم التطبيق (يظهر على الهاتف)
title = نظام الملفات الطبية

# اسم الحزمة (package name) - يجب أن يكون فريد
package.name = medicalrecords

# نطاق التطبيق (domain) - يستخدم في تمييز التطبيق
package.domain = org.medicalapp

# المجلد المصدر (حيث يوجد الكود)
source.dir = .

# الامتدادات المضمنة
source.include_exts = py,png,jpg,jpeg,kv,atlas,db,html,css,js,woff,woff2,ttf,svg

# الملفات والمجلدات المضمنة
source.include_patterns = templates/*,static/*,static/css/*,static/js/*

# الملفات المستثناة
source.exclude_dirs = tests, bin, .buildozer, .git, __pycache__, .venv, buildenv
source.exclude_patterns = buildozer.spec,BUILD_INSTRUCTIONS.md,FIX_GUIDE.md,.gitignore

# إصدار التطبيق
version = 1.0

# المتطلبات (Python packages)
# ملاحظة: sqlite3 مدمج مع Python
requirements = python3,kivy==2.2.1,flask,werkzeug,jinja2,markupsafe,itsdangerous,click,android,pyjnius

# Bootstrap (نوع التطبيق)
p4a.bootstrap = sdl2webview

# الأذونات (permissions)
android.permissions = INTERNET,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE,RECORD_AUDIO

# الميزات المطلوبة
android.features = android.hardware.microphone

# الأيقونة (إذا أردت تخصيصها)
# icon.filename = %(source.dir)s/icon.png

# الشاشة الافتتاحية (إذا أردت تخصيصها)
# presplash.filename = %(source.dir)s/presplash.png

# التوجيه (orientation)
# يمكن أن يكون: landscape, portrait, sensor, all
orientation = portrait

# تفعيل fullscreen
fullscreen = 0

# Android API المستهدف (Target API)
android.api = 33

# الحد الأدنى لـ Android API (Min API)
android.minapi = 21

# Android SDK version
android.sdk = 31

# Android NDK version (استخدم 25b أو أحدث)
android.ndk = 25b

# تفعيل AndroidX (ضروري للإصدارات الحديثة)
android.enable_androidx = True

# رقم إصدار التطبيق (يستخدم في التحديثات)
android.numeric_version = 1

# المعماريات المدعومة (architectures)
# armeabi-v7a للأجهزة القديمة، arm64-v8a للأجهزة الحديثة
android.archs = arm64-v8a,armeabi-v7a

# السماح بالنسخ الاحتياطي
android.allow_backup = True

# اسم الحزمة الكامل
android.accept_sdk_license = True

# إضافات Gradle (للدعم WebView)
android.gradle_dependencies = androidx.webkit:webkit:1.5.0

# خيارات Gradle إضافية (لتحسين الأداء)
android.add_gradle_repositories = 

# وضع السياسات الأمنية
android.uses_library = org.apache.http.legacy

# Wakelock لمنع إيقاف التطبيق
android.wakelock = True

# الخدمات في الخلفية (إذا احتجت)
# services = NAME:service.py

[buildozer]

# مستوى السجلات (log level):
# 0 = خطأ فقط، 1 = معلومات، 2 = تصحيح كامل
log_level = 2

# عدد المحاولات لتحميل الحزم
installer_timeout = 600

# تحذير عند استخدام root
warn_on_root = 1

# مسار Android SDK و NDK (إذا لم يتم اكتشافه تلقائياً)
# android.sdk_path = ~/.buildozer/android/platform/android-sdk
# android.ndk_path = ~/.buildozer/android/platform/android-ndk-r25b
