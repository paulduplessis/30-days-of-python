total_items, per_page = 47, 10

num_pages = total_items // per_page + (total_items % per_page != 0)

print("Number of pages:", num_pages)

page = int(input("Enter page number to calculate offset: "))

offset = (page - 1) * per_page

print("Offset:", offset)
