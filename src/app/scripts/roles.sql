% Сотрудник магазина
CREATE ROLE employee LOGIN PASSWORD 'postgres';
GRANT SELECT ON TABLE "Visitor" TO employee;

% Охрана
CREATE ROLE security LOGIN PASSWORD 'postgres';
GRANT SELECT ON TABLE "Visitor", "Product", "Shelf" TO security;

% Админстратор 
CREATE ROLE administrator LOGIN PASSWORD 'postgres';
GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public TO administrator;
