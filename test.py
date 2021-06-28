s2 = input().lower(); s2reverse = ""
for i in range(len(s2)):
    s2reverse += (s2[len(s2) -i -1])
print("Yes" if s2 == s2reverse else "No")