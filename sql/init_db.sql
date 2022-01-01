CREATE TABLE IF NOT EXISTS signals (
    id serial PRIMARY KEY,
    datetime TIMESTAMP,
    sensor int,
    value float
);
