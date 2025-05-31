# -*- coding: utf-8 -*-
"""
FADIM Çoklu Dil Desteği
Desteklenen diller: Türkçe (tr), İngilizce (en), Arapça (ar)
"""

LANGUAGES = {
    'tr': {
        # Ana UI öğeleri
        'title': "FADIM - Görselden Metne",
        'language_selection': "🌐 Arayüz Dili:",
        'ocr_language': "🔤 OCR Dili:",
        'help_text': "ℹ️ Yardım:",
        'help_hotkey': "Kısayol: {hotkey}",
        'ocr_result': "📝 OCR Sonucu",
        'operations': "🎯 İşlemler",
        'close_app': "❌ Kapat",

        # Diller
        'lang_turkish': "Türkçe",
        'lang_english': "İngilizce", 
        'lang_arabic': "Arapça",

        # Butonlar
        'take_screenshot': "📷 Ekran Alıntısı Al",
        'open_file': "📂 Dosya Aç",
        'stop_gif': "⏹️ GIF Dur",
        'save_txt': "💾 TXT Kaydet",
        'save_docx': "📄 DOCX Kaydet",
        'clear_text': "🗑️ Metni Temizle",
        'copy_text': "📋 Metni Kopyala",

        # Menü öğeleri
        'menu_file': "Dosya",
        'menu_open_image': "Görsel Aç",
        'menu_show_records': "Kayıtları Göster",
        'menu_settings': "Ayarlar",
        'menu_edit_settings': "Ayarları Düzenle",
        'menu_cleanup': "Temizlik",
        'menu_help': "Yardım",
        'menu_usage_guide': "Kullanım Kılavuzu",
        'menu_tesseract_install': "Tesseract Kurulumu",
        'menu_update_check': "Güncelleme Kontrol",
        'menu_website': "Web Sitesi",
        'menu_about': "Hakkında",

        # Ayarlar
        'settings_title': "⚙️ FADIM Ayarları",
        'settings_general': "Genel",
        'settings_input_cursor': "Girdi & İmleç",
        'settings_advanced': "Gelişmiş",
        'default_ocr_lang': "Varsayılan OCR Dili",
        'capture_mode_settings': "Yakalama Modu",
        'sound_settings': "Ses Ayarları",
        'click_sound': "Tıklama sesi",
        'mouse_cursor': "Fare İmleci",
        'show_cursor': "İmleci göster",
        'cursor_trail': "İmleç izi",
        'hotkeys': "Kısayol Tuşları",
        'capture_hotkey': "Yakalama kısayolu:",
        'esc_note': "Not: ESC tuşu GIF kaydını durdurur",
        'system_tray': "Sistem Tepsisi",
        'minimize_to_tray': "Sistem tepsisine küçült",
        'data_management': "Veri Yönetimi",
        'clear_all_records': "Tüm Kayıtları Sil",
        'save_settings': "💾 Ayarları Kaydet",
        'settings_saved': "✅ Ayarlar kaydedildi",

        # Mod seçimi
        'capture_mode': "📸 Yakalama Modu",
        'ocr_mode': "🔤 OCR Modu",
        'gif_mode': "🎥 GIF Modu",
        'screenshot_mode': "📷 Ekran Görüntüsü",
        'quick_mode_selection': "⚡ Hızlı Mod Seçimi",
        'quick_ocr': "⚡ Hızlı OCR",
        'quick_gif': "⚡ Hızlı GIF",
        'quick_screenshot': "⚡ Hızlı Görüntü",
        'active_mode': "Aktif: {mode}",
        'mode_ocr': "OCR Modu",
        'mode_gif': "GIF Modu", 
        'mode_screenshot': "Ekran Görüntüsü Modu",
        'mode_unknown': "Bilinmeyen Mod",

        # GIF seçenekleri
        'gif_options': "🎥 GIF Seçenekleri",
        'quality': "Kalite:",
        'duration': "Süre (sn):",
        'fps': "FPS:",
        'select_region': "🎯 Bölge Seç",

        # Metin düzenleme
        'font_size': "Font:",
        'alignment': "Hizalama:",
        'align_left': "Sol",
        'align_center': "Orta",
        'align_right': "Sağ",
        'style': "Stil:",
        'bold': "Kalın",
        'italic': "Eğik",

        # Durum mesajları
        'status_ready': "Hazır (Ctrl+Shift+F: ekran alıntısı)",
        'status_no_text': "Hiç metin yok",
        'language_selected': "🌐 Dil seçildi: {lang}",
        'language_update_error': "❌ Dil güncellenemedi: {error}",
        'text_loaded': "✅ Metin yüklendi: {timestamp}",
        'gif_recording_active': "🔴 GIF kaydı aktif",
        'region_selected': "Bölge seçildi: {width}x{height} piksel",
        'region_cancelled': "Bölge seçimi iptal edildi",
        'hotkeys_active': "✅ Kısayollar aktif: {hotkey} (yakalama)",
        'keyboard_not_found': "⚠️ Klavye kütüphanesi bulunamadı, kısayollar devre dışı",
        'hotkey_error': "❌ Kısayol ayarlanırken hata: {error}",
        'capture_starting': "Ekran alıntısı alınıyor...",
        'capture_error': "Ekran alıntısı hatası: {error}",
        'gif_recording_starting': "GIF kaydı başlatılıyor...",
        'gif_saved': "GIF kaydedildi: {filename}",
        'gif_stop_requested': "GIF kaydı durdurma talebi gönderildi...",
        'gif_stopped_button': "GIF kaydı buton ile durduruldu...",
        'no_active_gif': "Aktif GIF kaydı bulunamadı",
        'region_selected_size': "Bölge seçildi: {width}x{height} px",
        'region_cancelled_selection': "Bölge seçimi iptal edildi",
        'mode_selected': "✅ {mode} seçildi",
        'mode_change_error': "❌ Mod değiştirilemedi: {error}",
        'text_copied': "Metin panoya kopyalandı",
        'file_saved': "Dosya kaydedildi: {path}",
        'arabic_detected': "Arapça metin algılandı ve sağa yaslandı",
        'text_processed_saved': "✅ Metin alındı, kaydedildi (ID: {id}) - {status}",
        'text_processed_error': "❌ Metin alındı ancak veritabanına kaydedilemedi: {error}",
        'image_clipboard_success': "Görsel panoya kopyalandı",
        'image_clipboard_failed': "Görsel kopyalama başarısız",

        # İstatistikler
        'stats_format': "Satır: {lines} | Sözcük: {words} | Karakter: {chars}",
        'stats_lines': "Satır",
        'stats_words': "Sözcük", 
        'stats_characters': "Karakter",

        # Kayıtlar penceresi
        'records_title': "📊 OCR Kayıtları",
        'records_list': "Kayıt Listesi",
        'screenshot_preview': "Ekran Görüntüsü Önizleme",
        'records_date': "Tarih",
        'records_source': "Kaynak",
        'records_language': "Dil", 
        'records_preview': "Önizleme",
        'preview_select': "Önizleme için bir kayıt seçin",
        'preview_not_found': "Ekran görüntüsü bulunamadı",
        'preview_error': "Önizleme hatası",
        'delete_selected': "🗑️ Seçileni Sil",
        'close': "❌ Kapat",
        'total_records': "Toplam kayıt sayısı: {count}",
        'record_count_error': "Kayıt sayısı alınamadı",
        'confirm_delete_record': "Seçili kaydı silmek istediğinizden emin misiniz?",
        'record_deleted': "Kayıt silindi.",
        'select_record_to_delete': "Silmek için bir kayıt seçin",
        'record_delete_error': "Kayıt silinirken hata",

        # Temizlik
        'cleanup_title': "🧹 Dosya Temizliği",
        'disk_usage': "Disk Kullanımı",
        'total_size': "Toplam boyut: {size} MB",
        'file_count': "Dosya sayısı: {count}",
        'cleanup_settings': "Temizlik Ayarları",
        'days_to_keep': "Tutulacak gün sayısı:",
        'max_files': "Maksimum dosya sayısı:",
        'save_cleanup_settings': "💾 Ayarları Kaydet",
        'start_cleanup': "🧹 Temizliği Başlat",
        'delete_all': "🗑️ HEPSİNİ SİL",
        'cleanup_started': "Temizlik başlatıldı!\n{days} günden eski dosyalar temizlenecek.",
        'cleanup_completed': "✅ Temizlik tamamlandı!\n🗑️ Silinen dosya: {cleaned}\n💾 Tasarruf edilen alan: {saved} MB",
        'dangerous_operation': "⚠️ TEHLİKELİ İŞLEM",
        'delete_all_warning': "Bu işlem TÜM dosya ve kayıtları kalıcı olarak silecek!\nBu eylem geri alınamaz. Devam etmek istediğinizden emin misiniz?",
        'all_data_deleted': "✅ Tüm veriler silindi!\n🗑️ Silinen dosya: {count}",
        'cleanup_settings_saved': "Temizlik ayarları kaydedildi!",
        'cleanup_settings_error': "Ayarlar kaydedilemedi: {error}",
        'delete_error': "Silme sırasında hata: {error}",
        'auto_cleanup': "🧹 Otomatik temizlik: {count} dosya silindi",

        # Kayıt durumu mesajları  
        'recording_status': "🔴 Kayıt yapılıyor...\nDurdurmak için ESC'ye basın",

        # Hata mesajları
        'error': "Hata",
        'warning': "Uyarı", 
        'success': "Başarılı",
        'confirm': "Onay",
        'ocr_error': "OCR Hatası",
        'ocr_failed_tesseract': "❌ OCR başarısız - Tesseract kontrol edin",
        'ocr_failed_general': "❌ OCR genel hatası",
        'unexpected_error': "Beklenmeyen hata",
        'no_text_to_save': "Kaydedilecek metin yok",
        'app_already_running': "FADIM zaten çalışıyor!",
        'exit_title': "Çıkış",
        'confirm_exit': "FADIM'den çıkmak istediğinizden emin misiniz?",
        'confirm_clear_all': "Tüm kayıtları silmek istediğinizden emin misiniz? Bu işlem geri alınamaz.",
        'records_cleared': "Tüm kayıtlar silindi.",

        # Tooltip'ler
        'tooltip_lang_combo': "OCR işlemi için kullanılacak dili seçin",
        'tooltip_font_size': "Metin boyutunu ayarlayın",
        'tooltip_align_left': "Metni sola yasla",
        'tooltip_align_center': "Metni ortaya yasla", 
        'tooltip_align_right': "Metni sağa yasla",
        'tooltip_bold': "Metni kalın yap",
        'tooltip_italic': "Metni eğik yap",
        'tooltip_gif_quality': "GIF kalitesini seçin",
        'tooltip_gif_duration': "GIF kaydının süresini belirleyin",
        'tooltip_gif_fps': "Saniye başına kare sayısını belirleyin",
        'tooltip_select_region': "Kayıt için özel bölge seçin",
        'tooltip_ocr_mode': "Ekran alıntısından otomatik metin okuma",
        'tooltip_gif_mode': "Hareketli GIF kaydı yapma",
        'tooltip_screenshot_mode': "Sadece ekran görüntüsü alma",
        'tooltip_take_screenshot': "Ekran alıntısı al ve işle",
        'tooltip_open_file': "Bilgisayardan görsel dosyası aç",
        'tooltip_stop_gif': "Devam eden GIF kaydını durdur",
        'tooltip_save_txt': "Metni TXT dosyası olarak kaydet",
        'tooltip_save_docx': "Metni Word belgesi olarak kaydet",
        'tooltip_clear_text': "Metin alanını temizle",
        'tooltip_copy_text': "Metni panoya kopyala",
        'tooltip_close_app': "FADIM'i kapat",
        'tooltip_docs_folder': "Belge klasörünü aç",
        'tooltip_gif_folder': "GIF klasörünü aç",
        'tooltip_website': "FADIM web sitesini aç",
        'tooltip_main_site': "Ana web sitesini aç",

        # Yardım penceresi
        'help_title': "📖 FADIM Kullanım Kılavuzu",
        'help_basic_usage': "Temel Kullanım",
        'help_shortcuts': "Kısayol Tuşları",
        'help_shortcuts_content': """⌨️ Kısayol Tuşları

🎯 Ana Kısayollar:
• Ctrl+Shift+F: Ekran yakalama (varsayılan)
• ESC: GIF kaydını durdur

🔧 Kısayol Değiştirme:
1. Ayarlar > Ayarları Düzenle menüsüne gidin
2. "Girdi & İmleç" sekmesini açın
3. Yeni kısayol kombinasyonunu yazın
4. Ayarları Kaydet butonuna tıklayın

📝 Kısayol Formatları:
• ctrl+shift+f (Ctrl, Shift, F birlikte)
• alt+s (Alt + S)
• ctrl+alt+c (Ctrl, Alt, C birlikte)
• f1, f2, f3... (Fonksiyon tuşları)

⚠️ Önemli Notlar:
• Sistem kısayolları ile çakışmasına dikkat edin
• Geçersiz kombinasyonlar hata verebilir
• Değişiklikler hemen aktif olur""",
        'tesseract_help_title': "🔧 Tesseract OCR Kurulum Rehberi",
        'tesseract_windows': "Windows Kurulumu",
        'tesseract_linux': "Linux Kurulumu", 
        'official_website': "🌐 Resmi Web Sitesi",
        'windows_download': "💾 Windows İndir",
        'installation_complete': "✅ Kurulum Tamamlandı",
        'restart_fadim': "OCR özelliğini test etmek için FADIM'i yeniden başlatın!",

        # Hakkında penceresi
        'about_title': "ℹ️ FADIM Hakkında",
        'version': "Sürüm: {version}",
        'update_check_manual': "🔄 Güncelleme Kontrol",
        'up_to_date': "✅ Güncel",
        'up_to_date_message': "FADIM zaten güncel sürümde.\n\nMevcut sürüm: {version}",
        'update_check_error': "❌ Hata",
        'update_check_failed': "Güncelleme kontrolü başarısız:\n{error}",
        'checking_updates': "🔄 Güncelleme kontrol ediliyor...",

        # Sistem tepsisi
        'tray_show': "Göster",
        'tray_capture': "Ekran Yakala",
        'tray_settings': "Ayarlar",
        'tray_exit': "Çıkış",
        'app_title_en': "FADIM",
        
        # Hata mesajları
        'keyboard_not_found': "⚠️ Klavye kütüphanesi yok, kısayollar devre dışı",
        'hotkeys_active': "✅ Kısayollar aktif: {hotkey} (yakalama)",
        'hotkey_error': "❌ Kısayol ayarlanırken hata: {error}",
        
        # Eksik başlık metinleri
        'status_ready': "✅ Hazır",
        'limited_mode': "⚠️ Sınırlı Mod",
        'limited_mode_message': "Tesseract OCR bulunamadı. Sadece GIF kayıt özelliği kullanılabilir.",
        'app_already_running': "FADIM zaten çalışıyor!",

        # Eksik mesajlar
        'update_available_title': "🔄 Yeni Sürüm Mevcut",
        'update_available_message': "FADIM'in yeni bir sürümü mevcut!\n\nMevcut sürüm: {current_version}\nYeni sürüm: {latest_version}\n\nİndirme sayfasını açmak ister misiniz?",
        'limited_mode': "ℹ️ Sınırlı Mod",
        'limited_mode_message': "FADIM şu özelliklerle çalışacak:\n\n✅ GIF kaydı\n✅ Ekran görüntüleri\n❌ OCR metin okuma\n\nTesseract kurduktan sonra FADIM'i yeniden başlatın!"
    },

    'en': {
        # Main UI elements
        'title': "FADIM - Image to Text",
        'language_selection': "🌐 UI Language:",
        'ocr_language': "🔤 OCR Language:",
        'help_text': "ℹ️ Help:",
        'help_hotkey': "Hotkey: {hotkey}",
        'ocr_result': "📝 OCR Result",
        'operations': "🎯 Operations",
        'close_app': "❌ Close",

        # Languages
        'lang_turkish': "Turkish",
        'lang_english': "English",
        'lang_arabic': "Arabic",

        # Buttons
        'take_screenshot': "📷 Take Screenshot",
        'open_file': "📂 Open File",
        'stop_gif': "⏹️ Stop GIF",
        'save_txt': "💾 Save TXT",
        'save_docx': "📄 Save DOCX",
        'clear_text': "🗑️ Clear Text",
        'copy_text': "📋 Copy Text",

        # Menu items
        'menu_file': "File",
        'menu_open_image': "Open Image",
        'menu_show_records': "Show Records",
        'menu_settings': "Settings",
        'menu_edit_settings': "Edit Settings",
        'menu_cleanup': "Cleanup",
        'menu_help': "Help",
        'menu_usage_guide': "Usage Guide",
        'menu_tesseract_install': "Tesseract Installation",
        'menu_update_check': "Check Updates",
        'menu_website': "Website",
        'menu_about': "About",

        # Settings
        'settings_title': "⚙️ FADIM Settings",
        'settings_general': "General",
        'settings_input_cursor': "Input & Cursor",
        'settings_advanced': "Advanced",
        'default_ocr_lang': "Default OCR Language",
        'capture_mode_settings': "Capture Mode",
        'sound_settings': "Sound Settings",
        'click_sound': "Click sound",
        'mouse_cursor': "Mouse Cursor",
        'show_cursor': "Show cursor",
        'cursor_trail': "Cursor trail",
        'hotkeys': "Hotkeys",
        'capture_hotkey': "Capture hotkey:",
        'esc_note': "Note: ESC key stops GIF recording",
        'system_tray': "System Tray",
        'minimize_to_tray': "Minimize to tray",
        'data_management': "Data Management",
        'clear_all_records': "Clear All Records",
        'save_settings': "💾 Save Settings",
        'settings_saved': "✅ Settings saved",

        # Mode selection
        'capture_mode': "📸 Capture Mode",
        'ocr_mode': "🔤 OCR Mode",
        'gif_mode': "🎥 GIF Mode",
        'screenshot_mode': "📷 Screenshot Mode",
        'quick_mode_selection': "⚡ Quick Mode Selection",
        'quick_ocr': "⚡ Quick OCR",
        'quick_gif': "⚡ Quick GIF",
        'quick_screenshot': "⚡ Quick Screenshot",
        'active_mode': "Active: {mode}",
        'mode_ocr': "OCR Mode",
        'mode_gif': "GIF Mode",
        'mode_screenshot': "Screenshot Mode",
        'mode_unknown': "Unknown Mode",

        # GIF options
        'gif_options': "🎥 GIF Options",
        'quality': "Quality:",
        'duration': "Duration (s):",
        'fps': "FPS:",
        'select_region': "🎯 Select Region",

        # Text editing
        'font_size': "Font:",
        'alignment': "Alignment:",
        'align_left': "Left",
        'align_center': "Center",
        'align_right': "Right",
        'style': "Style:",
        'bold': "Bold",
        'italic': "Italic",

        # Status messages
        'status_ready': "Ready (Ctrl+Shift+F: screenshot)",
        'status_no_text': "No text available",
        'language_selected': "🌐 Language selected: {lang}",
        'language_update_error': "❌ Language update failed: {error}",
        'text_loaded': "✅ Text loaded: {timestamp}",
        'gif_recording_active': "🔴 GIF recording active",
        'region_selected': "Region selected: {width}x{height} pixels",
        'region_cancelled': "Region selection cancelled",
        'hotkeys_active': "✅ Hotkeys active: {hotkey} (capture)",
        'keyboard_not_found': "⚠️ Keyboard library not found, hotkeys disabled",
        'hotkey_error': "❌ Hotkey setup error: {error}",
        'capture_starting': "Taking screenshot...",
        'capture_error': "Screenshot error: {error}",
        'gif_recording_starting': "Starting GIF recording...",
        'gif_saved': "GIF saved: {filename}",
        'gif_stop_requested': "GIF stop request sent...",
        'gif_stopped_button': "GIF recording stopped via button...",
        'no_active_gif': "No active GIF recording found",
        'region_selected_size': "Region selected: {width}x{height} px",
        'region_cancelled_selection': "Region selection cancelled",
        'mode_selected': "✅ {mode} selected",
        'mode_change_error': "❌ Mode change failed: {error}",
        'text_copied': "Text copied to clipboard",
        'file_saved': "File saved: {path}",
        'arabic_detected': "Arabic text detected and right-aligned",
        'text_processed_saved': "✅ Text extracted, saved (ID: {id}) - {status}",
        'text_processed_error': "❌ Text extracted but could not be saved to database: {error}",
        'image_clipboard_success': "Image copied to clipboard",
        'image_clipboard_failed': "Image copy failed",

        # Statistics
        'stats_format': "Lines: {lines} | Words: {words} | Characters: {chars}",
        'stats_lines': "Lines",
        'stats_words': "Words",
        'stats_characters': "Characters",

        # Records window
        'records_title': "📊 OCR Records",
        'records_list': "Records List",
        'screenshot_preview': "Screenshot Preview",
        'records_date': "Date",
        'records_source': "Source",
        'records_language': "Language",
        'records_preview': "Preview",
        'preview_select': "Select a record for preview",
        'preview_not_found': "Screenshot not found",
        'preview_error': "Preview error",
        'delete_selected': "🗑️ Delete Selected",
        'close': "❌ Close",
        'total_records': "Total records: {count}",
        'record_count_error': "Cannot get record count",
        'confirm_delete_record': "Are you sure you want to delete the selected record?",
        'record_deleted': "Record deleted.",
        'select_record_to_delete': "Please select a record to delete",
        'record_delete_error': "Error deleting record",

        # Cleanup
        'cleanup_title': "🧹 File Cleanup",
        'disk_usage': "Disk Usage",
        'total_size': "Total size: {size} MB",
        'file_count': "File count: {count}",
        'cleanup_settings': "Cleanup Settings",
        'days_to_keep': "Days to keep:",
        'max_files': "Maximum file count:",
        'save_cleanup_settings': "💾 Save Settings",
        'start_cleanup': "🧹 Start Cleanup",
        'delete_all': "🗑️ DELETE ALL",
        'cleanup_started': "Cleanup started!\nFiles older than {days} days will be cleaned.",
        'cleanup_completed': "✅ Cleanup completed!\n🗑️ Files deleted: {cleaned}\n💾 Space saved: {saved} MB",
        'dangerous_operation': "⚠️ DANGEROUS OPERATION",
        'delete_all_warning': "This operation will permanently delete ALL files and records!\nThis action cannot be undone. Are you sure you want to continue?",
        'all_data_deleted': "✅ All data deleted!\n🗑️ Files deleted: {count}",
        'cleanup_settings_saved': "Cleanup settings saved!",
        'cleanup_settings_error': "Cannot save settings: {error}",
        'delete_error': "Error during deletion: {error}",
        'auto_cleanup': "🧹 Auto cleanup: {count} files deleted",

        # Recording status messages
        'recording_status': "🔴 Recording...\nPress ESC to stop",

        # Error messages
        'error': "Error",
        'warning': "Warning",
        'success': "Success",
        'confirm': "Confirm",
        'ocr_error': "OCR Error",
        'ocr_failed_tesseract': "❌ OCR failed - Check Tesseract",
        'ocr_failed_general': "❌ OCR general error",
        'unexpected_error': "Unexpected error",
        'no_text_to_save': "No text to save",
        'app_already_running': "FADIM is already running!",
        'exit_title': "Exit",
        'confirm_exit': "Are you sure you want to exit FADIM?",
        'confirm_clear_all': "Are you sure you want to delete all records? This action cannot be undone.",
        'records_cleared': "All records cleared.",

        # Tooltips
        'tooltip_lang_combo': "Select language for OCR processing",
        'tooltip_font_size': "Adjust text size",
        'tooltip_align_left': "Align text to left",
        'tooltip_align_center': "Align text to center",
        'tooltip_align_right': "Align text to right",
        'tooltip_bold': "Make text bold",
        'tooltip_italic': "Make text italic",
        'tooltip_gif_quality': "Select GIF quality",
        'tooltip_gif_duration': "Set GIF recording duration",
        'tooltip_gif_fps': "Set frames per second",
        'tooltip_select_region': "Select custom region for recording",
        'tooltip_ocr_mode': "Automatic text reading from screenshots",
        'tooltip_gif_mode': "Record animated GIF",
        'tooltip_screenshot_mode': "Take screenshots only",
        'tooltip_take_screenshot': "Take screenshot and process",
        'tooltip_open_file': "Open image file from computer",
        'tooltip_stop_gif': "Stop ongoing GIF recording",
        'tooltip_save_txt': "Save text as TXT file",
        'tooltip_save_docx': "Save text as Word document",
        'tooltip_clear_text': "Clear text area",
        'tooltip_copy_text': "Copy text to clipboard",
        'tooltip_close_app': "Close FADIM",
        'tooltip_docs_folder': "Open documents folder",
        'tooltip_gif_folder': "Open GIF folder",
        'tooltip_website': "Open FADIM website",
        'tooltip_main_site': "Open main website",

        # Help window
        'help_title': "📖 FADIM User Guide",
        'help_basic_usage': "Basic Usage",
        'help_shortcuts': "Hotkeys",
        'help_shortcuts_content': """⌨️ Hotkeys

🎯 Main Hotkeys:
• Ctrl+Shift+F: Screen capture (default)
• ESC: Stop GIF recording

🔧 Changing Hotkeys:
1. Go to Settings > Edit Settings menu
2. Open "Input & Cursor" tab
3. Write new hotkey combination
4. Click Save Settings button

📝 Hotkey Formats:
• ctrl+shift+f (Ctrl, Shift, F together)
• alt+s (Alt + S)
• ctrl+alt+c (Ctrl, Alt, C together)
• f1, f2, f3... (Function keys)

⚠️ Important Notes:
• Be careful not to conflict with system hotkeys
• Invalid combinations may cause errors
• Changes take effect immediately""",
        'tesseract_help_title': "🔧 Tesseract OCR Installation Guide",
        'tesseract_windows': "Windows Installation",
        'tesseract_linux': "Linux Installation",
        'official_website': "🌐 Official Website",
        'windows_download': "💾 Download Windows",
        'installation_complete': "✅ Installation Complete",
        'restart_fadim': "Restart FADIM to test OCR functionality!",

        # About window
        'about_title': "ℹ️ About FADIM",
        'version': "Version: {version}",
        'update_check_manual': "🔄 Check Updates",
        'up_to_date': "✅ Up to Date",
        'up_to_date_message': "FADIM is already up to date.\n\nCurrent version: {version}",
        'update_check_error': "❌ Error",
        'update_check_failed': "Update check failed:\n{error}",
        'checking_updates': "🔄 Checking for updates...",

        # System tray
        'tray_show': "Show",
        'tray_capture': "Capture Screen",
        'tray_settings': "Settings",
        'tray_exit': "Exit",
        'app_title_en': "FADIM",
        
        # Error messages
        'keyboard_not_found': "⚠️ Keyboard library not found, shortcuts disabled",
        'hotkeys_active': "✅ Hotkeys active: {hotkey} (capture)",
        'hotkey_error': "❌ Error setting hotkey: {error}",
        
        # Missing header texts
        'status_ready': "✅ Ready",
        'limited_mode': "⚠️ Limited Mode",
        'limited_mode_message': "Tesseract OCR not found. Only GIF recording feature available.",
        'app_already_running': "FADIM is already running!",

        # Missing messages
        'update_available_title': "🔄 New Version Available",
        'update_available_message': "A new version of FADIM is available!\n\nCurrent version: {current_version}\nNew version: {latest_version}\n\nWould you like to open the download page?",
        'limited_mode': "ℹ️ Limited Mode",
        'limited_mode_message': "FADIM will work with these features:\n\n✅ GIF recording\n✅ Screenshots\n❌ OCR text reading\n\nRestart FADIM after installing Tesseract!"
    },

    'ar': {
        # عناصر الواجهة الرئيسية
        'title': "فاديم - الصورة إلى نص",
        'language_selection': "🌐 لغة الواجهة:",
        'ocr_language': "🔤 لغة OCR:",
        'help_text': "ℹ️ مساعدة:",
        'help_hotkey': "الاختصار: {hotkey}",
        'ocr_result': "📝 نتيجة OCR",
        'operations': "🎯 العمليات",
        'close_app': "❌ إغلاق",

        # اللغات
        'lang_turkish': "التركية",
        'lang_english': "الإنجليزية",
        'lang_arabic': "العربية",

        # الأزرار
        'take_screenshot': "📷 التقط لقطة شاشة",
        'open_file': "📂 فتح ملف",
        'stop_gif': "⏹️ إيقاف GIF",
        'save_txt': "💾 حفظ TXT",
        'save_docx': "📄 حفظ DOCX",
        'clear_text': "🗑️ مسح النص",
        'copy_text': "📋 نسخ النص",

        # عناصر القائمة
        'menu_file': "ملف",
        'menu_open_image': "فتح صورة",
        'menu_show_records': "عرض السجلات",
        'menu_settings': "إعدادات",
        'menu_edit_settings': "تعديل الإعدادات",
        'menu_cleanup': "تنظيف",
        'menu_help': "مساعدة",
        'menu_usage_guide': "دليل الاستخدام",
        'menu_tesseract_install': "تثبيت Tesseract",
        'menu_update_check': "فحص التحديثات",
        'menu_website': "الموقع",
        'menu_about': "حول",

        # الإعدادات
        'settings_title': "⚙️ إعدادات فاديم",
        'settings_general': "عام",
        'settings_input_cursor': "الإدخال والمؤشر",
        'settings_advanced': "متقدم",
        'default_ocr_lang': "لغة OCR الافتراضية",
        'capture_mode_settings': "وضع الالتقاط",
        'sound_settings': "إعدادات الصوت",
        'click_sound': "صوت النقر",
        'mouse_cursor': "مؤشر الفأرة",
        'show_cursor': "إظهار المؤشر",
        'cursor_trail': "أثر المؤشر",
        'hotkeys': "الاختصارات",
        'capture_hotkey': "اختصار الالتقاط:",
        'esc_note': "ملاحظة: مفتاح ESC يوقف تسجيل GIF",
        'system_tray': "شريط النظام",
        'minimize_to_tray': "تصغير إلى الشريط",
        'data_management': "إدارة البيانات",
        'clear_all_records': "مسح جميع السجلات",
        'save_settings': "💾 حفظ الإعدادات",
        'settings_saved': "✅ تم حفظ الإعدادات",

        # اختيار الوضع
        'capture_mode': "📸 وضع الالتقاط",
        'ocr_mode': "🔤 وضع OCR",
        'gif_mode': "🎥 وضع GIF",
        'screenshot_mode': "📷 وضع لقطة الشاشة",
        'quick_mode_selection': "⚡ اختيار الوضع السريع",
        'quick_ocr': "⚡ OCR سريع",
        'quick_gif': "⚡ GIF سريع",
        'quick_screenshot': "⚡ لقطة سريعة",
        'active_mode': "نشط: {mode}",
        'mode_ocr': "وضع OCR",
        'mode_gif': "وضع GIF",
        'mode_screenshot': "وضع لقطة الشاشة",
        'mode_unknown': "وضع غير معروف",

        # خيارات GIF
        'gif_options': "🎥 خيارات GIF",
        'quality': "الجودة:",
        'duration': "المدة (ث):",
        'fps': "FPS:",
        'select_region': "🎯 تحديد المنطقة",

        # تحرير النص
        'font_size': "الخط:",
        'alignment': "المحاذاة:",
        'align_left': "يسار",
        'align_center': "وسط",
        'align_right': "يمين",
        'style': "النمط:",
        'bold': "عريض",
        'italic': "مائل",

        # رسائل الحالة
        'status_ready': "جاهز (Ctrl+Shift+F: لقطة شاشة)",
        'status_no_text': "لا يوجد نص",
        'language_selected': "🌐 تم اختيار اللغة: {lang}",
        'language_update_error': "❌ فشل تحديث اللغة: {error}",
        'text_loaded': "✅ تم تحميل النص: {timestamp}",
        'gif_recording_active': "🔴 تسجيل GIF نشط",
        'region_selected': "تم تحديد المنطقة: {width}x{height} بكسل",
        'region_cancelled': "تم إلغاء تحديد المنطقة",
        'hotkeys_active': "✅ الاختصارات نشطة: {hotkey} (التقاط)",
        'keyboard_not_found': "⚠️ لم يتم العثور على مكتبة لوحة المفاتيح، الاختصارات معطلة",
        'hotkey_error': "❌ خطأ في تعيين الاختصار: {error}",
        'capture_starting': "جاري التقاط لقطة الشاشة...",
        'capture_error': "خطأ في لقطة الشاشة: {error}",
        'gif_recording_starting': "بدء تسجيل GIF...",
        'gif_saved': "تم حفظ GIF: {filename}",
        'gif_stop_requested': "تم إرسال طلب إيقاف GIF...",
        'gif_stopped_button': "تم إيقاف تسجيل GIF عبر الزر...",
        'no_active_gif': "لم يتم العثور على تسجيل GIF نشط",
        'region_selected_size': "تم تحديد المنطقة: {width}x{height} بكسل",
        'region_cancelled_selection': "تم إلغاء تحديد المنطقة",
        'mode_selected': "✅ تم اختيار {mode}",
        'mode_change_error': "❌ فشل تغيير الوضع: {error}",
        'text_copied': "تم نسخ النص إلى الحافظة",
        'file_saved': "تم حفظ الملف: {path}",
        'arabic_detected': "تم اكتشاف النص العربي ومحاذاته لليمين",
        'text_processed_saved': "✅ تم استخراج النص وحفظه (ID: {id}) - {status}",
        'text_processed_error': "❌ تم استخراج النص ولكن لا يمكن حفظه في قاعدة البيانات: {error}",
        'image_clipboard_success': "تم نسخ الصورة إلى الحافظة",
        'image_clipboard_failed': "فشل نسخ الصورة",

        # الإحصائيات
        'stats_format': "الأسطر: {lines} | الكلمات: {words} | الأحرف: {chars}",
        'stats_lines': "الأسطر",
        'stats_words': "الكلمات",
        'stats_characters': "الأحرف",

        # نافذة السجلات
        'records_title': "📊 سجلات OCR",
        'records_list': "قائمة السجلات",
        'screenshot_preview': "معاينة لقطة الشاشة",
        'records_date': "التاريخ",
        'records_source': "المصدر",
        'records_language': "اللغة",
        'records_preview': "معاينة",
        'preview_select': "اختر سجلاً للمعاينة",
        'preview_not_found': "لقطة الشاشة غير موجودة",
        'preview_error': "خطأ في المعاينة",
        'delete_selected': "🗑️ حذف المحدد",
        'close': "❌ إغلاق",
        'total_records': "إجمالي السجلات: {count}",
        'record_count_error': "لا يمكن الحصول على عدد السجلات",
        'confirm_delete_record': "هل أنت متأكد من أنك تريد حذف السجل المحدد؟",
        'record_deleted': "تم حذف السجل.",
        'select_record_to_delete': "يرجى تحديد سجل للحذف",
        'record_delete_error': "خطأ في حذف السجل",

        # التنظيف
        'cleanup_title': "🧹 تنظيف الملفات",
        'disk_usage': "استخدام القرص",
        'total_size': "الحجم الإجمالي: {size} ميجابايت",
        'file_count': "عدد الملفات: {count}",
        'cleanup_settings': "إعدادات التنظيف",
        'days_to_keep': "الأيام للاحتفاظ:",
        'max_files': "العدد الأقصى للملفات:",
        'save_cleanup_settings': "💾 حفظ الإعدادات",
        'start_cleanup': "🧹 بدء التنظيف",
        'delete_all': "🗑️ حذف الكل",
        'cleanup_started': "بدأ التنظيف!\nسيتم تنظيف الملفات الأقدم من {days} أيام.",
        'cleanup_completed': "✅ اكتمل التنظيف!\n🗑️ الملفات المحذوفة: {cleaned}\n💾 المساحة المحفوظة: {saved} ميجابايت",
        'dangerous_operation': "⚠️ عملية خطيرة",
        'delete_all_warning': "ستقوم هذه العملية بحذف جميع الملفات والسجلات نهائياً!\nلا يمكن التراجع عن هذا الإجراء. هل أنت متأكد من المتابعة؟",
        'all_data_deleted': "✅ تم حذف جميع البيانات!\n🗑️ الملفات المحذوفة: {count}",
        'cleanup_settings_saved': "تم حفظ إعدادات التنظيف!",
        'cleanup_settings_error': "لا يمكن حفظ الإعدادات: {error}",
        'delete_error': "خطأ أثناء الحذف: {error}",
        'auto_cleanup': "🧹 التنظيف التلقائي: تم حذف {count} ملف",

        # رسائل حالة التسجيل
        'recording_status': "🔴 جاري التسجيل...\nاضغط ESC للإيقاف",

        # رسائل الخطأ
        'error': "خطأ",
        'warning': "تحذير",
        'success': "نجح",
        'confirm': "تأكيد",
        'ocr_error': "خطأ OCR",
        'ocr_failed_tesseract': "❌ فشل OCR - تحقق من Tesseract",
        'ocr_failed_general': "❌ خطأ عام في OCR",
        'unexpected_error': "خطأ غير متوقع",
        'no_text_to_save': "لا يوجد نص للحفظ",
        'app_already_running': "فاديم يعمل بالفعل!",
        'exit_title': "خروج",
        'confirm_exit': "هل أنت متأكد من أنك تريد الخروج من فاديم؟",
        'confirm_clear_all': "هل أنت متأكد من أنك تريد حذف جميع السجلات؟ لا يمكن التراجع عن هذا الإجراء.",
        'records_cleared': "تم مسح جميع السجلات.",

        # التلميحات
        'tooltip_lang_combo': "اختر اللغة لمعالجة OCR",
        'tooltip_font_size': "ضبط حجم النص",
        'tooltip_align_left': "محاذاة النص لليسار",
        'tooltip_align_center': "محاذاة النص للوسط",
        'tooltip_align_right': "محاذاة النص لليمين",
        'tooltip_bold': "جعل النص عريضاً",
        'tooltip_italic': "جعل النص مائلاً",
        'tooltip_gif_quality': "اختر جودة GIF",
        'tooltip_gif_duration': "تعيين مدة تسجيل GIF",
        'tooltip_gif_fps': "تعيين الإطارات في الثانية",
        'tooltip_select_region': "تحديد منطقة مخصصة للتسجيل",
        'tooltip_ocr_mode': "قراءة النص التلقائية من لقطات الشاشة",
        'tooltip_gif_mode': "تسجيل GIF متحرك",
        'tooltip_screenshot_mode': "التقاط لقطات الشاشة فقط",
        'tooltip_take_screenshot': "التقط لقطة شاشة ومعالجة",
        'tooltip_open_file': "فتح ملف صورة من الكمبيوتر",
        'tooltip_stop_gif': "إيقاف تسجيل GIF الجاري",
        'tooltip_save_txt': "حفظ النص كملف TXT",
        'tooltip_save_docx': "حفظ النص كمستند Word",
        'tooltip_clear_text': "مسح منطقة النص",
        'tooltip_copy_text': "نسخ النص إلى الحافظة",
        'tooltip_close_app': "إغلاق فاديم",
        'tooltip_docs_folder': "فتح مجلد المستندات",
        'tooltip_gif_folder': "فتح مجلد GIF",
        'tooltip_website': "فتح موقع فاديم",
        'tooltip_main_site': "فتح الموقع الرئيسي",

        # نافذة المساعدة
        'help_title': "📖 دليل مستخدم فاديم",
        'help_basic_usage': "الاستخدام الأساسي",
        'help_shortcuts': "اختصارات المفاتيح",
        'help_shortcuts_content': """⌨️ اختصارات المفاتيح

🎯 الاختصارات الرئيسية:
• Ctrl+Shift+F: التقاط الشاشة (افتراضي)
• ESC: إيقاف تسجيل GIF

🔧 تغيير الاختصارات:
1. اذهب إلى الإعدادات > تعديل الإعدادات
2. افتح تبويب "الإدخال والمؤشر"
3. اكتب تركيبة اختصار جديدة
4. اضغط على زر حفظ الإعدادات

📝 تنسيقات الاختصارات:
• ctrl+shift+f (Ctrl, Shift, F معاً)
• alt+s (Alt + S)
• ctrl+alt+c (Ctrl, Alt, C معاً)
• f1, f2, f3... (مفاتيح الوظائف)

⚠️ ملاحظات مهمة:
• احذر من التعارض مع اختصارات النظام
• التركيبات غير الصحيحة قد تسبب أخطاء
• التغييرات تصبح فعالة فوراً""",
        'tesseract_help_title': "🔧 دليل تثبيت Tesseract OCR",
        'tesseract_windows': "تثبيت Windows",
        'tesseract_linux': "تثبيت Linux",
        'official_website': "🌐 الموقع الرسمي",
        'windows_download': "💾 تحميل Windows",
        'installation_complete': "✅ اكتمل التثبيت",
        'restart_fadim': "أعد تشغيل فاديم لاختبار وظيفة OCR!",

        # نافذة حول
        'about_title': "ℹ️ حول فاديم",
        'version': "الإصدار: {version}",
        'update_check_manual': "🔄 فحص التحديثات",
        'up_to_date': "✅ محدث",
        'up_to_date_message': "فاديم محدث بالفعل.\n\nالإصدار الحالي: {version}",
        'update_check_error': "❌ خطأ",
        'update_check_failed': "فشل فحص التحديث:\n{error}",
        'checking_updates': "🔄 جاري فحص التحديثات...",

        # شريط النظام
        'tray_show': "إظهار",
        'tray_capture': "التقاط الشاشة",
        'tray_settings': "الإعدادات",
        'tray_exit': "خروج",
        'app_title_en': "فاديم",
        
        # رسائل الخطأ
        'keyboard_not_found': "⚠️ مكتبة لوحة المفاتيح غير موجودة، الاختصارات معطلة",
        'hotkeys_active': "✅ الاختصارات نشطة: {hotkey} (التقاط)",
        'hotkey_error': "❌ خطأ في تعيين الاختصار: {error}",
        
        # نصوص العناوين المفقودة
        'status_ready': "✅ جاهز",
        'limited_mode': "⚠️ وضع محدود",
        'limited_mode_message': "لم يتم العثور على Tesseract OCR. متاح فقط ميزة تسجيل GIF.",
        'app_already_running': "فاديم يعمل بالفعل!",

        # الرسائل المفقودة
        'update_available_title': "🔄 إصدار جديد متاح",
        'update_available_message': "إصدار جديد من فاديم متاح!\n\nالإصدار الحالي: {current_version}\nالإصدار الجديد: {latest_version}\n\nهل تريد فتح صفحة التحميل؟",
        'limited_mode': "ℹ️ الوضع المحدود",
        'limited_mode_message': "سيعمل فاديم بهذه الميزات:\n\n✅ تسجيل GIF\n✅ لقطات الشاشة\n❌ قراءة نص OCR\n\nأعد تشغيل فاديم بعد تثبيت Tesseract!"
    }
}

def get_text(key, language='tr', **kwargs):
    """
    Belirtilen dil ve anahtar için metni döndürür
    Args:
        key: Anahtar kelime
        language: Dil kodu (tr, en, ar)
        **kwargs: Format parametreleri
    """
    if language not in LANGUAGES:
        language = 'tr'  # Varsayılan dil

    text = LANGUAGES[language].get(key, LANGUAGES['tr'].get(key, f"[{key}]"))

    # Format parametrelerini uygula
    try:
        return text.format(**kwargs)
    except:
        return text

def get_available_languages():
    """Mevcut dillerin listesini döndürür"""
    return list(LANGUAGES.keys())

def get_language_code(language_name):
    """Dil adından dil kodunu döndürür"""
    name_to_code = {
        'Türkçe': 'tr',
        'English': 'en', 
        'العربية': 'ar'
    }
    return name_to_code.get(language_name, 'tr')