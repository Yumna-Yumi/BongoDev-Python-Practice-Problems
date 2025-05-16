def isLandscape(width, height):
    if width > height:
        return "Landscape"
    else:
        return "Portrait"

print(isLandscape(1920, 1080))