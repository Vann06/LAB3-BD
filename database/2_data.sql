-- data.sql

-- Inserción de datos en la tabla "tipo_evento"
INSERT INTO tipo_evento (nombre, descripcion) VALUES 
('Conferencia', 'Eventos de carácter académico y profesional'),
('Taller', 'Actividades prácticas para el desarrollo de habilidades'),
('Seminario', 'Sesiones de profundización sobre temas específicos'),
('Hackathon', 'Maratón de desarrollo colaborativo de software'),
('Exposición', 'Muestras de proyectos o trabajos'),
('Debate', 'Discusión organizada sobre temas controversiales'),
('Networking', 'Eventos para establecer conexiones profesionales');

-- Inserción de datos en la tabla "eventos"
INSERT INTO eventos (nombre, descripcion, fecha, id_tipo_evento) VALUES 
('Conferencia IA 2025', 'Exploración de tendencias en inteligencia artificial', '2025-06-15', 1),
('Taller de Desarrollo Web', 'Introducción a tecnologías web modernas', '2025-06-20', 2),
('Seminario de Base de Datos', 'Optimización y nuevas tecnologías en BBDD', '2025-07-05', 3),
('DataHack 2025', 'Hackathon enfocado en ciencia de datos', '2025-07-10', 4),
('Expo Proyectos UVG', 'Muestra anual de proyectos estudiantiles', '2025-08-01', 5),
('Debate: Ética en IA', 'Dilemas éticos en el desarrollo de IA', '2025-08-15', 6),
('Connect Tech 2025', 'Evento de networking para profesionales IT', '2025-09-01', 7),
('Workshop PostgreSQL', 'Taller avanzado de PostgreSQL', '2025-09-10', 2),
('Conferencia Ciberseguridad', 'Tendencias en seguridad informática', '2025-09-20', 1),
('Seminario Cloud Computing', 'Arquitecturas cloud modernas', '2025-10-05', 3),
('Hackathon IoT', 'Desarrollo de soluciones IoT', '2025-10-15', 4),
('Exposición Startups', 'Muestra de startups tecnológicas', '2025-11-01', 5),
('Taller Machine Learning', 'Aplicaciones prácticas de ML', '2025-11-15', 2);

-- Inserción de datos en la tabla "participantes"
INSERT INTO participantes (nombre, apellido, correo) VALUES 
('Ana', 'García', 'ana.garcia@mail.com'),
('Carlos', 'Rodríguez', 'carlos.rodriguez@mail.com'),
('María', 'López', 'maria.lopez@mail.com'),
('Juan', 'Martínez', 'juan.martinez@mail.com'),
('Laura', 'Hernández', 'laura.hernandez@mail.com'),
('Pedro', 'González', 'pedro.gonzalez@mail.com'),
('Sofia', 'Díaz', 'sofia.diaz@mail.com'),
('Miguel', 'Sánchez', 'miguel.sanchez@mail.com'),
('Elena', 'Torres', 'elena.torres@mail.com'),
('David', 'Ramírez', 'david.ramirez@mail.com'),
('Lucía', 'Flores', 'lucia.flores@mail.com'),
('Daniel', 'Gómez', 'daniel.gomez@mail.com'),
('Carmen', 'Vásquez', 'carmen.vasquez@mail.com'),
('Jorge', 'Castro', 'jorge.castro@mail.com'),
('Patricia', 'Morales', 'patricia.morales@mail.com'),
('Roberto', 'Vargas', 'roberto.vargas@mail.com'),
('Susana', 'Ortiz', 'susana.ortiz@mail.com'),
('Felipe', 'Mendoza', 'felipe.mendoza@mail.com'),
('Gabriela', 'Pérez', 'gabriela.perez@mail.com'),
('Andrés', 'Navarro', 'andres.navarro@mail.com');

-- Inserción de datos en la tabla "estado_inscripcion"
INSERT INTO estado_inscripcion (nombre) VALUES 
('Pendiente'),
('Confirmado'),
('Cancelado'),
('En lista de espera'),
('Asistió');

-- Inserción de datos en la tabla "eventos_participantes"
-- Algunas personas participan en mas de un evento
INSERT INTO eventos_participantes (id_evento, id_persona, id_estado_inscripcion) VALUES 
(1, 1, 2), 
(8, 1, 5), 
(12, 1, 2), 


(2, 2, 5), 
(4, 2, 5), 
(8, 2, 2), 
(13, 2, 2), 
(1, 3, 5), 
(3, 3, 5), 


(4, 4, 5), 
(7, 4, 2), 
(11, 4, 1), 

(3, 5, 5), 
(13, 5, 2), 

(5, 6, 5), 
(6, 7, 5), 
(9, 8, 2), 
(10, 9, 2), 
(2, 10, 5), 
(5, 11, 5), 
(7, 12, 2), 
(12, 13, 4), 
(6, 14, 3), 
(10, 15, 1), 
(11, 16, 2), 
(9, 17, 1), 
(4, 18, 2), 
(5, 19, 5),
(8, 20, 4), 
(1, 6, 5), 
(6, 10, 5), 
(13, 12, 2), 
(9, 14, 1); 
