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

No hay instalación, ni build, ni dependencias.

**Opción 1 — Local:**
1. Descarga [`index.html`](./index.html) **y** [`style.css`](./style.css) — deben estar juntos, en la misma carpeta.
2. Abre `index.html` con cualquier navegador (haciendo doble clic, o "Abrir con..."). Eso es todo.

> **Importante (celular):** ábrelo siempre con un navegador de verdad (Chrome, Safari, Firefox...), no desde el visor interno de WhatsApp, Telegram, Google Drive u otra app — esos visores no cargan el `style.css` ni permiten guardar datos correctamente.

**Opción 2 — GitHub Pages (para tenerla en una URL fija):**
1. Ve a *Settings → Pages* en este repositorio.
2. Elige la rama `main` y la carpeta `/ (root)`.
3. En un par de minutos tu animeteca estará disponible en `https://<tu-usuario>.github.io/mi-animeteca/`.

**Opción 3 — App de escritorio para Windows (`.exe`):**

El proyecto ya trae todo listo para compilarse como una app real de Windows con [Tauri](https://tauri.app), sin depender del navegador. Funciona **con y sin internet**: la app en sí (ver, calificar, editar, agregar manualmente) no necesita conexión; solo buscar animes nuevos y traducir sinopsis la necesitan, igual que en la versión web.

1. **Agrega tu logo** (si todavía no lo hiciste): coloca una imagen cuadrada (ideal 1024×1024 px) y corre:
   ```bash
   pip install pillow
   python3 scripts/generar_iconos.py ruta/a/tu-logo.png