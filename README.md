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

**Modo +18**
- 🔞 Un botón aparte cambia, **dentro de la misma ventana**, a un archivo independiente con su propio almacenamiento — nunca se mezcla con tu catálogo principal. Tiene su propio acento de color (`#ff537e`) para diferenciarlo de un vistazo, y pide confirmar mayoría de edad la primera vez.

**Respaldo**
- 💾 **Exportar respaldo (.json)** — un solo archivo que incluye **ambas colecciones** (normal y +18), pensado para restaurar todo de una vez en otro dispositivo.
- 📝 **Exportar lista (.txt)** — listado legible con título, género y calificación.
- 📥 **Importar respaldo** — restaura cada colección en su lugar correspondiente, sin duplicar lo que ya tengas.

## 🚀 Cómo usarla

No hay instalación, ni build, ni dependencias.

**Opción 1 — Local:**
1. Descarga [`index.html`](./index.html) **y** [`style.css`](./style.css) — deben estar juntos, en la misma carpeta.
2. Abre `index.html` haciendo doble clic. Eso es todo.

**Opción 2 — GitHub Pages (para tenerla en una URL fija):**
1. Ve a *Settings → Pages* en este repositorio.
2. Elige la rama `main` y la carpeta `/ (root)`.
3. En un par de minutos tu animeteca estará disponible en `https://<tu-usuario>.github.io/mi-animeteca/`.

## 🗃️ Dónde se guardan tus datos

Todo se guarda con `localStorage` **en el navegador donde la abras**. Eso significa:

- Tus datos persisten entre sesiones sin necesidad de internet ni de iniciar sesión en ningún lado.
- El catálogo normal y el modo +18 se guardan bajo claves completamente separadas, así que nunca se mezclan aunque sea el mismo archivo.
- Si la abres en otro navegador o dispositivo, empieza vacía — usa **Exportar respaldo** en un lado e **Importar respaldo** en el otro para llevar tu colección contigo (el respaldo incluye ambas colecciones en un solo archivo).

## 🛠️ Stack

Dos archivos, sin frameworks, sin build step:

- `index.html` — estructura y JavaScript vanilla
- `style.css` — todos los estilos (variables CSS nativas, sin preprocesador)
- [AniList GraphQL API](https://anilist.co/graphiql) para la búsqueda de animes
- API pública de Google Translate para traducir sinopsis al español
- `localStorage` para toda la persistencia

Ambos archivos están comentados por secciones, para que sea fácil ubicar qué modificar en el futuro.

## 🤝 Contribuciones

Ideas, mejoras o reportes de bugs son bienvenidos vía *issues* o *pull requests*.

## 📄 Licencia

MIT — usa, copia y modifica libremente.
