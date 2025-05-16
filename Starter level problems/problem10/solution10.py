data_list = [13, 24, 'Karim', {'name': 'guru'}, 45, 17]
cleaned_list = [item for item in data_list if isinstance(item, int)]
print("Cleaned list:", cleaned_list)