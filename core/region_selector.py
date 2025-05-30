
import tkinter as tk
from tkinter import ttk
import pyautogui
from PIL import Image, ImageTk, ImageDraw

class RegionSelector:
    def __init__(self, callback=None):
        self.callback = callback
        self.selected_region = None
        self.start_x = 0
        self.start_y = 0
        self.end_x = 0
        self.end_y = 0
        self.selecting = False
        
    def show_selector(self):
        """Tam ekran seçici göster"""
        self.root = tk.Toplevel()
        self.root.attributes('-fullscreen', True)
        self.root.attributes('-alpha', 0.3)
        self.root.attributes('-topmost', True)
        self.root.configure(bg='black')
        self.root.overrideredirect(True)
        
        # Ekran görüntüsü al ve arkaplan olarak ayarla
        screenshot = pyautogui.screenshot()
        self.bg_image = ImageTk.PhotoImage(screenshot)
        
        self.canvas = tk.Canvas(self.root, highlightthickness=0)
        self.canvas.pack(fill='both', expand=True)
        self.canvas.create_image(0, 0, anchor='nw', image=self.bg_image)
        
        # Overlay
        overlay = Image.new('RGBA', screenshot.size, (0, 0, 0, 120))
        self.overlay_image = ImageTk.PhotoImage(overlay)
        self.overlay_id = self.canvas.create_image(0, 0, anchor='nw', image=self.overlay_image)
        
        # Event bindings
        self.canvas.bind('<Button-1>', self.start_selection)
        self.canvas.bind('<B1-Motion>', self.update_selection)
        self.canvas.bind('<ButtonRelease-1>', self.end_selection)
        self.root.bind('<Escape>', self.cancel_selection)
        
        # Yardım metni
        help_text = "Alan seçmek için fare ile sürükleyin • ESC: İptal • Enter: Onayla"
        self.canvas.create_text(
            screenshot.width // 2, 50,
            text=help_text,
            fill='white',
            font=('Arial', 16),
            anchor='center'
        )
        
        self.root.focus_set()
        self.root.bind('<Return>', self.confirm_selection)
        
    def start_selection(self, event):
        self.selecting = True
        self.start_x = event.x
        self.start_y = event.y
        self.end_x = event.x
        self.end_y = event.y
        
    def update_selection(self, event):
        if self.selecting:
            self.end_x = event.x
            self.end_y = event.y
            self.draw_selection()
            
    def end_selection(self, event):
        self.selecting = False
        self.end_x = event.x
        self.end_y = event.y
        self.draw_selection()
        
    def draw_selection(self):
        """Seçim dikdörtgenini çiz"""
        self.canvas.delete('selection')
        
        x1, y1 = min(self.start_x, self.end_x), min(self.start_y, self.end_y)
        x2, y2 = max(self.start_x, self.end_x), max(self.start_y, self.end_y)
        
        # Dikdörtgen çiz
        self.canvas.create_rectangle(
            x1, y1, x2, y2,
            outline='red',
            width=2,
            tags='selection'
        )
        
        # Boyut bilgisi
        width = abs(x2 - x1)
        height = abs(y2 - y1)
        size_text = f"{width}x{height} px"
        self.canvas.create_text(
            x1, y1 - 25,
            text=size_text,
            fill='yellow',
            font=('Arial', 12),
            anchor='nw',
            tags='selection'
        )
        
    def confirm_selection(self, event=None):
        """Seçimi onayla"""
        if abs(self.end_x - self.start_x) > 10 and abs(self.end_y - self.start_y) > 10:
            x1, y1 = min(self.start_x, self.end_x), min(self.start_y, self.end_y)
            x2, y2 = max(self.start_x, self.end_x), max(self.start_y, self.end_y)
            self.selected_region = (x1, y1, x2, y2)
            
            if self.callback:
                self.callback(self.selected_region)
                
        self.close_selector()
        
    def cancel_selection(self, event=None):
        """Seçimi iptal et"""
        self.selected_region = None
        if self.callback:
            self.callback(None)
        self.close_selector()
        
    def close_selector(self):
        """Seçiciyi kapat"""
        if hasattr(self, 'root'):
            self.root.destroy()
import tkinter as tk
from PIL import ImageGrab
import time

class RegionSelector:
    def __init__(self, callback=None):
        self.callback = callback
        self.region = None
        
    def show_selector(self):
        """Bölge seçici pencereyi göster"""
        try:
            # Ana pencereyi gizle
            root = tk.Tk()
            root.withdraw()
            
            # Tam ekran overlay pencere
            overlay = tk.Toplevel(root)
            overlay.attributes('-fullscreen', True, '-alpha', 0.3, '-topmost', True)
            overlay.configure(bg='gray')
            
            # Koordinat değişkenleri
            self.start_x = tk.IntVar()
            self.start_y = tk.IntVar()
            self.end_x = tk.IntVar()
            self.end_y = tk.IntVar()
            self.drawing = tk.BooleanVar(value=False)
            
            # Canvas
            canvas = tk.Canvas(overlay, cursor="cross")
            canvas.pack(fill=tk.BOTH, expand=True)
            
            # Yardım metni
            help_text = tk.Label(overlay, text="🎯 Kayıt bölgesini seçin (sürükleyin) | ESC: İptal", 
                               font=('Arial', 12, 'bold'), bg='yellow', fg='black')
            help_text.place(x=10, y=10)
            
            def on_press(event):
                self.drawing.set(True)
                self.start_x.set(event.x)
                self.start_y.set(event.y)
                
            def on_motion(event):
                if self.drawing.get():
                    canvas.delete("selection")
                    # Seçim dikdörtgeni
                    canvas.create_rectangle(self.start_x.get(), self.start_y.get(), 
                                         event.x, event.y, outline="red", 
                                         fill="white", stipple="gray25",
                                         width=3, tags="selection")
                    
                    # Boyut bilgisi
                    width = abs(event.x - self.start_x.get())
                    height = abs(event.y - self.start_y.get())
                    info_text = f"📏 {width} x {height} px"
                    canvas.delete("info")
                    canvas.create_text(event.x + 10, event.y - 10, text=info_text, 
                                     fill="red", font=('Arial', 10, 'bold'), tags="info")
                    
            def on_release(event):
                self.end_x.set(event.x)
                self.end_y.set(event.y)
                
                # Bölgeyi hesapla
                x1 = min(self.start_x.get(), self.end_x.get())
                y1 = min(self.start_y.get(), self.end_y.get())
                x2 = max(self.start_x.get(), self.end_x.get())
                y2 = max(self.start_y.get(), self.end_y.get())
                
                # Minimum boyut kontrolü
                if abs(x2 - x1) < 10 or abs(y2 - y1) < 10:
                    canvas.delete("selection", "info")
                    canvas.create_text(event.x, event.y, text="❌ Çok küçük bölge!", 
                                     fill="red", font=('Arial', 12, 'bold'))
                    return
                
                self.region = (x1, y1, x2, y2)
                overlay.destroy()
                root.destroy()
                
            def on_escape(event):
                self.region = None
                overlay.destroy()
                root.destroy()
                
            canvas.bind("<Button-1>", on_press)
            canvas.bind("<B1-Motion>", on_motion)
            canvas.bind("<ButtonRelease-1>", on_release)
            overlay.bind("<Escape>", on_escape)
            
            overlay.focus_set()  # Klavye odağı
            
            # Pencere kapatılana kadar bekle
            root.wait_window(overlay)
            
            # Callback çağır
            if self.callback:
                self.callback(self.region)
                
            return self.region
            
        except Exception as e:
            print(f"Bölge seçici hatası: {e}")
            return None
