from sqlalchemy import create_engine, Column, Integer, String, Text, DateTime, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from datetime import datetime

Base = declarative_base()

class TextRecord(Base):
    __tablename__ = 'text_records'

    id = Column(Integer, primary_key=True)
    text = Column(String)
    source = Column(String)  # screenshot, pdf, or image
    timestamp = Column(DateTime, default=datetime.now)
    language = Column(String)

class DatabaseManager:
    def __init__(self):
        try:
            home_dir = os.path.expanduser('~')
            db_path = os.path.join(home_dir, 'Documents', 'fadim', 'database.db')
            os.makedirs(os.path.dirname(db_path), exist_ok=True)

            # SQLite veritabanı URL'ini düzelt
            self.db_path = db_path
            self.engine = create_engine(f'sqlite:///{db_path}', echo=False)
            Base.metadata.create_all(self.engine)
            Session = sessionmaker(bind=self.engine)
            self.session = Session()

            # Veritabanı bağlantısını test et
            self._test_connection()
            print(f"✅ Veritabanı başarıyla bağlandı: {db_path}")

        except Exception as e:
            print(f"❌ Veritabanı bağlantı hatası: {e}")
            raise

    def _test_connection(self):
        """Veritabanı bağlantısını test et"""
        try:
            self.session.execute(text("SELECT 1"))
            print("✅ Veritabanı bağlantısı başarılı")
        except Exception as e:
            print(f"❌ Veritabanı bağlantı hatası: {e}")
            raise Exception(f"Veritabanı bağlantı testi başarısız: {e}")

    def save_text(self, text, source='screenshot', language='auto'):
        try:
            if not text or len(text.strip()) == 0:
                raise ValueError("Boş metin kaydedilemez")

            # Veritabanı bağlantısını test et
            self._test_connection()

            record = TextRecord(text=text, source=source, language=language)
            self.session.add(record)
            self.session.commit()

            print(f"✅ Metin veritabanına kaydedildi: ID={record.id}, Uzunluk={len(text)} karakter, Dil={language}")
            return record.id

        except Exception as e:
            try:
                self.session.rollback()
            except:
                pass
            error_msg = f"Veritabanı kayıt hatası: {e}"
            print(f"❌ {error_msg}")
            # Bağlantı sorunu varsa yeniden bağlanmayı dene
            if "database" in str(e).lower() or "connection" in str(e).lower():
                try:
                    self._reconnect()
                    # Tekrar dene
                    record = TextRecord(text=text, source=source, language=language)
                    self.session.add(record)
                    self.session.commit()
                    print(f"✅ Yeniden bağlantı sonrası kayıt başarılı: ID={record.id}")
                    return record.id
                except Exception as retry_error:
                    print(f"❌ Yeniden deneme başarısız: {retry_error}")
            raise Exception(error_msg)

    def get_all_records(self):
        return self.session.query(TextRecord).order_by(TextRecord.timestamp.desc()).all()

    def delete_record(self, record_id):
        """Belirli bir kaydı sil"""
        record = self.session.query(TextRecord).filter(TextRecord.id == record_id).first()
        if record:
            self.session.delete(record)
            self.session.commit()
            return True
        return False

    def _reconnect(self):
        """Veritabanı bağlantısını yeniden kur"""
        try:
            self.session.close()
            Session = sessionmaker(bind=self.engine)
            self.session = Session()
            self._test_connection()
            print("✅ Veritabanı yeniden bağlandı")
        except Exception as e:
            print(f"❌ Veritabanı yeniden bağlantı hatası: {e}")
            raise

    def clear_all_records(self):
        """Tüm kayıtları sil"""
        self.session.query(TextRecord).delete()
        self.session.commit()