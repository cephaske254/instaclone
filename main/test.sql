SELECT "main_post"."id",
    "main_post"."image",
    "main_post"."caption",
    "main_post"."user_id",
    "main_post"."date"
FROM "main_post"
    INNER JOIN "auth_user" ON ("main_post"."user_id" = "auth_user"."id")
    INNER JOIN "main_follower" ON ("auth_user"."id" = "main_follower"."user_id")
WHERE "main_follower"."id" = 1