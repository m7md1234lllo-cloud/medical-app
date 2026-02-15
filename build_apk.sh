#!/bin/bash

# سكريبت بناء تطبيق Android APK
# Build Script for Android APK

set -e  # إيقاف السكريبت عند أي خطأ

echo "=========================================="
echo "🏥 بناء تطبيق نظام الملفات الطبية"
echo "=========================================="
echo ""

# التحقق من Python
if ! command -v python3 &> /dev/null; then
    echo "❌ خطأ: Python 3 غير مثبت"
    echo "قم بتثبيته باستخدام: sudo apt install python3"
    exit 1
fi

echo "✅ Python موجود: $(python3 --version)"

# إنشاء بيئة افتراضية إذا لم تكن موجودة
if [ ! -d "buildenv" ]; then
    echo ""
    echo "📦 إنشاء بيئة افتراضية..."
    python3 -m venv buildenv
fi

# تفعيل البيئة الافتراضية
echo "🔌 تفعيل البيئة الافتراضية..."
source buildenv/bin/activate

# تثبيت/تحديث المتطلبات
echo ""
echo "📥 تثبيت/تحديث Buildozer و Cython..."
pip install --upgrade pip
pip install --upgrade buildozer cython==0.29.33

# تنظيف البناء السابق (اختياري)
read -p "هل تريد تنظيف البناء السابق؟ (y/N): " clean_build
if [[ $clean_build =~ ^[Yy]$ ]]; then
    echo "🧹 تنظيف البناء السابق..."
    rm -rf .buildozer
    rm -rf bin
fi

# اختيار نوع البناء
echo ""
echo "اختر نوع البناء:"
echo "1) Debug (للاختبار)"
echo "2) Release (للنشر)"
read -p "اختيارك (1 أو 2): " build_type

if [ "$build_type" = "2" ]; then
    BUILD_CMD="buildozer android release"
    echo "🔨 بناء نسخة Release..."
else
    BUILD_CMD="buildozer android debug"
    echo "🔨 بناء نسخة Debug..."
fi

echo ""
echo "⏳ جاري البناء... (قد يستغرق 30-60 دقيقة في المرة الأولى)"
echo ""

# بناء التطبيق
$BUILD_CMD

# التحقق من نجاح البناء
if [ $? -eq 0 ]; then
    echo ""
    echo "=========================================="
    echo "✅ تم البناء بنجاح!"
    echo "=========================================="
    echo ""
    echo "📱 ملف APK موجود في:"
    find bin/ -name "*.apk" -type f
    echo ""
    echo "📋 لتثبيت التطبيق على هاتفك:"
    echo "   1. وصل هاتفك بالكمبيوتر"
    echo "   2. نفذ: adb install bin/*.apk"
    echo "   أو انسخ ملف APK للهاتف وثبته يدوياً"
    echo ""
else
    echo ""
    echo "❌ فشل البناء!"
    echo "راجع سجلات الخطأ في: .buildozer/logs/"
    exit 1
fi
