
with open("data_file.txt","r") as f:
    list_items=f.readlines()
print(list_items)
list_items=[space.strip() for space in list_items]
print(list_items)
    
