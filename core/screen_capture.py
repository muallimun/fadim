
import pyautogui
import tkinter as tk
from PIL import ImageGrab
import os
import sys
import platform
from datetime import datetime

def capture_screen_region(play_sound=True, show_cursor=False):
    """
    Captures a selected region of the screen
    Args:
        play_sound: Boolean, ses efekti çalınıp çalınmayacağını belirler
        show_cursor: Boolean, mouse imlecinin gösterilip gösterilmeyeceğini belirler
    Returns:
        Path to the saved screenshot
    """
    # Replit ortamında ekran yakalama sınırlı
    if 'REPL_ID' in os.environ:
        print("⚠️ Replit ortamında ekran yakalama özelliği sınırlıdır")
        return None
        
    try:
        # Belgeler/fadim/screenshots dizinini oluştur
        home_dir = os.path.expanduser('~')
        screenshots_dir = os.path.join(home_dir, 'Documents', 'fadim', 'screenshots')
        os.makedirs(screenshots_dir, exist_ok=True)
        
        # Hide the main window temporarily
        root = None
        screen = None
        canvas = None
        
        root = tk.Tk()
        root.withdraw()
        
        # Create a fullscreen transparent window
        screen = tk.Toplevel(root)
        screen.attributes('-fullscreen', True, '-alpha', 0.3, '-topmost', True)
        screen.configure(bg='gray')
        
        # Variables to store coordinates
        start_x = tk.IntVar()
        start_y = tk.IntVar()
        end_x = tk.IntVar()
        end_y = tk.IntVar()
        drawing = tk.BooleanVar(value=False)
        
        # Canvas for drawing selection rectangle
        canvas = tk.Canvas(screen, cursor="cross")
        canvas.pack(fill=tk.BOTH, expand=True)
        
        def on_press(event):
            drawing.set(True)
            start_x.set(event.x)
            start_y.set(event.y)
            
        def on_motion(event):
            if drawing.get():
                canvas.delete("selection")
                # Gölge/fill alanı
                canvas.create_rectangle(start_x.get(), start_y.get(), 
                                     event.x, event.y, outline="red", 
                                     fill="white", stipple="gray25",
                                     width=4, tags="selection")
                # Kontur
                canvas.create_rectangle(start_x.get(), start_y.get(), 
                                     event.x, event.y, outline="red", 
                                     width=3, tags="selection")
                
        def on_release(event):
            end_x.set(event.x)
            end_y.set(event.y)
            
            # Ses efekti çalma (ayarlara göre)
            if play_sound:
                try:
                    import pygame
                    pygame.mixer.pre_init(frequency=22050, size=-16, channels=2, buffer=512)
                    pygame.mixer.init()
                    # PyInstaller destekli yol çözümü
                    if hasattr(sys, '_MEIPASS'):
                        base_path = sys._MEIPASS
                    else:
                        base_path = os.path.abspath(".")
                    click_sound_path = os.path.join(base_path, 'core', 'click.mp3')
                    if os.path.exists(click_sound_path):
                        click_sound = pygame.mixer.Sound(click_sound_path)
                        click_sound.play()
                    else:
                        # Sistem bip sesi alternatifi
                        print('\a')  # Terminal bip sesi
                except (ImportError, Exception) as e:
                    # Ses çalamazsa sistem bip sesi
                    print('\a')
                    print(f"Ses efekti hatası: {e}")
            
            screen.destroy()
            root.destroy()
        
        canvas.bind("<Button-1>", on_press)
        canvas.bind("<B1-Motion>", on_motion)
        canvas.bind("<ButtonRelease-1>", on_release)
        
        # Wait for the window to be destroyed
        root.wait_window(screen)
        
        # Capture the selected region
        x1, y1 = min(start_x.get(), end_x.get()), min(start_y.get(), end_y.get())
        x2, y2 = max(start_x.get(), end_x.get()), max(start_y.get(), end_y.get())
        
        # PyAutoGUI mouse imleci ayarını güncelle
        if show_cursor:
            pyautogui.screenshot = lambda region=None: ImageGrab.grab(bbox=region, include_layered_windows=False)
        
        screenshot = ImageGrab.grab(bbox=(x1, y1, x2, y2))
        
        # Generate filename with timestamp
        filename = os.path.join(screenshots_dir, f"capture_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png")
        screenshot.save(filename)
        
        # Ekran görüntüsünü panoya kopyala
        try:
            if platform.system() == 'Windows':
                try:
                    import win32clipboard
                    import io
                    
                    def copy_image_to_clipboard_windows(image):
                        output = io.BytesIO()
                        image.convert('RGB').save(output, 'BMP')
                        data = output.getvalue()[14:]  # BMP header'ı atla
                        output.close()
                        
                        win32clipboard.OpenClipboard()
                        win32clipboard.EmptyClipboard()
                        win32clipboard.SetClipboardData(win32clipboard.CF_DIB, data)
                        win32clipboard.CloseClipboard()
                    
                    copy_image_to_clipboard_windows(screenshot)
                    print("✅ Ekran görüntüsü panoya kopyalandı (Windows)")
                    
                except ImportError:
                    print("⚠️ win32clipboard modülü bulunamadı")
                except Exception as e:
                    print(f"⚠️ Windows panoya kopyalama hatası: {e}")
                    
            elif platform.system() == 'Darwin':  # macOS
                try:
                    import subprocess
                    temp_path = os.path.join(os.path.dirname(filename), 'temp_screenshot.png')
                    screenshot.save(temp_path)
                    subprocess.run(['osascript', '-e', 
                                  f'set the clipboard to POSIX file "{temp_path}"'])
                    os.remove(temp_path)
                    print("✅ Ekran görüntüsü panoya kopyalandı (macOS)")
                except Exception as e:
                    print(f"⚠️ macOS panoya kopyalama hatası: {e}")
                    
            else:  # Linux
                try:
                    import subprocess
                    temp_path = os.path.join(os.path.dirname(filename), 'temp_screenshot.png')
                    screenshot.save(temp_path)
                    subprocess.run(['xclip', '-selection', 'clipboard', '-t', 'image/png', '-i', temp_path])
                    os.remove(temp_path)
                    print("✅ Ekran görüntüsü panoya kopyalandı (Linux)")
                except Exception as e:
                    print(f"⚠️ Linux panoya kopyalama hatası: {e}")
        
        except Exception as e:
            print(f"⚠️ Panoya kopyalama hatası: {e}")
        
        return filename
        
    except Exception as e:
        print(f"Error capturing screen: {str(e)}")
        # Pencereyi güvenli şekilde kapat
        try:
            if screen and screen.winfo_exists():
                screen.destroy()
        except:
            pass
        try:
            if root and root.winfo_exists():
                root.destroy()
        except:
            pass
        return None
