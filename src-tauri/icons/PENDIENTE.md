# Íconos pendientes

Esta carpeta necesita 4 archivos antes de poder compilar el `.exe`:

- `32x32.png`
- `128x128.png`
- `128x128@2x.png` (256x256 px, a pesar del nombre)
- `icon.ico`

**Forma más fácil:** cuando tengas tu logo (una sola imagen cuadrada, idealmente
1024x1024 px), corre desde la raíz del proyecto:

```bash
pip install pillow
python3 scripts/generar_iconos.py ruta/a/tu-logo.png
```

Eso genera los 4 archivos automáticamente en esta carpeta. Después de eso,
puedes borrar este archivo `PENDIENTE.md`.

**Sin ese script:** también puedes crearlos a mano con cualquier editor de
imágenes, respetando esos 4 nombres y tamaños exactos.
