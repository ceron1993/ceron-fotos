# Cerón Fotos Prediales

App para tomar fotos de predios por manzana o vereda. Crea la carpeta (MZ-3, VDA-EL GUAMO…), los predios P-1, P-2… y renombra cada foto sola: `MZ-3 P-1.jpg`, `MZ-3 P-1_2.jpg`. Exporta un ZIP con subcarpetas por predio y un resumen CSV (fecha, GPS, nota).

- `www/` → la app web (también sirve tal cual para Netlify).
- `.github/workflows/build-apk.yml` → compila el APK automáticamente en cada cambio.

## Descargar el APK
Pestaña **Actions** → espere el check verde → pestaña **Releases** → `CeronFotos.apk`.
