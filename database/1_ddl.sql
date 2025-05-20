-- ddl.sql

CREATE TABLE eventos (
  id SERIAL PRIMARY KEY,
  nombre VARCHAR(100) NOT NULL,
  descripcion TEXT,
  fecha DATE NOT NULL,
  id_tipo_evento INT REFERENCES tipo_evento(id)
);

CREATE TABLE tipo_evento (
  id SERIAL PRIMARY KEY,
  nombre VARCHAR(100) NOT NULL,
  descripcion TEXT
);

CREATE TABLE participantes (
  id SERIAL PRIMARY KEY,
  nombre VARCHAR(100) NOT NULL,
  apellido VARCHAR(100) NOT NULL,
  correo VARCHAR(100) UNIQUE
);

CREATE TABLE eventos_participantes (
  id SERIAL PRIMARY KEY,
  id_evento INT REFERENCES eventos(id) ON DELETE CASCADE,
  id_persona INT REFERENCES participantes(id) NOT NULL,
  id_estado_inscripcion INT REFERENCES estado_inscripcion(id) NOT NULL
);

CREATE TABLE estado_inscripcion(
  id SERIAL PRIMARY KEY, 
  nombre VARCHAR(100) NOT NULL
);
