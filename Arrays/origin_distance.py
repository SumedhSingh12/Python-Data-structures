import math
def distance_origin(points, k):
    distance = {}
    for point in points:
        distance[math.sqrt((point[0]**2)+(point[1]**2))] = point
    dist = list(distance.keys())
    dist.sort()
    result = []
    for d in dist:
        result.append(distance[d])
    return result[:k]
        
        
points = [(-2,4),(0,-2),(-1,0),(3,-5),(-2,-3),(3,2)]
print(distance_origin(points, 3))