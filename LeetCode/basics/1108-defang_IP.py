def brute(address):
    address = address.replace('.', '[.]')
    return address

address = '172.16.30.20'
print(brute(address))