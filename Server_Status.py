# Server status check

server_status = "running" # change this to "stopped" or "down" for testing

if server_status == "running":
    print("Server is running smoothly")

elif server_status == "stopped":
    print("Server is stopped!! Please start the service.")

else:
    print("Server is down!! Immediate action required.")
    