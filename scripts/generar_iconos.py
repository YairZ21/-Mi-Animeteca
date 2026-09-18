"""
Genera todos los tamaños de ícono que Tauri necesita para Windows, a partir
de UNA sola imagen cuadrada (recomendado: 1024x1024 px, fondo incluido).

Uso:
    pip install pillow
    python3 scripts/generar_iconos.py ruta/a/tu-logo.png

Esto crea (o reemplaza) los archivos dentro de src-tauri/icons/:
    32x32.png, 128x128.png, 128x128@2x.png, icon.ico
"""
import sys
import os
from PIL import Image


def main():
    if len(sys.argv) < 2:
        print("Uso: python3 scripts/generar_iconos.py ruta/a/tu-logo.png")
        sys.exit(1)

    src_path = sys.argv[1]
    out_dir = os.path.join(os.path.dirname(__file__), "..", "src-tauri", "icons")
    os.makedirs(out_dir, exist_ok=True)

    img = Image.open(src_path).convert("RGBA")
    if img.width != img.height:
        print("Aviso: la imagen no es cuadrada, se recorta al centro.")
        size = min(img.width, img.height)
        left = (img.width - size) // 2
        top = (img.height - size) // 2
        img = img.crop((left, top, left + size, top + size))

    sizes = {
        "32x32.png": 32,
        "128x128.png": 128,
        "128x128@2x.png": 256,
    }
    for name, size in sizes.items():
        img.resize((size, size), Image.LANCZOS).save(os.path.join(out_dir, name))

    # .ico multi-resolución, el formato que Windows espera para el ícono del .exe
    ico_img = img.resize((256, 256), Image.LANCZOS)
    ico_img.save(
        os.path.join(out_dir, "icon.ico"),
        sizes=[(16, 16), (24, 24), (32, 32), (48, 48), (64, 64), (128, 128), (256, 256)],
    )

    print("Listo. Archivos generados en", out_dir)


if __name__ == "__main__":
    main()
