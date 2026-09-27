# 🐔 Mi Animeteca

**Tu catálogo personal de anime, sin cuentas, sin servidores, sin excusas.**

Una app de una sola página para llevar el registro de todo lo que ya viste (o estás viendo): buscas el título, se agrega con imagen, sinopsis traducida, tipo, año, episodios y temporada, lo calificas con un sello estilo archivo, y lo organizas por orden alfabético, calificación, género o estado.

Todo vive en tu navegador. Nada se sube a ningún servidor.

---

## ✨ Qué hace

**Agregar animes**
- 🔍 **Buscar y agregar** — busca cualquier anime (vía [AniList](https://anilist.co)) y se agrega con póster, sinopsis **traducida automáticamente al español**, tipo, año, episodios y nombres alternativos (japonés / inglés).
- 🧠 **Autocompletado inteligente** — el tipo (TV/OVA/Película/Especial) y la temporada (Primera, Segunda, Tercera...) se sugieren solos leyendo el título y la sinopsis (detecta "2nd Season", "Segunda Temporada", "第2期", etc.) — pero siempre puedes cambiarlos a mano, y tu elección nunca se pisa sola.
- 🔁 **Búsqueda persistente** — agregar un anime ya no borra tu búsqueda: ideal para meter varias temporadas de una sola tanda. Los resultados solo se limpian cuando tú borras el texto del buscador.
- ✍️ **Agregar manualmente** — sin depender de ninguna base de datos externa: título, imagen (por URL o subida desde tu dispositivo), género, tipo, año, episodios, temporada, calificación, estado y sinopsis, todo a mano.

**Organizar tu colección**
- 🎫 **Calificación con decimales** — del 1 al 10 en pasos de 0.5, más una marca especial **✦** para lo que consideres "obra maestra" (más de un 10).
- 🏷️ **Etiquetas de género** — cada género se muestra por separado, y puedes filtrar tu colección por cualquiera de ellos.
- 📺 **Mis Listas** — pestañas de estado (Todo / Viendo / Por Ver / Completado / Pausado / Descartado) para separar lo que ya terminaste de lo que sigues viendo.
- 🔤 **Ordenar** alfabéticamente, por calificación o por fecha de agregado.
- 🔍 **Búsqueda discreta** dentro de tu propia colección, sin salir de la pantalla principal.
- 🖼️ **Tres tamaños de vista** — miniaturas grandes, medianas o pequeñas, según cuánto quieras ver de un vistazo (se recuerda tu preferencia).
- 📖 **Ficha de detalle editable** — haz clic en cualquier título para ver y editar toda su información después de agregarlo.
- 📊 **Panel de estadísticas** — total de títulos, calificación promedio, episodios vistos, "obras maestra", desglose por estado y tus géneros más frecuentes.
- 🎨 **Color de acento personalizable** — elige tu propio color desde un selector nativo, en vez del turquesa por defecto.
- 👀 **Vista previa al pasar el mouse** — la sinopsis rápida sin abrir la ficha completa (en pantallas con mouse).
- 📺 **Progreso de episodios** y **próximo episodio** — para lo que estás viendo, con barra de avance y la fecha del siguiente capítulo si el anime sigue en emisión.
- 📝 **Notas personales** — un campo aparte de la sinopsis para tus propios comentarios.

**Respaldo**
- 💾 **Exportar respaldo (.json)** — toda tu colección en un solo archivo, para restaurarla en otro dispositivo.
- 🖨️ **Exportar lista (PDF con carátulas)** — genera de forma instantánea un documento web visual con toda tu colección y sus imágenes. Al abrirlo, solo necesitas presionar `Ctrl + P` (Imprimir) en tu navegador para guardarlo como un PDF perfecto.
- 📥 **Importar respaldo** — agrega lo del archivo a tu colección, sin duplicar lo que ya tengas.

## 🚀 Cómo usarla
**Opción 1 — .exe:**
1. Descarga el Releases `https://github.com/YairZ21/-Mi-Animeteca/releases/tag/Mi-Animeteca`
2. Ejecutar el instalador.

**Opción 2 — Local:**
1. Descarga [`index.html`](./index.html) **y** [`style.css`](./style.css) — deben estar juntos, en la misma carpeta.
2. Abre `index.html` con cualquier navegador (haciendo doble clic, o "Abrir con..."). Eso es todo.

> **Importante (celular):** ábrelo siempre con un navegador de verdad (Chrome, Safari, Firefox...), no desde el visor interno de WhatsApp, Telegram, Google Drive u otra app — esos visores no cargan el `style.css` ni permiten guardar datos correctamente.

**Opción 3 — GitHub Pages (para tenerla en una URL fija):**
1. Ve a *Settings → Pages* en este repositorio.
2. Elige la rama `main` y la carpeta `/ (root)`.
3. En un par de minutos tu animeteca estará disponible en `https://<tu-usuario>.github.io/mi-animeteca/`.

---

## 📜 Acuerdo de licencia de uso

Este proyecto **no es de código abierto** y se proporciona únicamente para uso personal y no comercial.

Consulta el archivo [LICENSE](LICENSE) para conocer los términos completos.

---



## 🌍 English version

# 🐔 Mi Animeteca

**Your personal anime catalog, no accounts, no servers, no excuses.**

A single-page app to keep track of everything you've already watched (or are watching): search for a title, add it with an image, translated synopsis, type, year, episodes, and season, rate it with a file-like stamp, and organize it alphabetically, by score, genre, or status.

Everything lives in your browser. Nothing is uploaded to any server.

---

## ✨ What it does

**Add anime**
- 🔍 **Search and add** — search for any anime (via [AniList](https://anilist.co)) and it gets added with a poster, synopsis **automatically translated into Spanish**, type, year, episodes, and alternate titles (Japanese / English).
- 🧠 **Smart autocomplete** — the type (TV/OVA/Movie/Special) and season (First, Second, Third...) are suggested automatically by reading the title and synopsis (detects "2nd Season", "Segunda Temporada", "第2期", etc.) — but you can always change them manually, and your choice is never overwritten.
- 🔁 **Persistent search** — adding an anime no longer clears your search: perfect for adding several seasons in one batch. Results only clear when you delete the search text.
- ✍️ **Add manually** — without relying on any external database: title, image (by URL or upload from your device), genres, type, year, episodes, season, rating, status, and synopsis, all by hand.

**Organize your collection**
- 🎫 **Decimal ratings** — from 1 to 10 in 0.5 steps, plus a special **✦** mark for what you consider a "masterpiece" (more than a 10).
- 🏷️ **Genre tags** — each genre is displayed separately, and you can filter your collection by any of them.
- 📺 **My Lists** — status tabs (All / Watching / To Watch / Completed / Paused / Dropped) to separate what you've finished from what you're still watching.
- 🔤 **Sort** alphabetically, by rating, or by date added.
- 🔍 **Discreet search** within your own collection without leaving the main screen.
- 🖼️ **Three view sizes** — large, medium, or small thumbnails depending on how much you want to see at a glance (your preference is remembered).
- 📖 **Editable detail sheet** — click any title to view and edit all its information after adding it.
- 📊 **Statistics panel** — total titles, average rating, episodes watched, "masterpieces", breakdown by status, and your most frequent genres.
- 🎨 **Custom accent color** — choose your own color from a native selector instead of the default turquoise.
- 👀 **Hover preview** — quick synopsis without opening the full details sheet (on mouse-enabled screens).
- 📺 **Episode progress** and **next episode** — for what you're watching, with a progress bar and the next chapter date if the anime is still airing.
- 📝 **Personal notes** — a separate field from the synopsis for your own comments.

**Backup**
- 💾 **Export backup (.json)** — your entire collection in a single file, so you can restore it on another device.
- 🖨️ **Export list (PDF with covers)** — instantly generates a visual web document with your whole collection and images. When you open it, all you need is to press `Ctrl + P` (Print) in your browser to save it as a perfect PDF.
- 📥 **Import backup** — adds the data from the file to your collection without duplicating what you already have.

## 🚀 How to use it
**Option 1 — .exe:**
1. Download the release at `https://github.com/YairZ21/-Mi-Animeteca/releases/tag/Mi-Animeteca`
2. Run the installer.

**Option 2 — Local:**
1. Download [`index.html`](./index.html) **and** [`style.css`](./style.css) — they must stay together in the same folder.
2. Open `index.html` in any browser (double-click it, or use "Open with..."). That's it.

> **Important (mobile):** always open it in a real browser (Chrome, Safari, Firefox...), not from the internal viewer of WhatsApp, Telegram, Google Drive, or any other app — those viewers do not load `style.css` and do not save data correctly.

**Option 3 — GitHub Pages (to have it on a fixed URL):**
1. Go to *Settings → Pages* in this repository.
2. Choose the `main` branch and the `/ (root)` folder.
3. In a couple of minutes your animeteca will be available at `https://<your-user>.github.io/mi-animeteca/`.

---

## 📜 License usage agreement

This project is **not open source** and is provided for personal and non-commercial use only.

See the [LICENSE](LICENSE) file for the complete terms.

---


