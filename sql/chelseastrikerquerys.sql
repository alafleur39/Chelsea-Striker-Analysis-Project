-- updated chelsea striker analysis
USE chelsea_strikers_analysis;
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

SELECT * FROM strikers LIMIT 10; -- this is how i check to see if my new table has been inserted 

SELECT name, club, goals
FROM strikers
ORDER BY goals DESC
LIMIT 10;
-- most efficient finishers 
SELECT name, club, goals, shots,
       ROUND(goals / shots, 2) AS goal_conversion
FROM strikers
WHERE shots >= 20
ORDER BY goal_conversion DESC
LIMIT 10;
-- highest xG per shot
SELECT name, club, xG, shots,
       ROUND(xG / shots, 2) AS xG_per_shot
FROM strikers
WHERE shots >= 20
ORDER BY xG_per_shot DESC
LIMIT 10;

-- shortest Shot distance 
SELECT name, club, shot_distance, goals
FROM strikers
WHERE shots >= 20
ORDER BY shot_distance ASC
LIMIT 10;

-- data for our shortlisted players 
SELECT name, club, goals, shots,
       ROUND(goals / shots, 4) AS goal_conversion,
       xG,
       ROUND(xG / shots, 4) AS xG_per_shot,
       shot_distance
FROM strikers
WHERE name IN (
  'Goncalo Ramos',
  'Jonathan David',
  'Myron Boadu',
  'Emanuel Emegha',
  'Chris Wood',
  'Mika Biereth',
  'Mateo Retegui'
);
