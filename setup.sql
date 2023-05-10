DROP TABLE IF EXISTS books;

CREATE TABLE books (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    title TEXT NOT NULL,
    summary TEXT NOT NULL,
    count INTEGER NOT NULL
);

INSERT INTO books (title, summary, count) VALUES ('Harry Potter', 'My Summary', '3');
INSERT INTO books (title, summary, count) VALUES ('Mus', 'The genus Mus or typical mice refers to a specific genus of muroid rodents, all typically called mice (the adjective "muroid" comes from the word "Muroidea", which is a large superfamily of rodents, including mice, rats, voles, hamsters, gerbils, and many other relatives). They are the only members of the tribe Murini.', '3');
INSERT INTO books (title, summary, count) VALUES ('Data', 'data is a collection of discrete values that convey information, describing quantity, quality, fact, statistics, ...', '3');
