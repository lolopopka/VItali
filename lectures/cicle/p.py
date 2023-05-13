def perim(width, height):
    per = (width * 2) + (height * 2)
    print(f"Периметр прямоугольника, равен {per}")
perim(*list(map(int, input().split())))