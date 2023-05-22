blog_posts = [{"Likes":11, "Comments":22, "Shares":33},{"Photos":3, "Likes": 21, "Comments":2}, {"Likes":13, "Comments":2, "Shares":33}]

total_photos = 0
for post in blog_posts:
    try:
     total_photos = total_photos + post["Photos"]
    except KeyError:
        print("Exception  occured")
        pass
print(total_photos)
