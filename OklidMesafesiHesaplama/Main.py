import math

# Noktaların Tanımlanması
points = [
    (1, 2),
    (4, 6),
    (3, 1),
    (8, 5),
    (0, 0)
]

# Öklid Mesafesi Hesaplama Fonksiyonu
def euclidean_distance(point1, point2):
    """İki nokta arasındaki Öklid mesafesini formüle göre hesaplar:
       d = √((x₂ - x₁)² + (y₂ - y₁)²)
    """
    x1, y1 = point1
    x2, y2 = point2
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Mesafelerin Hesaplanması
distances = []
for i in range(len(points)):
    for j in range(i + 1, len(points)):
        # Her nokta çifti arasındaki mesafeyi hesapla
        distance = euclidean_distance(points[i], points[j])
        distances.append(distance)
        # Formüle göre mesafeyi yazdır
        print(f"Mesafe hesaplandı: d = √(({points[j][0]} - {points[i][0]})² + ({points[j][1]} - {points[i][1]})²) = {distance:.2f}")

# Minimum Mesafenin Bulunması
min_distance = min(distances)
print("\nMinimum mesafe:", min_distance)

