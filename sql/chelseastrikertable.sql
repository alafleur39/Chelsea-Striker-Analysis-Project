-- CREATE DATABASE chelsea_striker_analysis;
USE chelsea_striker_analysis;strikers
DROP TABLE IF EXISTS strikers;

CREATE TABLE strikers (
    striker_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    club VARCHAR(100),
    goals INT,
    shots INT,
    shots_on_target INT,
    shot_distance FLOAT,
    xG FLOAT,
    npxG FLOAT,
    nineties_played FLOAT,
    season VARCHAR(10)
);

