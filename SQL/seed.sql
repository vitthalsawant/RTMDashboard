
DELETE FROM alerts;
DELETE FROM equipment;

INSERT INTO equipment (name, status, temperature, production) VALUES
    ('Machine A', 'Running',     72.5, 1500.00),
    ('Machine B', 'Stopped',     45.0,  800.00),
    ('Machine C', 'Running',     68.3, 2100.00),
    ('Machine D', 'Maintenance', 55.1,  300.00),
    ('Machine E', 'Running',     80.2, 1750.00),
    ('Machine F', 'Stopped',     40.0,  500.00),
    ('Machine G', 'Running',     74.8, 1900.00),
    ('Machine H', 'Running',     69.0, 2200.00),
    ('Machine I', 'Maintenance', 60.5,  100.00),
    ('Machine J', 'Stopped',     38.5,  700.00);


INSERT INTO alerts (equipment_id, message) VALUES
    (2,  'Machine B stopped unexpectedly'),
    (4,  'Machine D under scheduled maintenance'),
    (6,  'Machine F temperature below threshold'),
    (9,  'Machine I awaiting spare parts'),
    (10, 'Machine J shutdown for inspection');


SELECT * FROM equipment ORDER BY id;
SELECT * FROM alerts ORDER BY id;






