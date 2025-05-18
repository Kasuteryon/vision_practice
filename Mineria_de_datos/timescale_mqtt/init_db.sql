CREATE EXTENSION IF NOT EXISTS timescaledb;

CREATE TABLE IF NOT EXISTS dht_readings (
    time        TIMESTAMPTZ       NOT NULL,
    temperature DOUBLE PRECISION  NOT NULL,
    humidity    DOUBLE PRECISION  NOT NULL
);

SELECT create_hypertable('dht_readings', 'time', if_not_exists => TRUE);