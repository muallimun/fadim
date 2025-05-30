

import os
import time
import threading
from datetime import datetime, timedelta
import shutil

class FileManager:
    def __init__(self, config):
        self.config = config
        self.cleanup_settings = config.get('cleanup', {
            'enabled': True,
            'days_to_keep': 30,
            'max_files': 100,
            'auto_cleanup_interval': 24
        })
        
    def get_disk_usage(self):
        """Disk kullanım bilgisi al"""
        try:
            base_dir = os.path.expanduser(self.config['base_directory'])
            total_size = 0
            file_count = 0
            
            for directory in self.config['directories'].values():
                dir_path = os.path.join(base_dir, directory)
                if os.path.exists(dir_path):
                    for root, dirs, files in os.walk(dir_path):
                        for file in files:
                            file_path = os.path.join(root, file)
                            if os.path.exists(file_path):
                                total_size += os.path.getsize(file_path)
                                file_count += 1
            
            return {
                'total_size_mb': round(total_size / (1024 * 1024), 2),
                'file_count': file_count
            }
        except Exception as e:
            print(f"Disk kullanım hesaplama hatası: {e}")
            return {'total_size_mb': 0, 'file_count': 0}
    
    def cleanup_old_files(self, show_progress=False):
        """Eski dosyaları temizle"""
        try:
            base_dir = os.path.expanduser(self.config['base_directory'])
            days_to_keep = self.cleanup_settings['days_to_keep']
            max_files = self.cleanup_settings['max_files']
            
            cutoff_date = datetime.now() - timedelta(days=days_to_keep)
            cleaned_count = 0
            
            # Screenshots klasörünü temizle
            screenshots_dir = os.path.join(base_dir, self.config['directories']['screenshots'])
            if os.path.exists(screenshots_dir):
                files = []
                for file in os.listdir(screenshots_dir):
                    file_path = os.path.join(screenshots_dir, file)
                    if os.path.isfile(file_path):
                        file_time = datetime.fromtimestamp(os.path.getmtime(file_path))
                        files.append((file_path, file_time))
                
                # Tarihe göre sırala (eski -> yeni)
                files.sort(key=lambda x: x[1])
                
                # Eski dosyaları sil
                for file_path, file_time in files:
                    if file_time < cutoff_date:
                        try:
                            os.remove(file_path)
                            cleaned_count += 1
                            if show_progress:
                                print(f"🗑️ Silindi: {os.path.basename(file_path)}")
                        except Exception as e:
                            print(f"Dosya silinemedi {file_path}: {e}")
                
                # Dosya sayısı limiti kontrolü
                remaining_files = [f for f in files if datetime.fromtimestamp(os.path.getmtime(f[0])) >= cutoff_date]
                if len(remaining_files) > max_files:
                    # En eski dosyaları sil
                    excess_files = remaining_files[:len(remaining_files) - max_files]
                    for file_path, _ in excess_files:
                        try:
                            os.remove(file_path)
                            cleaned_count += 1
                            if show_progress:
                                print(f"🗑️ Limit aşımı - silindi: {os.path.basename(file_path)}")
                        except Exception as e:
                            print(f"Dosya silinemedi {file_path}: {e}")
            
            return {'cleaned': cleaned_count}
            
        except Exception as e:
            print(f"Temizlik hatası: {e}")
            return {'cleaned': 0}
    
    def auto_cleanup_thread(self, callback=None):
        """Otomatik temizlik thread'i"""
        def cleanup_worker():
            while True:
                try:
                    if self.cleanup_settings.get('enabled', True):
                        result = self.cleanup_old_files()
                        if result['cleaned'] > 0 and callback:
                            callback(f"🧹 Otomatik temizlik: {result['cleaned']} dosya silindi")
                    
                    # Belirtilen saatte bir tekrar çalış
                    interval_hours = self.cleanup_settings.get('auto_cleanup_interval', 24)
                    time.sleep(interval_hours * 3600)  # saat -> saniye
                    
                except Exception as e:
                    print(f"Otomatik temizlik hatası: {e}")
                    time.sleep(3600)  # Hata durumunda 1 saat bekle
        
        cleanup_thread = threading.Thread(target=cleanup_worker, daemon=True)
        cleanup_thread.start()
