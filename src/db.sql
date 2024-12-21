CREATE TABLE IF NOT EXISTS semestre (
    id INT PRIMARY KEY AUTO_INCREMENT,
    grado INT,
    nombre VARCHAR(30)
);

CREATE TABLE IF NOT EXISTS asignatura (
    id INT PRIMARY KEY AUTO_INCREMENT, 
    id_semestre INT,
    nombre VARCHAR(255),
    Foreign Key (id_semestre) REFERENCES semestre (id)
);


CREATE TABLE IF NOT EXISTS calificacion (
    id INT PRIMARY KEY AUTO_INCREMENT,
    id_asignatura INT,
    nota FLOAT,
    FOREIGN KEY (id_asignatura) REFERENCES asignatura (id)
);


INSERT INTO semestre (grado, nombre) VALUES 
    (1, "Primero"), 
    (2, "Segundo"), 
    (3, "Tercero"), 
    (4, "Cuarto"), 
    (5, "Quinto"), 
    (6, "Sexto"), 
    (7, "Septimo"), 
    (8, "Octavo"), 
    (9, "Noveno")
;

INSERT INTO asignatura (id_semestre, nombre) VALUES
    (1, "Algebra lineal"),
    (1, "Fundamentos de programación"),
    (1, "Cálculo de una variable"),
    (2, "Programación orientada a objetos"),
    (2, "Fundamentos de ingenieria de software"),
    (2, "Sistemas operativos"),
    (3, "Estadística"),
    (3, "Estructura de datos"),
    (3, "Administración de sistemas operativos"),
    (4, "Redes de computadoras"),
    (4, "Desarrollo basado en plataformas"),
    (4, "Bases de datos"),
    (5, "Técnicas de simulación"),
    (5, "Desarrollo de apliciones web"),
    (5, "Administración de base de datos"),
    (6, "Lógica difusa"),
    (6, "Aplicaciones móviles"),
    (6, "Control de calidad del software"),
    (7, "Sistemas inteligentes"),
    (7, "Sistemas de juegos"),
    (7, "Técnicas avanzadas de despliegue"),
    (8, "Computación en la nube"),
    (8, "Arquitecturas empresariales"),
    (8, "Emprendimiento e innovación"),
    (9, "Auditoría informática"),
    (9, "Gestión de proyectos de software"),
    (9, "Practicas laborales")  
;