import urllib.request
import os
from PIL import Image

BASE = r"F:\Doubao\ZombieSurvival\assets"

ASSETS = {
    "title.jpg": "https://aka.doubaocdn.com/s/IolEgpNbp5",
    "player.jpg": "https://aka.doubaocdn.com/s/rQZkkc2KVr",
    "supermarket.jpg": "https://aka.doubaocdn.com/s/UX4lSB7lYF",
    "hospital.jpg": "https://aka.doubaocdn.com/s/eKRkBjnQwM",
    "police.jpg": "https://aka.doubaocdn.com/s/Mt4mhor7k7",
    "warehouse.jpg": "https://aka.doubaocdn.com/s/10JZhzXUOG",
    "apartment.jpg": "https://aka.doubaocdn.com/s/jcZV2221jw",
    "safehouse.jpg": "https://aka.doubaocdn.com/s/EFeqzrKIE7",
    "zombie.jpg": "https://aka.doubaocdn.com/s/2uJdyUdWEi",
    "items_sheet.jpg": "https://aka.doubaocdn.com/s/gTIIGDIiRH",
}

def download(url, path):
    if os.path.exists(path):
        print(f"  exists: {path}")
        return
    print(f"  downloading: {url}")
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, timeout=30) as r:
        data = r.read()
    with open(path, "wb") as f:
        f.write(data)
    print(f"  saved: {path} ({len(data)} bytes)")

print("=== Downloading ===")
for name, url in ASSETS.items():
    download(url, os.path.join(BASE, name))

# Split item sheet (2 cols x 3 rows)
print("\n=== Splitting item icons ===")
sheet = Image.open(os.path.join(BASE, "items_sheet.jpg"))
w, h = sheet.size
cell_w, cell_h = w // 2, h // 3
item_names = ["canned_food", "water_bottle", "first_aid", "knife", "pistol", "wood_plank"]
for idx, name in enumerate(item_names):
    col = idx % 2
    row = idx // 2
    x = col * cell_w
    y = row * cell_h
    crop = sheet.crop((x, y, x + cell_w, y + cell_h))
    # Add padding
    out = Image.new("RGB", (cell_w, cell_h), (40, 40, 40))
    out.paste(crop, (0, 0))
    out.save(os.path.join(BASE, f"item_{name}.jpg"), "JPEG", quality=90)
    print(f"  item_{name}.jpg")

print("\n=== Done ===")
