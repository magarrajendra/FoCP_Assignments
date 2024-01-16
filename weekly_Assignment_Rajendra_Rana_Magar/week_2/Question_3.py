total_students = int(input("How many students? "))
group_size = int(input("Required group size? "))

num_groups = total_students // group_size
remaining_students = total_students % group_size

group_plural = "groups" if num_groups != 1 else "group"
students_plural = "students" if remaining_students != 1 else "student"
print(f"There will be {num_groups} {group_plural} with"
      f" {remaining_students} {students_plural} left over.")
