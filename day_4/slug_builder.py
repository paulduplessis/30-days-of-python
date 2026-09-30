blog_title = input("Enter your blog post title: ").lower()

blog_title = blog_title.split()
blog_title = "-".join(blog_title)

print(blog_title)
print("Longer than 50 characters:", len(blog_title) > 50)
