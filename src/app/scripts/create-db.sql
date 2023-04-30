DROP TABLE IF EXISTS visitor CASCADE;
CREATE TABLE IF NOT EXISTS visitor
(
    id INT NOT NULL GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    description text,
    location text,
    view: text,
    detection text,
);
