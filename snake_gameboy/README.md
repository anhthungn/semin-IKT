# Maturitní práce – Herní konzole Snake

Tento projekt je maturitní prací zaměřenou na vývoj jednoduché přenosné herní konzole pro klasickou hru **Snake**, postavené na platformě **Arduino Nano**.

## Programová část

Herní logika je implementována v jazyce **C/C++** pro Arduino. Program zajišťuje:

- **Zobrazování hada** na 8×8 LED matici (ovládané přes MAX7219)
- **Zobrazování skóre** na dvou 7segmentových displejích pomocí posuvných registrů (74HC595)
- **Ovládání pohybu** pomocí čtyř směrových tlačítek
- **Zvukové efekty** pomocí piezo-bzučáku
- **Detekci kolizí** a **generování potravy** pro hada
- **Sledování a aktualizaci skóre**

Kód je optimalizován pro běh v reálném čase, využívá stavový automat pro řízení hry a neblokující časování pro hladký průběh.

## Použité nástroje

- Arduino IDE pro vývoj kódu
- Knihovny: LedControl (MAX7219), vlastní funkce pro registry a displeje

## Hardware

- Arduino Nano  
- LED matice 8×8 + MAX7219  
- 2× 7segmentový displej + 2× 74HC595  
- 4 tlačítka, piezo-bzučák  
- Napájení: 4× AA baterie  

## Autor

Nguyenová Anh Thu  
Střední škola _Gymnázium, Praha 4, Písnická 760_  
Rok: 2025
