CREATE TABLE equipment (
    id          SERIAL PRIMARY KEY,
    name        VARCHAR(100)  NOT NULL,
    status      VARCHAR(50)   NOT NULL,   -- Allowed values: Running, Stopped, Maintenance
    temperature NUMERIC(6,2),
    production  NUMERIC(10,2)
);




CREATE TABLE alerts (
    id           SERIAL PRIMARY KEY,
    equipment_id INTEGER NOT NULL,
    message      VARCHAR(255) NOT NULL,
    CONSTRAINT fk_equipment
        FOREIGN KEY (equipment_id)
        REFERENCES equipment(id)
        ON DELETE CASCADE
);