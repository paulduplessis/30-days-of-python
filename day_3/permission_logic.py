is_active, is_staff, is_owner = True, True, False

can_edit = is_active and (is_staff or is_owner)

print("can_edit =", can_edit)

# This version gives the wrong answer if is_staff is true and is_active is false because and is 
# evaluated before or, so even if is_owner and is_active = False then if is_staff is True the whole
# expression is True
buggy_can_edit = is_staff or is_owner and is_active
