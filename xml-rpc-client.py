import xmlrpc.client

# Connect to the remote server
server = xmlrpc.client.ServerProxy("http://localhost:8000")

# Call remote functions as if they were local
customer = server.get_customer(101)
print(f"Customer: {customer['name']}, Balance: ${customer['balance']}")

# Another remote call
total = server.calculate_total([10, 20, 30, 40])
print(f"Total: {total}")
