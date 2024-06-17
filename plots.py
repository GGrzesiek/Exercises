import matplotlib.pyplot as plt
import numpy as np
# I needed plot for my report :p
# Dane do wykresu
rozmiary = ['900 B', '900 kB', '100 MB']
czasy_MD5 = [8.158508, 0.01, 0.00141]

# Tworzenie wykresu
plt.figure(figsize=(8, 5))
plt.bar(rozmiary, czasy_MD5, color='blue', edgecolor='grey')

# Dodanie etykiet na osiach X i Y oraz tytułu
plt.xlabel('Rozmiar pliku', fontweight='bold')
plt.ylabel('Czas obliczenia MD5 (s)', fontweight='bold')
plt.title('Czas obliczania MD5 dla różnych rozmiarów plików')

# Wyświetlenie wykresu
plt.show()
