import pyautogui
import imageio
import time
import keyboard
import threading
import math
import os
import sys
from PIL import Image, ImageDraw

# Durdurma bayrağını içeren sınıfı ekleyin
class RecordingStatus:
    def __init__(self):
        self.stop_requested = False
        self._lock = threading.Lock()
        
    def request_stop(self):
        with self._lock:
            self.stop_requested = True
            
    def should_stop(self):
        with self._lock:
            return self.stop_requested

def record_gif(output_path, duration=30, fps=5, region=None, status=None, show_cursor=False, cursor_trail=False, quality='medium'):
    frames = []
    interval = 1 / fps
    end_time = time.time() + duration
    recording_stopped = False
    
    # Kalite ayarları - tüm kalitelerde hareketli kayıt
    quality_settings = {
        'low': {'scale': 0.6, 'fps_multiplier': 1.0, 'compression': 0.3},
        'medium': {'scale': 0.8, 'fps_multiplier': 1.0, 'compression': 0.5},
        'high': {'scale': 1.0, 'fps_multiplier': 1.0, 'compression': 0.8}
    }
    
    current_quality = quality_settings.get(quality, quality_settings['medium'])
    actual_fps = max(3, fps * current_quality['fps_multiplier'])  # Minimum 3 FPS
    interval = 1 / actual_fps

    # Mouse takibi için
    cursor_positions = []
    click_effects = []  # Tıklama efektleri için
    last_click_state = False

    start_time = time.time()
    print(f"GIF kaydı başladı... Süre: {duration}s, ESC ile durdurabilirsiniz.")

    while time.time() < end_time and not recording_stopped:
        elapsed = time.time() - start_time
        remaining = duration - elapsed
        
        # Her 5 saniyede progress göster
        if int(elapsed) % 5 == 0 and elapsed > 0:
            print(f"⏱️ Geçen süre: {int(elapsed)}s / {duration}s")
        # ESC tuşu kontrolü ve status kontrolü
        try:
            if status and status.should_stop():
                print("Kayıt durduruldu (durum kontrolü).")
                recording_stopped = True
                break
            if keyboard.is_pressed('esc'):
                print("Kayıt durduruldu (ESC tuşu).")
                recording_stopped = True
                if status:
                    status.request_stop()
                break
        except Exception as e:
            print(f"Tuş kontrolü hatası: {e}")
            if status and status.should_stop():
                recording_stopped = True
                break
            
        # Bölge belirtilmişse sadece o bölgeyi yakala
        if region:
            x1, y1, x2, y2 = region
            screenshot = pyautogui.screenshot(region=(x1, y1, x2-x1, y2-y1))
        else:
            screenshot = pyautogui.screenshot()
        
        # Kalite ayarlarına göre boyutlandırma
        if current_quality['scale'] < 1.0:
            new_size = (int(screenshot.width * current_quality['scale']), 
                       int(screenshot.height * current_quality['scale']))
            screenshot = screenshot.resize(new_size, Image.Resampling.LANCZOS)
        
        frame = screenshot.convert("RGB")

        # Mouse imleci gösterimi (sadece basit imleç, iz kaldırıldı)
        if show_cursor:
            from PIL import ImageDraw
            draw = ImageDraw.Draw(frame)

            # Mevcut mouse pozisyonu
            try:
                current_pos = pyautogui.position()
                mouse_x, mouse_y = current_pos
                
                # Bölge belirtilmişse mouse pozisyonunu ayarla
                if region:
                    x1, y1, x2, y2 = region
                    # Mouse pozisyonu bölge içindeyse göster
                    if x1 <= mouse_x <= x2 and y1 <= mouse_y <= y2:
                        # Bölgeye göre relatif pozisyon
                        rel_x = mouse_x - x1
                        rel_y = mouse_y - y1
                        draw.polygon([(rel_x, rel_y), (rel_x+10, rel_y+6), (rel_x+6, rel_y+10)], 
                                   fill='white', outline='black', width=1)
                else:
                    # Tam ekran modunda
                    draw.polygon([(mouse_x, mouse_y), (mouse_x+10, mouse_y+6), (mouse_x+6, mouse_y+10)], 
                               fill='white', outline='black', width=1)
                
            except Exception as e:
                # Mouse pozisyonu alınamadıysa devam et
                pass

        frames.append(frame)
        time.sleep(interval)
    
    # Hiç kare yoksa boş bir gif oluşturmasını engelle
    if frames:
        # Kalite ayarlarına göre optimizasyonlar
        gif_params = {
            'format': 'GIF',
            'duration': interval,
            'loop': 0  # Sonsuz döngü
        }
        
        # Yüksek kalitede daha iyi sıkıştırma
        if quality == 'high':
            gif_params['quantizer'] = 'nq'
            gif_params['palettesize'] = 256
        elif quality == 'low':
            gif_params['quantizer'] = 'nq'
            gif_params['palettesize'] = 64
        
        imageio.mimsave(output_path, frames, **gif_params)
        return True
    return False