COPY "Visitor"(description, location, view, detection)
FROM '/var/lib/postgresql/data/csv_tables/tables/visitor.csv'
DELIMITER ','
CSV HEADER;


COPY "Camera"(location, resolution, rotation, cam_type)
FROM '/var/lib/postgresql/data/csv_tables/tables/camera.csv'
DELIMITER ','
CSV HEADER;

COPY "Shelf"(location, length)
FROM '/var/lib/postgresql/data/csv_tables/tables/shelf.csv'
DELIMITER ','
CSV HEADER;

COPY "Product"(location, name, "dataEnd", weight, status, price)
FROM '/var/lib/postgresql/data/csv_tables/tables/product.csv'
DELIMITER ','
CSV HEADER;


COPY "ChainStore"(location, name, "nameDir", income, consumption)
FROM '/var/lib/postgresql/data/csv_tables/tables/chainStore.csv'
DELIMITER ','
CSV HEADER;
