#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
تطبيق أندرويد لنظام إدارة الملفات الطبية
Android App for Medical Records Management System
"""

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.clock import Clock
from kivy.logger import Logger
import threading
import time
import os

# التحقق من البيئة
try:
    from android.runnable import run_on_ui_thread
    from jnius import autoclass
    IS_ANDROID = True
except ImportError:
    IS_ANDROID = False
    def run_on_ui_thread(func):
        return func

# Import Flask app
from app import app as flask_app, init_db


class MedicalRecordsApp(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.flask_thread = None
        self.webview = None
        
    def build(self):
        """بناء واجهة التطبيق"""
        Logger.info("MedicalApp: بدء تهيئة التطبيق")
        
        # تهيئة قاعدة البيانات
        try:
            init_db()
            Logger.info("MedicalApp: تم تهيئة قاعدة البيانات")
        except Exception as e:
            Logger.error(f"MedicalApp: خطأ في تهيئة قاعدة البيانات: {e}")
        
        # بدء Flask في خلفية
        self.start_flask_server()
        
        # انتظار ثم فتح WebView
        if IS_ANDROID:
            Clock.schedule_once(self.setup_webview, 2)
        
        return Widget()
    
    def start_flask_server(self):
        """تشغيل خادم Flask في خلفية"""
        def run_flask():
            try:
                Logger.info("MedicalApp: بدء خادم Flask")
                flask_app.run(
                    host='127.0.0.1',
                    port=5000,
                    debug=False,
                    use_reloader=False,
                    threaded=True
                )
            except Exception as e:
                Logger.error(f"MedicalApp: خطأ في تشغيل Flask: {e}")
        
        self.flask_thread = threading.Thread(target=run_flask, daemon=True)
        self.flask_thread.start()
        Logger.info("MedicalApp: تم بدء thread خادم Flask")
    
    @run_on_ui_thread
    def setup_webview(self, dt):
        """إعداد WebView لعرض تطبيق Flask"""
        if not IS_ANDROID:
            Logger.warning("MedicalApp: WebView متاح فقط على أندرويد")
            return
            
        try:
            Logger.info("MedicalApp: إعداد WebView")
            
            # استيراد classes أندرويد
            PythonActivity = autoclass('org.kivy.android.PythonActivity')
            WebView = autoclass('android.webkit.WebView')
            WebViewClient = autoclass('android.webkit.WebViewClient')
            LayoutParams = autoclass('android.view.ViewGroup$LayoutParams')
            LinearLayout = autoclass('android.widget.LinearLayout')
            
            # الحصول على activity
            activity = PythonActivity.mActivity
            webview = WebView(activity)
            
            # إعدادات WebView
            settings = webview.getSettings()
            settings.setJavaScriptEnabled(True)
            settings.setDomStorageEnabled(True)
            settings.setDatabaseEnabled(True)
            settings.setAllowFileAccess(True)
            settings.setAllowContentAccess(True)
            settings.setAllowFileAccessFromFileURLs(True)
            settings.setAllowUniversalAccessFromFileURLs(True)
            settings.setMediaPlaybackRequiresUserGesture(False)
            settings.setBuiltInZoomControls(False)
            settings.setDisplayZoomControls(False)
            
            # إنشاء WebViewClient مخصص
            webview.setWebViewClient(WebViewClient())
            
            # إنشاء Layout
            layout = LinearLayout(activity)
            layout.setOrientation(LinearLayout.VERTICAL)
            layout.addView(webview, LayoutParams(
                LayoutParams.MATCH_PARENT,
                LayoutParams.MATCH_PARENT
            ))
            
            # تحميل الصفحة
            webview.loadUrl('http://127.0.0.1:5000')
            
            # تعيين content view
            activity.setContentView(layout)
            
            self.webview = webview
            Logger.info("MedicalApp: تم إعداد WebView بنجاح")
            
        except Exception as e:
            Logger.error(f"MedicalApp: خطأ في إعداد WebView: {e}")
            import traceback
            Logger.error(f"MedicalApp: {traceback.format_exc()}")
    
    def on_pause(self):
        """عند إيقاف التطبيق مؤقتاً"""
        return True
    
    def on_resume(self):
        """عند استئناف التطبيق"""
        if self.webview and IS_ANDROID:
            try:
                self.webview.reload()
            except:
                pass


if __name__ == '__main__':
    MedicalRecordsApp().run()
