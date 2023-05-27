/* Sentencias para crear la base de datos (Solo se requiere una vez) */
DROP TABLE IF EXISTS urls;

CREATE TABLE urls (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    creado TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    url_original TEXT NOT NULL,
    clicks INTEGER NOT NULL DEFAULT 0
);
