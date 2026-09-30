item, qty, price = "Mechanical keyboard", 2, 1249.9

total = qty * price

total_str = "R" + f"{total:,.2f}"

print(f"{item:<22}{qty:>4}{total_str:>12}")

print(f"{item[::-1]} {item[2::3]}")