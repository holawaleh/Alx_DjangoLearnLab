API Documentation

🔹 Posts

GET /api/posts/
Retrieve a list of posts. Supports search via ?search=keyword.
Response:

[
{
"id": 1,
"author": "john",
"title": "First Post",
"content": "Hello world!",
"image": null,
"created_at": "2025-09-01T08:00:00Z",
"updated_at": "2025-09-01T08:00:00Z",
"comments_count": 2
}
]

POST /api/posts/ (Auth required)
Request:
{
"title": "My New Post",
"content": "This is a post with some text."
}

Response:

{
"id": 2,
"author": "alice",
"title": "My New Post",
"content": "This is a post with some text.",
"image": null,
"created_at": "2025-09-01T09:10:00Z",
"updated_at": "2025-09-01T09:10:00Z",
"comments_count": 0
}

GET /api/posts/<id>/
Retrieve details of a single post.

PUT /api/posts/<id>/ (Auth required, owner only)
Update post.

DELETE /api/posts/<id>/ (Auth required, owner only)
Delete post.

🔹 Comments

GET /api/posts/<post_id>/comments/
List all comments for a post.
Response:

[
{
"id": 1,
"author": "john",
"post": 2,
"content": "Nice post!",
"created_at": "2025-09-01T09:20:00Z",
"updated_at": "2025-09-01T09:20:00Z"
}
]

POST /api/posts/<post_id>/comments/ (Auth required)
Request:

{
"content": "This is a comment."
}

Response:

{
"id": 2,
"author": "alice",
"post": 2,
"content": "This is a comment.",
"created_at": "2025-09-01T09:30:00Z",
"updated_at": "2025-09-01T09:30:00Z"
}
