CREATE TABLE user (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name VARCHAR(45) NOT NULL,
    last_name VARCHAR(45) NOT NULL,
    hobbies TEXT,
    active BOOLEAN NOT NULL DEFAULT 1
);

CREATE TABLE vehicle (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    color VARCHAR (45) NOT NULL,
    license_plate VARCHAR(45) NOT NULL,
    v_type INTEGER NOT NULL,
    user_id INTEGER NOT NULL,
    active BOOLEAN DEFAULT 1,
    FOREIGN KEY (v_type) REFERENCES vehicle_type(id),
    FOREIGN KEY (user_id) REFERENCES user(id)
);

CREATE TABLE vehicle_type(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    description VARCHAR(64)
);

INSERT INTO vehicle_type (description) VALUES ("Airplane")
INSERT INTO vehicle_type (description) VALUES ("Boat")
INSERT INTO vehicle_type (description) VALUES ("Car")


INSERT INTO user (
    first_name,
    last_name,
    hobbies
) VALUES (
    "Jadro",
    "Montes",
    "Sleep"
);

INSERT INTO user (
    first_name,
    last_name,
    hobbies
) VALUES (
    "Andres",
    "Castelo",
    "Gym"
);

INSERT INTO user (
    first_name,
    last_name,
    hobbies
) VALUES (
    "Sammy",
    "Ballesteros",
    "Eat"
);

INSERT INTO vehicle (
    color,
    license_plate,
    v_type,
    user_id
) VALUES(
    "Red",
    "Hello1",
    2,
    1
);

INSERT INTO vehicle (
    color,
    license_plate,
    v_type,
    user_id
) VALUES(
    "Black",
    "Hello2",
    3,
    1
);

INSERT INTO vehicle (
    color,
    license_plate,
    v_type,
    user_id
) VALUES(
    "Green",
    "Hello3",
    4,
    2
);

SELECT user.last_name,
       user.first_name,
       user.hobbies,
       user.active,
       vehicle.license_plate,
       vehicle.color,
       vehicle.v_type AS vehicle_type

FROM user
INNER JOIN vehicle ON user.id = vehicle.user_id
INNER JOIn vehicle_type ON vehicle_type = vehicle_type.id;