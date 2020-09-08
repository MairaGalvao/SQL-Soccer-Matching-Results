SELECT team, Sum (scored) Scored, Sum (received) Received, Sum (goaldiff) GoalDiff, Sum (points) Points FROM (SELECT team, scored, received, ( scored - received ) GoalDiff, points FROM (SELECT*, CASE WHEN ( scored > received ) THEN 3 WHEN ( scored = received ) THEN 1 ELSE 0 end AS Points FROM (SELECT hometeam team,

homescore scored, awayscore received FROM matches UNION ALL SELECT awayteam team, awayscore scored, homescore received FROM matches))) GROUP BY team ORDER BY points DESC, goaldiff DESC
