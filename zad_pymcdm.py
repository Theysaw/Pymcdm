import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pymcdm.methods import TOPSIS, SPOTIS, VIKOR 
from pymcdm.weights import entropy_weights
from pymcdm.normalizations import minmax_normalization

# --- Dane wejściowe ---
# Alternatywy: A1, A2, A3
# Kryteria: Cena (min), Spalanie (min), Moc (max)

matrix = np.array([
    [50000, 7.0, 120],   # A1
    [55000, 6.5, 130],   # A2
    [52000, 6.8, 125]    # A3
])

# Ręczne wagi
weights_manual = np.array([0.4, 0.3, 0.3])

# Automatyczne wagi – metoda entropii
weights_entropy = entropy_weights(matrix, types=[-1, -1, 1])

# Typy kryteriów: -1 = minimalizuj, 1 = maksymalizuj
types_list = [-1, -1, 1]           # Do normalizacji
types_array = np.array(types_list) # Do SPOTIS

# --- Normalizacja danych dla metod, które tego wymagają ---
norm_matrix = minmax_normalization(matrix, types_list)

# --- TOPSIS ---
topsis = TOPSIS()
scores_topsis = topsis(norm_matrix, weights_manual, types_list)

# --- SPOTIS ---
# Określenie granic (min i max dla każdej kolumny)
bounds = np.array([(min(matrix[:, i]), max(matrix[:, i])) for i in range(matrix.shape[1])])

spotis = SPOTIS(bounds)
scores_spotis = spotis(matrix, weights_manual, types_array)

# --- VIKOR  ---
vikor = VIKOR()
scores_vikor = vikor(norm_matrix, weights_manual, types_list)

# --- Zestawienie wyników ---
alternatives = ['A1', 'A2', 'A3']
results_df = pd.DataFrame({
    'Alternatywa': alternatives,
    'TOPSIS': scores_topsis,
    'SPOTIS': scores_spotis,
    'VIKOR': scores_vikor
})

# --- Sortowanie dla każdego rankingu (im wyższa wartość, tym lepsza alternatywa) ---
for col in ['TOPSIS', 'SPOTIS', 'VIKOR']:
    results_df[col + '_Ranking'] = results_df[col].rank(ascending=False)

print("\n=== Ranking Alternatyw ===")
print(results_df)

# --- Wagi: ręczne vs entropia ---
print("\nWagi ręczne:", weights_manual)
print("Wagi (entropy):", weights_entropy)

# --- Wykres słupkowy porównujący wyniki metod TOPSIS, SPOTIS, VIKOR ---
# Ustawienia wykresu
plt.figure(figsize=(10, 6))

# Ustalamy szerokość słupków
bar_width = 0.2

# Ustalamy pozycje słupków dla każdej metody
index = np.arange(len(alternatives))

# Rysujemy słupki dla każdej metody
plt.bar(index - bar_width, results_df['TOPSIS'], bar_width, label='TOPSIS')
plt.bar(index, results_df['SPOTIS'], bar_width, label='SPOTIS')
plt.bar(index + bar_width, results_df['VIKOR'], bar_width, label='VIKOR')

# Dodajemy etykiety, tytuł i legendę
plt.xlabel('Alternatywy')
plt.ylabel('Wynik')
plt.title('Porównanie wyników metod MCDM (TOPSIS, SPOTIS, VIKOR)')
plt.xticks(index, alternatives)
plt.legend()

# Wyświetlamy wykres
plt.tight_layout()
plt.show()