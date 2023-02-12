def defang(s:str):
    s = s.replace(".", "[.]")
    return s

test = "172.16.192.14"
print(defang(test))