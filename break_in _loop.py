key_location="chair"
location=["sofa","table","chair","garage","closet"]

for loc in location:
    if loc==key_location:
        print("key found at:",loc)
        break
    else:
        print("key not found at:",loc)

print("end")

