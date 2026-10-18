# import pygame
# import sys

# pygame.init()

# # Ekran boyutu
# genislik, yukseklik = 600, 400
# ekran = pygame.display.set_mode((genislik, yukseklik))
# pygame.display.set_caption("🐍 Yılan Oyunu")

# # Renkler (RGB formatında)
# siyah = (0, 0, 0)
# yesil = (0, 255, 0)
# kirmizi = (255, 0, 0)

# # FPS (oyun hızı)
# saat = pygame.time.Clock()
# import random

# yilan_konum = [100, 50]  # Başlangıç pozisyonu
# yilan_govde = [[100, 50], [90, 50], [80, 50]]

# elma_konum = [random.randrange(1, (genislik//10)) * 10,
#                random.randrange(1, (yukseklik//10)) * 10]
# elma_cikti = True

# yön = 'SAĞ'
# degisim = yön

# skor = 0

# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             pygame.quit()
#             sys.exit()
#         elif event.type == pygame.KEYDOWN:
#             if event.key == pygame.K_UP and yön != 'AŞAĞI':
#                 degisim = 'YUKARI'
#             elif event.key == pygame.K_DOWN and yön != 'YUKARI':
#                 degisim = 'AŞAĞI'
#             elif event.key == pygame.K_LEFT and yön != 'SAĞ':
#                 degisim = 'SOL'
#             elif event.key == pygame.K_RIGHT and yön != 'SOL':
#                 degisim = 'SAĞ'

#     yön = degisim

#     # Yönlere göre hareket
#     if yön == 'YUKARI':
#         yilan_konum[1] -= 10
#     if yön == 'AŞAĞI':
#         yilan_konum[1] += 10
#     if yön == 'SOL':
#         yilan_konum[0] -= 10
#     if yön == 'SAĞ':
#         yilan_konum[0] += 10

#     # Gövde güncelle
#     yilan_govde.insert(0, list(yilan_konum))
#     if yilan_konum[0] == elma_konum[0] and yilan_konum[1] == elma_konum[1]:
#         skor += 1
#         elma_cikti = False
#     else:
#         yilan_govde.pop()

#     if not elma_cikti:
#         elma_konum = [random.randrange(1, (genislik//10)) * 10,
#                        random.randrange(1, (yukseklik//10)) * 10]
#     elma_cikti = True

#     # Arka plan
#     ekran.fill(siyah)

#     # Yılanı çiz
#     for parca in yilan_govde:
#         pygame.draw.rect(ekran, yesil, pygame.Rect(parca[0], parca[1], 10, 10))

#     # Elmayı çiz
#     pygame.draw.rect(ekran, kirmizi, pygame.Rect(elma_konum[0], elma_konum[1], 10, 10))

#     # Sınır kontrolü (oyun bitiş)
#     if yilan_konum[0] < 0 or yilan_konum[0] > genislik-10:
#         break
#     if yilan_konum[1] < 0 or yilan_konum[1] > yukseklik-10:
#         break

#     # Kendine çarpma
#     for blok in yilan_govde[1:]:
#         if yilan_konum[0] == blok[0] and yilan_konum[1] == blok[1]:
#             pygame.quit()
#             sys.exit()

#     pygame.display.update()
#     saat.tick(15)
   
#     def skoru_goster(skor):
#         font = pygame.font.SysFont('Arial', 25)
#         skor_yazi = font.render(f"Skor: {skor}", True, (255, 255, 255))
#         ekran.blit(skor_yazi, [10, 10])

#     skoru_goster(skor) 



# 

import pygame
import sys
import random

pygame.init()

# ---------------- AYARLAR VE RENKLER ----------------
GENISLIK, YUKSEKLIK = 600, 400
HUCRE = 10

ekran = pygame.display.set_mode((GENISLIK, YUKSEKLIK))
pygame.display.set_caption("🐍 Liderlik Tablolu Oyunu")

SIYAH = (15, 15, 15)
YESIL = (46, 204, 113)
KOYU_YESIL = (39, 174, 96)
KIRMIZI = (231, 76, 60)
BEYAZ = (236, 240, 241)
SARI = (241, 196, 15)
MAVI = (52, 152, 219)

saat = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 22)
buyuk_font = pygame.font.SysFont("Arial", 40)

# Oyunlar arası skor kaydı (İsim, Skor)
liderlik_tablosu = []

# ---------------- İSİM ALMA EKRANI ----------------
def isim_al_ekrani():
    oyuncu_adi = ""
    aktif = True
    
    while aktif:
        ekran.fill(SIYAH)
        
        baslik = buyuk_font.render("OYUNCU ADI", True, MAVI)
        bilgi = font.render("Lütfen adınızı yazın ve ENTER'a basın:", True, BEYAZ)
        isim_yazi = buyuk_font.render(oyuncu_adi + "_", True, SARI)
        
        ekran.blit(baslik, (GENISLIK // 2 - baslik.get_width() // 2, 80))
        ekran.blit(bilgi, (GENISLIK // 2 - bilgi.get_width() // 2, 150))
        ekran.blit(isim_yazi, (GENISLIK // 2 - isim_yazi.get_width() // 2, 210))
        
        pygame.display.update()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if oyuncu_adi.strip() != "":
                        aktif = False
                elif event.key == pygame.K_BACKSPACE:
                    oyuncu_adi = oyuncu_adi[:-1]
                else:
                    if len(oyuncu_adi) < 12 and event.unicode.isprintable():
                        oyuncu_adi += event.unicode
                        
    return oyuncu_adi.strip()

# ---------------- SKOR VE BİLGİ PANELİ ----------------
def bilgileri_goster(oyuncu_adi, skor):
    yazi = font.render(f"Oyuncu: {oyuncu_adi}  |  Skor: {skor}", True, BEYAZ)
    ekran.blit(yazi, (10, 8))
    pygame.draw.line(ekran, (50, 50, 50), (0, 35), (GENISLIK, 35), 2)

# ---------------- RESTART VE LİDERLİK EKRANI ----------------
def game_over_ekrani(oyuncu_adi, skor):
    # Skoru tabloya ekle ve yüksekten düşüğe sırala
    liderlik_tablosu.append((oyuncu_adi, skor))
    liderlik_tablosu.sort(key=lambda x: x[1], reverse=True)
    
    while True:
        ekran.fill(SIYAH)

        baslik = buyuk_font.render("GAME OVER", True, KIRMIZI)
        ekran.blit(baslik, (GENISLIK // 2 - baslik.get_width() // 2, 20))
        
        skor_yazi = font.render(f"Son Skorunuz ({oyuncu_adi}): {skor}", True, SARI)
        ekran.blit(skor_yazi, (GENISLIK // 2 - skor_yazi.get_width() // 2, 70))

        # Liderlik Tablosu Çizimi
        tablo_baslik = font.render("🏆 EN YÜKSEK SKORLAR 🏆", True, MAVI)
        ekran.blit(tablo_baslik, (GENISLIK // 2 - tablo_baslik.get_width() // 2, 110))
        
        y_pos = 145
        for i, (isim, p) in enumerate(liderlik_tablosu[:5], start=1):
            sira_yazi = font.render(f"{i}. {isim} - {p} Puan", True, BEYAZ)
            ekran.blit(sira_yazi, (GENISLIK // 2 - sira_yazi.get_width() // 2, y_pos))
            y_pos += 30

        secenek = font.render("R: Yeni Oyuncu / Tekrar Oyna   |   Q: Çıkış", True, YESIL)
        ekran.blit(secenek, (GENISLIK // 2 - secenek.get_width() // 2, 350))

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    oyunu_baslat()
                if event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()

# ---------------- ANA OYUN DÖNGÜSÜ ----------------
def oyunu_baslat():
    oyuncu_adi = isim_al_ekrani()
    
    skor = 0
    yilan_konum = [100, 60]
    yilan_govde = [[100, 60], [90, 60], [80, 60]]

    # Elma konumlandırma (Üst bilgi panelinin altında çıksın diye Y min: 40)
    elma_konum = [
        random.randrange(0, GENISLIK // HUCRE) * HUCRE,
        random.randrange(4, YUKSEKLIK // HUCRE) * HUCRE
    ]

    yon = "RIGHT"
    degisim = yon

    while True:
        # Event Kontrolü
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and yon != "DOWN":
                    degisim = "UP"
                elif event.key == pygame.K_DOWN and yon != "UP":
                    degisim = "DOWN"
                elif event.key == pygame.K_LEFT and yon != "RIGHT":
                    degisim = "LEFT"
                elif event.key == pygame.K_RIGHT and yon != "LEFT":
                    degisim = "RIGHT"

        yon = degisim

        # Hareket Güncelleme
        if yon == "UP":
            yilan_konum[1] -= HUCRE
        if yon == "DOWN":
            yilan_konum[1] += HUCRE
        if yon == "LEFT":
            yilan_konum[0] -= HUCRE
        if yon == "RIGHT":
            yilan_konum[0] += HUCRE

        # Gövdeyi öne ekle
        yilan_govde.insert(0, list(yilan_konum))

        # Elma Yeme & Büyüme Mantığı
        if yilan_konum == elma_konum:
            skor += 3  # Her yem 3 puan
            elma_konum = [
                random.randrange(0, GENISLIK // HUCRE) * HUCRE,
                random.randrange(4, YUKSEKLIK // HUCRE) * HUCRE
            ]
            # Büyüme: pop() yapılmaz, yılan 1 birim uzar
        else:
            yilan_govde.pop()

        # Duvara Çarpma (Üst panel sınırı Y < 40)
        if yilan_konum[0] < 0 or yilan_konum[0] >= GENISLIK or yilan_konum[1] < 40 or yilan_konum[1] >= YUKSEKLIK:
            game_over_ekrani(oyuncu_adi, skor)

        # Kendine Çarpma
        for blok in yilan_govde[1:]:
            if yilan_konum == blok:
                game_over_ekrani(oyuncu_adi, skor)

        # Çizim İşlemleri
        ekran.fill(SIYAH)

        # Yılanı çiz
        for i, parca in enumerate(yilan_govde):
            renk = YESIL if i == 0 else KOYU_YESIL
            pygame.draw.rect(ekran, renk, pygame.Rect(parca[0], parca[1], HUCRE, HUCRE))

        # Elmayı çiz
        pygame.draw.rect(ekran, KIRMIZI, pygame.Rect(elma_konum[0], elma_konum[1], HUCRE, HUCRE))

        # Üst Bilgileri Çiz
        bilgileri_goster(oyuncu_adi, skor)

        pygame.display.update()
        saat.tick(15 + (skor // 9))  # Skor arttıkça hız hafifçe artar

if __name__ == "__main__":
    oyunu_baslat()