import math #sqrt fonksiyonunu kullanmak için

points=[(0,5),(5,10),(10,15),(15,20)]


def euclideanDistance(point1,point2):
    x1 , y1 = point1
    x2 , y2 = point2
    distance=math.sqrt((x2-x1)**2+(y2-y1)**2)
    return distance


distances=[]
for i in range(len(points)):
   for j in range(i+1,len(points)): #diğer noktalar ile hesaplamak için
       distance=euclideanDistance(points[i],points[j])
       distances.append(distance)


min_distance=min(distances)
print("Noktalar arasındaki uzaklıklar:")
print(distances)
print("Noktalar arasındaki minimum mesafe:", min_distance)
