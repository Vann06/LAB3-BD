-- ddl.sql

CREATE TABLE tipo_evento (
  id SERIAL PRIMARY KEY,
  nombre VARCHAR(100) NOT NULL,
  descripcion TEXT
);

CREATE TABLE eventos (
  id SERIAL PRIMARY KEY,
  nombre VARCHAR(100) NOT NULL,
  descripcion TEXT,
  fecha DATE NOT NULL,
  id_tipo_evento INT REFERENCES tipo_evento(id)
);

CREATE TABLE participantes (
  id SERIAL PRIMARY KEY,
  nombre VARCHAR(100) NOT NULL,
  apellido VARCHAR(100) NOT NULL,
  correo VARCHAR(100) UNIQUE
);


CREATE TABLE estado_inscripcion(
  id SERIAL PRIMARY KEY, 
  nombre VARCHAR(100) NOT NULL
);


CREATE TABLE eventos_participantes (
  id SERIAL PRIMARY KEY,
  id_evento INT REFERENCES eventos(id) ON DELETE CASCADE,
  id_persona INT REFERENCES participantes(id) NOT NULL,
  id_estado_inscripcion INT REFERENCES estado_inscripcion(id) NOT NULL
);





-- VIEWS 
CREATE VIEW eventos_resumen AS
SELECT 
    e.id AS id_evento,
    e.nombre AS nombre_evento,
    e.fecha,
    te.nombre AS tipo_evento,
    COUNT(ep.id_persona) FILTER (WHERE ei.nombre = 'Confirmado') AS total_confirmados
FROM eventos e
JOIN tipo_evento te ON e.id_tipo_evento = te.id
LEFT JOIN eventos_participantes ep ON ep.id_evento = e.id
LEFT JOIN estado_inscripcion ei ON ep.id_estado_inscripcion = ei.id
GROUP BY e.id, e.nombre, e.fecha, te.nombre;
