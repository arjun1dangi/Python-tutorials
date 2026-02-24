def http_status(status):
    match status:
        case 200:
            return"OK"
        case 200:
            return"oooK"
        case 405:
            return"not found"
        case 500:
            return"internal server error"
        case _:
            return"unknown status"
            
user_input = int(input("Enter HTTP status code: "))

print(http_status(user_input))


