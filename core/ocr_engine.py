import pytesseract
from PIL import Image, ImageFilter, ImageOps, ImageEnhance
import re
import shutil

def is_tesseract_available():
    return shutil.which("tesseract") is not None

# Gerekirse Windows için Tesseract yolu tanımlayın:
# pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def is_arabic_text(text):
    """Metnin Arapça olup olmadığını kontrol et"""
    if not text:
        return False
    arabic_words = re.findall(r'[\u0600-\u06FF]{3,}', text)
    return len(arabic_words) >= 3

def preprocess_image_for_language(image, lang_code):
    """Dile özel görüntü ön işleme"""

    if image.mode != 'RGB':
        image = image.convert('RGB')

    width, height = image.size
    if width < 300 or height < 300:
        scale_factor = max(300/width, 300/height)
        image = image.resize((int(width * scale_factor), int(height * scale_factor)), Image.Resampling.LANCZOS)

    gray = image.convert('L')

    if lang_code == 'ara':
        enhancer = ImageEnhance.Contrast(gray)
        enhanced = enhancer.enhance(1.5)
        sharpener = ImageEnhance.Sharpness(enhanced)
        return sharpener.enhance(1.3)

    elif lang_code == 'tur':
        enhanced = ImageOps.autocontrast(gray, cutoff=2)
        sharpened = enhanced.filter(ImageFilter.SHARPEN)
        return sharpened.filter(ImageFilter.MedianFilter(size=3))

    else:
        enhanced = ImageOps.autocontrast(gray)
        return enhanced.filter(ImageFilter.SHARPEN)

def get_tesseract_config(lang_code):
    """Dile özel Tesseract konfigürasyonu"""
    if lang_code == 'ara':
        return '--psm 3 --oem 3'
    elif lang_code == 'tur':
        return '--psm 3 --oem 3'
    else:
        return '--psm 6 --oem 3'

def enhance_text_result(text, lang_code):
    """OCR sonucunu iyileştir"""
    if not text:
        return text

    text = re.sub(r'\s+', ' ', text.strip())

    if lang_code == 'tur':
        replacements = {
            'i̇': 'i',
            'İ': 'İ',
            'ı': 'ı',
            'I': 'I'
        }
        for old, new in replacements.items():
            text = text.replace(old, new)

    return text

def ocr_image(image_path, lang='tur'):
    """
    Görselden metin çıkarma işlemi
    Args:
        image_path: Görsel dosyasının yolu
        lang: OCR dili (tur, eng, ara)
    Returns:
        tuple: (extracted_text, processed_image) - Her zaman tuple döndürür
    """
    if not is_tesseract_available():
        raise RuntimeError("Tesseract OCR yüklü değil. OCR işlemi yapılamaz.")

    """Gelişmiş OCR işlemi"""
    try:
        raw_image = Image.open(image_path)

        lang_map = {
            "Türkçe": "tur",
            "İngilizce": "eng", 
            "Arapça": "ara"
        }

        selected_lang = lang_map.get(lang.strip(), 'tur')
        print(f"🌐 Seçilen dil: {selected_lang}")

        processed_image = preprocess_image_for_language(raw_image, selected_lang)
        config = get_tesseract_config(selected_lang)
        print(f"⚙️ Tesseract config: {config}")

        best_text = ""

        try:
            text = pytesseract.image_to_string(processed_image, lang=selected_lang, config=config).strip()
            if text:
                best_text = text
                print(f"✅ OCR başarılı: {len(text)} karakter")
        except Exception as e:
            print(f"❌ OCR hatası: {e}")

        if not best_text:
            print("🔄 Alternatif OCR deneniyor...")
            alt_config = config.replace('--psm 6', '--psm 3') if '--psm 6' in config else config
            try:
                text = pytesseract.image_to_string(processed_image, lang=selected_lang, config=alt_config).strip()
                if len(text) > len(best_text):
                    best_text = text
                    print(f"✅ Alternatif başarılı: {len(text)} karakter")
            except Exception as e:
                print(f"❌ Alternatif OCR hatası: {e}")

        if best_text:
            best_text = enhance_text_result(best_text, selected_lang)

            if selected_lang == 'ara' and is_arabic_text(best_text):
                print("🔤 Arapça metin tespit edildi")
            elif selected_lang == 'tur':
                print("🔤 Türkçe metin işlendi")

            # Hem metin hem de görüntü objesini döndür
            return best_text, raw_image
        else:
            # Başarısız durumda da görüntü objesini döndür
            return "OCR işlemi metin algılayamadı. Daha net bir görüntü deneyin.", raw_image

    except Exception as e:
        error_msg = f"OCR işlemi sırasında hata: {str(e)}"
        print(f"❌ {error_msg}")
        # Hata durumunda None döndür
        return error_msg, None