SELECT DISTINCT tweets.pk, tweets.users_pk, tweets.username, tweets.content, image_pathname, ipfs_hash, tweets.time
FROM tweets
JOIN users_followed
ON users_followed.followed_pk =  tweets.users_pk
WHERE users_followed.users_pk = 1
UNION ALL
SELECT * FROM tweets WHERE users_pk = 1
ORDER BY time DESC;





-- row_place.append(row["pk"]) 
-- row_place.append(row["users_pk"])
-- row_place.append(row["username"])
-- row_place.append(row["content"]) 
-- row_place.append(row["time"]) 