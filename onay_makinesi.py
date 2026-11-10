#!/usr/bin/env python3
# Resmi Bürokratik Evrak Onay Makinesi v1.0
# Her evrak önce çay demlenir, sonra damgalanır, sonra reddedilir.
import time
import random
import base64

# Gizli not: aGVya2VzIGJ1cm9rcmFzaSBldnJha2V5aSBldnJha2V5ZSBib3JjdWxhcmlr (decode edersen anlarsın, ama etme)

def damgala(evrak):
    print(f"\n📜 Evrak alındı: '{evrak}'")
    print("☕ Çay demleniyor...")
    time.sleep(2)
    print("📝 Formlar kontrol ediliyor...")
    time.sleep(1.5)
    print("🔍 Eksik evrak aranıyor...")
    time.sleep(2)
    
    kararlar = [
        "EVRAK EKSİK! Lütfen 47 adet fotokopi ile tekrar başvurun.",
        "ONAYLANDI... şaka. Aslında reddedildi. Sebep: 'Gerek yok'.",
        "BEKLEME LİSTESİNE ALINDI. Tahmini süre: 2047 yılı.",
        "DAMGA BASILDI ama mürekkep bitmiş. Tekrar gelin.",
        "Resmi olarak 'olur' dendi ama sonra 'olmaz' çıktı."
    ]
    karar = random.choice(kararlar)
    print(f"\n📌 KARAR: {karar}")
    print("\n✅ İşlem tamamlandı (asla tamamlanmadı).")

if __name__ == "__main__":
    print("🏢 RESMİ BÜROKRATİK EVRAK ONAY MAKİNESİ")
    print("Lütfen onaylanmasını istediğiniz evrakı yazın (veya herhangi bir şey):")
    try:
        evrak = input("> ")
        if not evrak.strip():
            evrak = "Boş evrak (en tehlikelisi)"
        damgala(evrak)
    except KeyboardInterrupt:
        print("\n\n🚫 İşlem iptal edildi. Evrak dosyaya konuldu ve kayboldu.")
