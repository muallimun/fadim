
import os
import sys
import threading

try:
    import pystray
    from PIL import Image, ImageDraw
    PYSTRAY_AVAILABLE = True
except ImportError:
    PYSTRAY_AVAILABLE = False

class SystemTray:
    def __init__(self, app):
        self.app = app
        self.tray = None
        self.running = False

    def setup_tray(self):
        """Sistem trayını kur"""
        if not PYSTRAY_AVAILABLE:
            print("⚠️ pystray kütüphanesi bulunamadı, sistem tray devre dışı")
            return False

        try:
            # İkon yükle - EXE derlemesi için uygun yol
            icon_path = os.path.join('core', 'fadim_icon.png')

            # PyInstaller uyumlu resource path kontrolü
            if hasattr(self.app, 'get_resource_path'):
                icon_path = self.app.get_resource_path(icon_path)

            if os.path.exists(icon_path):
                icon_image = Image.open(icon_path)
                print(f"✅ Sistem tepsisi ikonu yüklendi: {icon_path}")
            else:
                # Varsayılan emoji ikon oluştur (mavi kutu yerine)
                from PIL import ImageDraw
                icon_image = Image.new('RGBA', (64, 64), (0, 123, 255, 255))
                draw = ImageDraw.Draw(icon_image)
                # Basit F harfi çiz
                draw.text((20, 15), "F", fill='white')
                print("⚠️ Varsayılan sistem tepsisi ikonu oluşturuldu")

            # Menü oluştur
            menu = pystray.Menu(
                pystray.MenuItem(self.app.get_text('tray_show'), self.show_app),
                pystray.MenuItem(self.app.get_text('tray_capture'), self.capture_screen_tray),
                pystray.Menu.SEPARATOR,
                pystray.MenuItem(self.app.get_text('tray_settings'), self.open_settings),
                pystray.MenuItem(self.app.get_text('tray_exit'), self.quit_app)
            )

            self.tray = pystray.Icon("FADIM", icon_image, self.app.get_text('app_title_en'), menu)
            return True

        except Exception as e:
            print(f"❌ Sistem trayı kurulumu hatası: {e}")
            return False

    def run_tray(self):
        """Tray'i çalıştır"""
        if self.tray and PYSTRAY_AVAILABLE:
            try:
                tray_thread = threading.Thread(target=self.tray.run, daemon=True)
                tray_thread.start()
                self.running = True
                return True
            except Exception as e:
                print(f"Tray çalıştırma hatası: {e}")
                return False
        return False

    def hide_to_tray(self):
        """Pencereyi tray'e gizle"""
        if PYSTRAY_AVAILABLE and self.tray:
            self.app.withdraw()

    def show_app(self, icon=None, item=None):
        """Pencereyi göster"""
        self.app.deiconify()
        self.app.lift()
        self.app.focus_force()

    def capture_screen_tray(self, icon=None, item=None):
        """Tray'den ekran yakalama"""
        self.app.after(0, self.app.capture_and_process)

    def open_settings(self, icon=None, item=None):
        """Ayarlar penceresini aç"""
        self.app.after(0, self.app.open_settings_window)

    def quit_app(self, icon=None, item=None):
        """Uygulamayı kapat"""
        self.app.after(0, self.app.quit_app)

    def stop_tray(self):
        """Tray'i durdur"""
        if self.tray and PYSTRAY_AVAILABLE and self.running:
            try:
                self.tray.stop()
                self.running = False
            except Exception as e:
                print(f"Tray durdurma hatası: {e}")
