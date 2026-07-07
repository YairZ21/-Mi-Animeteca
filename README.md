# 🐔 Mi Animeteca

**Tu catálogo personal de anime, sin cuentas, sin servidores, sin excusas.**

Una app de una sola página para llevar el registro de todo lo que ya viste: buscas el título, se agrega con imagen y sinopsis, lo calificas del 1 al 10 con un sello estilo archivo, y lo organizas por orden alfabético, calificación o género.

Todo vive en tu navegador. Nada se sube a ningún servidor.

---

## ✨ Qué hace

- 🔍 **Buscar y agregar** — busca cualquier anime (vía [AniList](https://anilist.co)) y se agrega con póster, sinopsis, tipo, año y episodios.
- ✍️ **Agregar manualmente** — sin internet, sin depender de ninguna base de datos: escribe el título, sube una imagen, pon el género y la sinopsis a mano.
- 🎫 **Sello de calificación** — califica cada título del 1 al 10 con un vistazo.
- 🏷️ **Etiquetas de género** — cada género se muestra por separado, y puedes filtrar tu colección por cualquiera de ellos.
- 📖 **Ficha de detalle editable** — haz clic en cualquier título para ver y editar toda su información después de agregarlo.
- 🔤 **Orden alfabético, por calificación o por fecha de agregado.**
- 💾 **Respaldo real** — exporta tu colección completa a `.json` (para restaurarla en otro dispositivo) o a `.txt` (lista legible con título, género y calificación).
- 📤 **Compartir directo** — envía tu respaldo por correo, Drive o cualquier app desde el mismo panel de compartir del sistema.

## 🚀 Cómo usarla

No hay instalación, ni build, ni dependencias.

**Opción 1 — Local:**
1. Descarga [`index.html`](./index.html).
2. Ábrelo haciendo doble clic. Eso es todo.

**Opción 2 — GitHub Pages (para tenerla en una URL fija):**
1. Ve a *Settings → Pages* en este repositorio.
2. Elige la rama `main` y la carpeta `/ (root)`.
3. En un par de minutos tu animeteca estará disponible en `https://<tu-usuario>.github.io/mi-animeteca/`.

## 🗃️ Dónde se guardan tus datos

Todo se guarda con `localStorage` **en el navegador donde la abras**. Eso significa:

- Tus datos persisten entre sesiones sin necesidad de internet ni de iniciar sesión en ningún lado.
- Si la abres en otro navegador o dispositivo, empieza vacía — usa **Exportar respaldo** en un lado e **Importar respaldo** en el otro para llevar tu colección contigo.

## 🛠️ Stack

Un solo archivo HTML. Sin frameworks, sin build step:

- HTML + CSS (variables nativas, sin preprocesador)
- JavaScript vanilla
- [AniList GraphQL API](https://anilist.co/graphiql) para la búsqueda
- `localStorage` para persistencia

## 🤝 Contribuciones

Ideas, mejoras o reportes de bugs son bienvenidos vía *issues* o *pull requests*.

## 📄 Licencia

MIT — usa, copia y modifica libremente.
