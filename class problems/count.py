posts = [
    {"user": "alice", "post": "Hai"},
    {"user": "bob", "post": "hello"},
    {"user": "alice", "post": "Hai"},
    {"user": "bob", "post": "hello"},
    {"user": "john", "post": "Hai"}
]


post_counts = {}


for entry in posts:
    post_text = entry["post"]
    if post_text in post_counts:
        post_counts[post_text] += 1
    else:
        post_counts[post_text] = 1



print(post_counts)