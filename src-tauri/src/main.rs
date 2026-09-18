// No se toca casi nunca: Tauri solo usa esto para abrir la ventana y cargar
// tu index.html/style.css tal cual — toda la lógica real de la app sigue
// siendo el HTML/CSS/JS de siempre, no Rust.
#![cfg_attr(not(debug_assertions), windows_subsystem = "windows")]

fn main() {
    tauri::Builder::default()
        .run(tauri::generate_context!())
        .expect("error al iniciar Mi Animeteca");
}
