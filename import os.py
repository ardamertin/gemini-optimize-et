import os
from google import genai
from google.genai import errors, types


def kod_optimize_et(spagetti_kod: str) -> None:
    os.system("cls" if os.name == "nt" else "clear")

    print("=" * 75)
    print(" YAPAY ZEKA DESTEKLİ KOD İYİLEŞTİRME VE OPTİMİZASYON ".center(75))
    print("=" * 75)

    # API anahtarını ortam değişkeninden al (veya doğrudan tanımla)
    api_anahtari = "api_keyiniz"

    if not api_anahtari:
        print("\n[HATA] GEMINI_API_KEY tanımlanmamış!")
        return

    sistem_mesaji = """
    Sen kıdemli bir Yazılım Mimarı ve Performans Uzmanısın.

    Kullanıcının gönderdiği kötü yazılmış (spagetti)
    Python kodunu analiz et.

    1. Değişken isimlerini anlamlı hale getir (Clean Code).
    2. Algoritmanın çalışma hızını iyileştir.
       Örneğin O(n^2) yerine mümkünse O(n) kullan.
    3. Type Hint (Tip belirteçleri) ekle.
    4. Kodun mevcut işlevselliğini koru.
    5. Gereksiz döngüleri ortadan kaldır.

    Çıktın KESİNLİKLE sadece düzeltilmiş Python kodu olmalıdır.
    Ek açıklama veya Markdown yazma.
    """

    print("\n[AŞAMA 1] OPTİMİZE EDİLECEK SPAGETTİ KOD SİSTEME ALINDI...")
    print("\n[AŞAMA 2] REFACTORING İÇİN YAPAY ZEKAYA BAĞLANILIYOR...\n")

    try:
        # gemini istemcisini oluştur
        with genai.Client(api_key=api_anahtari) as client:
            # gemini api isteğini gönder
            response = client.models.generate_content(
                model="gemini-3.8-flash",
                contents=spagetti_kod,
                config=types.GenerateContentConfig(
                    system_instruction=sistem_mesaji,
                    temperature=0.2,
                ),
            )

        # Yapay zekanın ürettiği kod
        temiz_kod = response.text

        if not temiz_kod:
            print("\n[HATA] Yapay zeka boş cevap döndürdü.")
            return

        print("=" * 75)
        print(" OPTİMİZE EDİLMİŞ KOD ".center(75))
        print("=" * 75)
        print(temiz_kod)

    except errors.APIError as e:
        print(f"\n[API HATASI] Gemini servisi hata döndürdü: {e}")
    except Exception as e:
        print(f"\n[BEKLENMEYEN HATA] İşlem sırasında hata oluştu: {e}")


# Kötü yazılmış, iç içe döngüler kullanan spagetti kod
kotu_kod = """
def bul(l):
    r = []
    for i in range(len(l)):
        for j in range(i+1, len(l)):
            if l[i] == l[j] and l[i] not in r:
                r.append(l[i])
    return r
"""

# Programı başlat
if __name__ == "__main__":
    kod_optimize_et(kotu_kod)