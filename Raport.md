## 1. Wprowadzenie

Celem analizy było porównanie różnych alternatyw (A1, A2, A3) na podstawie trzech kryteriów: ceny, spalania i mocy. Wykorzystano metody MCDM (TOPSIS, SPOTIS, VIKOR), aby wyznaczyć ranking alternatyw.

## 2. Konfiguracja analizy

- **Alternatywy:**
  - A1: Cena = 50000, Spalanie = 7.0, Moc = 120
  - A2: Cena = 55000, Spalanie = 6.5, Moc = 130
  - A3: Cena = 52000, Spalanie = 6.8, Moc = 125

- **Kryteria:**
  - Cena (min), Spalanie (min), Moc (max)

- **Wagi:**
  - Ręczne wagi: [0.4, 0.3, 0.3]

- **Typy kryteriów:**
  - Cena: minimalizuj, Spalanie: minimalizuj, Moc: maksymalizuj

## 3. Wyniki

### 3.1 Ranking Alternatyw

| Alternatywa | TOPSIS  | SPOTIS  | VIKOR   | TOPSIS_Ranking | SPOTIS_Ranking | VIKOR_Ranking |
|-------------|---------|---------|---------|----------------|----------------|---------------|
| A1          | 0.5147  | 0.60    | 0.5000  | 1.0            | 1.0            | 2.0           |
| A2          | 0.4853  | 0.40    | 0.6875  | 2.0            | 3.0            | 1.0           |
| A3          | 0.4800  | 0.49    | 0.2750  | 3.0            | 2.0            | 3.0           |

### 3.2 Analiza wyników

- **TOPSIS:** Najwyższy wynik uzyskała alternatywa A1, co oznacza, że jest to najlepsza opcja według tej metody.
- **SPOTIS:** Alternatywa A1 także zajmuje pierwsze miejsce, a A2 uzyskuje najgorszy wynik.
- **VIKOR:** Alternatywa A2 uzyskuje najlepszy wynik, podczas gdy A3 wypada najsłabiej.

## 4. Wnioski

- **A1** wydaje się najlepszą alternatywą, szczególnie w metodach TOPSIS i SPOTIS.
- **A2** jest najlepsza według metody VIKOR, ale w pozostałych metodach wypada słabiej.
- **A3** zajmuje najniższe pozycje w każdej z metod, co sugeruje, że jest to najmniej korzystna opcja.

## 5. Podsumowanie

Pomimo różnic w rankingach, A1 jest najlepszą alternatywą w analizie MCDM, biorąc pod uwagę metody TOPSIS i SPOTIS. Z kolei A2 wyróżnia się metodą VIKOR. Wyniki pokazują, jak różne metody mogą prowadzić do różnych wniosków, a odpowiedni wybór metody zależy od preferencji decydenta.
"""
