import matplotlib.pyplot as plt
import random
import numpy as np

# --- 1. KURULUM ---
num_samples = 50
time_steps = np.arange(num_samples)

# Normal veriler için başlangıç değerleri
gps_altitude = [100.0] # Drone 100m yükseklikte başlıyor
speed = [15.0]         # 15 m/s hız
battery = [95.0]       # %95 batarya

# Anormallik Eşiği
THRESHOLD = 10.0 

# Güvenlik Durumu Kayıtları
security_logs = ["GÜVENLİ"] 
rejected_indices = []    
rejected_values = []     

# --- 2. VERİ SİMULASYONU ---
for i in range(1, num_samples):
    # Normal değişimler
    new_battery = battery[-1] - random.uniform(0.1, 0.3)
    new_speed = speed[-1] + random.uniform(-1, 1)
    delta_h = random.uniform(-2, 2)
    
    # --- ANOMALİ ENJEKSİYONU (SENARYO 2) ---
    # 30. saniyede bir "GPS Spoofing" simülasyonu
    if i == 30:
        delta_h = 35.0 # Ani sıçrama!
        
    current_val = gps_altitude[-1] + delta_h
    
    # --- 3. KONTROL MANTIĞI ---
    diff = abs(current_val - gps_altitude[-1])
    
    if diff > THRESHOLD:
        # ANORMAL DURUM: Veriyi kaydet ama REJECT et.
        security_logs.append("Reddedildi")
        rejected_indices.append(i)
        rejected_values.append(current_val)
    else:
        security_logs.append("Güvenli")
    
    gps_altitude.append(current_val)
    speed.append(new_speed)
    battery.append(new_battery)

# --- 4. GÖRSELLEŞTİRME ---
plt.figure(figsize=(10, 6))
plt.plot(time_steps, gps_altitude, label='GPS Rakımı (Veri Akışı)', color='blue', linewidth=2)

if rejected_indices:
    plt.scatter(rejected_indices, rejected_values, color='red', s=150, label='Anormallik Tespit Edildi (REDDEDİLDİ)', zorder=5)
    plt.annotate('SPOOFING ATTACK TESPİT EDİLDİ', 
                 xy=(rejected_indices[0], rejected_values[0]), 
                 xytext=(rejected_indices[0]+2, rejected_values[0]-15),
                 arrowprops=dict(facecolor='black', shrink=0.05))

plt.title('CBF Drone Projesi - Telemetri Güvenlik Kontrolü')
plt.xlabel('Zaman (saniye)')
plt.ylabel('Rakım (metre)')
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend()
plt.show()

print(f"Test Tamamlandı. Tespit edilen anomali sayısı: {len(rejected_indices)}")