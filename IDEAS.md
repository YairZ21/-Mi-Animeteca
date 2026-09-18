# 💡 Ideas pendientes

Lista de funciones pedidas para implementar más adelante. Se ejecutan bajo demanda
("ejecuta la idea N"), no automáticamente.

## ✅ Ya hechas (de tandas anteriores)
- Precuela/secuela clicable, con vínculo manual visual por carátulas.
- Fondo con imagen en la ficha de detalle.
- Sello de calificación cambiado a estrella.
- Progreso de episodios, próximos episodios, notas personales.
- Selector de color de acento, vista previa al pasar el mouse.
- Barra de controles fija (sticky) al hacer scroll.
- Rediseño visual de los formularios de agregar/editar (secciones agrupadas).
- Arreglo de la vista en celular.
- App de escritorio para Windows (Tauri + GitHub Actions) — en construcción.

## 1. Sección de Manga / Manhwa
Una colección nueva, independiente del catálogo de anime, con su propio
almacenamiento separado (mismo concepto que tenía el antiguo modo +18, ya
quitado — habría que decidir si esto sigue teniendo sentido ahora que el
proyecto va hacia convertirse en app de escritorio, o si conviene mantenerlo
todo en un solo catálogo con un filtro de tipo en vez de una sección aparte).

Si se retoma, queda pendiente decidir:
- Color de acento (Manhwa: morado, ya pedido explícitamente antes; Manga: sin definir).
- Si los campos deben adaptarse ("episodios" → "capítulos/tomos", si "temporada"
  sigue aplicando igual).
- Si la búsqueda sigue usando AniList (`type: MANGA`, con `countryOfOrigin`
  para distinguir Corea/Japón) o conviene separarlo en dos filtros.

## 2. App para Android (.apk)
Ya se armó la base con Tauri para Windows; en algún momento se retoma para
generar también la versión Android (Tauri también soporta ese destino, con
Android Studio o, igual que con Windows, compilándolo en la nube vía GitHub
Actions con un runner adecuado).
