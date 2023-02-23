CREATE TABLE Movies(
    id INTEGER PRIMARY KEY,
    name TEXT,
    year INTEGER NOT NULL,
    producer VARCHAR(255) NOT NULL,
    director VARCHAR(255) NOT NULL,
    budget INTEGER NOT NULL,
    category VARCHAR(255) NOT NULL
);

INSERT INTO Movies(name, year, producer, director, budget, category) values ("Harry Potter and the Prisoner of Azkaban", 2004, "Chris Columbus", "Alfonso Cuarón", 130000000, "Adventure");

INSERT INTO Movies(name, year, producer, director, budget, category) values ("Passengers", 2016, "Start Motion Pictures", "Morten Tyldum", 110000000, "Romance");

select * from Movies;
