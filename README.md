# CBF Drone - Telemetri Güvenlik ve Anormallik Tespit Modülü

Bu modül, İHA sistemleri için Python tabanlı basit bir telemetri veri simülasyonu ve güvenlik kontrol mekanizması içerir.

## 📋 Modül Özeti
Modül, sensörlerden gelen verilerin güvenilirliğini test etmek amacıyla iki temel senaryo üzerine kurulmuştur:
1.  **Normal Durum:** GPS konumu, hız ve batarya değerlerinin olağan seyirde değiştiği simülasyon.
2.  **Anormal Durum (Saldırı/Hata):** Veri akışı içerisine ani ve fiziksel olarak imkansız sıçramaların (örn: konumun aniden 20-30 metre atlaması) eklendiği senaryo.

## ⚙️ Kontrol Mantığı
Sistem, verilerin güvenilirliğini basit bir **Eşik Kontrolü (Threshold Check)** ile denetler:
* Konum verisindeki değişim belirli bir eşik değerinden büyükse, sistem bu veriyi **"Güvenilmez"** kabul eder.
* Bu durumda **"Veri Reddedildi"** durumu tetiklenir ve hatalı veri sisteme sokulmaz.

## 📊 Görselleştirme ve Çıktılar
Modül kapsamında aşağıdaki çıktılar üretilmiştir:

* **Matplotlib Grafiği:** Normal veri akışı ile tespit edilen hatalı verinin aynı grafik üzerinde görselleştirilmesi. Sistemin anormalliği ayırt edebildiği gösterilmiştir.
* **Veri Akış Diyagramı (Draw.io):** Sensör → Veri Paketi → Güvenlik Kontrolü → Kabul/Red → Uçuş Kontrol Sistemi mantığını gösteren şema.
* **Teknik Açıklama:** Sistemin anormal veriyi nasıl tespit ettiğini anlatan 1 sayfalık teknik rapor.
