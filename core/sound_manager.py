
import os
import threading
import time

try:
    import pygame
    PYGAME_AVAILABLE = True
except ImportError:
    PYGAME_AVAILABLE = False

try:
    import playsound
    PLAYSOUND_AVAILABLE = True
except ImportError:
    PLAYSOUND_AVAILABLE = False

if not PYGAME_AVAILABLE and not PLAYSOUND_AVAILABLE:
    print("Ses çalmak için pygame veya playsound kütüphanesi bulunamadı")

class SoundManager:
    def __init__(self):
        self.enabled = True
        self.sound_files = {
            'capture': 'core/click.mp3',
            'recording_start': 'core/recording_start.mp3',
            'recording_stop': 'core/recording_stop.mp3',
            'success': 'core/success.mp3',
            'error': 'core/error.mp3'
        }
        self.init_pygame()
        
    def init_pygame(self):
        """Pygame ses sistemini başlat"""
        if PYGAME_AVAILABLE:
            try:
                pygame.mixer.init(frequency=22050, size=-16, channels=2, buffer=512)
                return True
            except:
                return False
        return False
        
    def create_default_sounds(self):
        """Varsayılan ses dosyalarını oluştur (basit beep'ler)"""
        if not PYGAME_AVAILABLE:
            return
            
        import numpy as np
        import wave
        
        def create_beep(filename, frequency, duration, volume=0.3):
            sample_rate = 22050
            frames = int(duration * sample_rate)
            arr = np.zeros(frames)
            
            for i in range(frames):
                arr[i] = volume * np.sin(2 * np.pi * frequency * i / sample_rate)
                
            # Fade in/out
            fade_frames = int(0.01 * sample_rate)
            for i in range(fade_frames):
                arr[i] *= i / fade_frames
                arr[frames - 1 - i] *= i / fade_frames
                
            arr = (arr * 32767).astype(np.int16)
            
            with wave.open(filename, 'w') as wav_file:
                wav_file.setnchannels(1)
                wav_file.setsampwidth(2)
                wav_file.setframerate(sample_rate)
                wav_file.writeframes(arr.tobytes())
        
        try:
            os.makedirs('core', exist_ok=True)
            
            # Kayıt başlama sesi (yükselen ton)
            if not os.path.exists('core/recording_start.wav'):
                create_beep('core/recording_start.wav', 800, 0.2)
                
            # Kayıt durdurma sesi (alçalan ton)
            if not os.path.exists('core/recording_stop.wav'):
                create_beep('core/recording_stop.wav', 400, 0.3)
                
            # Başarı sesi (çift beep)
            if not os.path.exists('core/success.wav'):
                create_beep('core/success.wav', 1000, 0.1)
                
            # Hata sesi (düşük ton)
            if not os.path.exists('core/error.wav'):
                create_beep('core/error.wav', 200, 0.5)
                
        except Exception as e:
            print(f"Varsayılan sesler oluşturulamadı: {e}")
    
    def play_sound(self, sound_type, async_play=True):
        """Ses çal"""
        if not self.enabled:
            return
            
        def play_worker():
            try:
                sound_file = self.sound_files.get(sound_type)
                if not sound_file:
                    return
                    
                # Önce .mp3, sonra .wav dene
                for ext in ['.mp3', '.wav']:
                    file_path = sound_file.replace('.mp3', ext)
                    if os.path.exists(file_path):
                        self._play_file(file_path)
                        return
                        
                # Dosya bulunamadıysa varsayılan ses çal
                self._play_system_beep(sound_type)
                
            except Exception as e:
                print(f"Ses çalma hatası: {e}")
                
        if async_play:
            threading.Thread(target=play_worker, daemon=True).start()
        else:
            play_worker()
            
    def _play_file(self, file_path):
        """Dosya çal"""
        if PYGAME_AVAILABLE:
            try:
                pygame.mixer.music.load(file_path)
                pygame.mixer.music.play()
                # Ses bitene kadar bekle
                while pygame.mixer.music.get_busy():
                    time.sleep(0.1)
            except:
                pass
        elif PLAYSOUND_AVAILABLE:
            try:
                playsound.playsound(file_path, block=False)
            except:
                pass
                
    def _play_system_beep(self, sound_type):
        """Sistem beep'i çal"""
        try:
            import winsound
            
            beep_patterns = {
                'capture': (800, 100),
                'recording_start': (1000, 200),
                'recording_stop': (600, 300),
                'success': (1200, 150),
                'error': (400, 500)
            }
            
            frequency, duration = beep_patterns.get(sound_type, (800, 100))
            winsound.Beep(frequency, duration)
            
        except ImportError:
            # Linux/Mac için
            print('\a')  # Terminal beep
            
    def set_enabled(self, enabled):
        """Sesleri etkinleştir/devre dışı bırak"""
        self.enabled = enabled
        
    def test_sounds(self):
        """Tüm sesleri test et"""
        for sound_type in self.sound_files.keys():
            print(f"Test ediliyor: {sound_type}")
            self.play_sound(sound_type, async_play=False)
            time.sleep(0.5)
