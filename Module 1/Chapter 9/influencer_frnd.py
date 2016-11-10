friends = fb.get_connections("me", "friends")["data"]
print friends
for frd in friends:
    print fb.get_connections(frd["id"],"friends")
