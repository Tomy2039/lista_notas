const fs = require("fs");
const path = require("path");

// Ruta del archivo JSON dentro de la carpeta "data"
const jsonPath = path.join(__dirname, "../data/datos.json");

// Leer los datos desde el archivo JSON
const data = fs.readFileSync(jsonPath, "utf8");
const personas = JSON.parse(data);

// Ordenar los datos por nota de mayor a menor
personas.sort((a, b) => b[2] - a[2]);

console.log("\nLista ordenada por nota (de mayor a menor) en JavaScript:");
console.table(personas);
