from xmlrpc.server import SimpleXMLRPCServer

# Define functions that clients can call remotely
def get_customer(customer_id):
    # Simulating database lookup
    customers = {
        101: {"name": "John Doe", "email": "john@example.com", "balance": 1500.00},
        102: {"name": "Jane Smith", "email": "jane@example.com", "balance": 2300.50}
    }
    return customers.get(customer_id, {"error": "Customer not found"})

def calculate_total(items):
    return sum(items)

# Create server
server = SimpleXMLRPCServer(("localhost", 8000))
print("Server listening on port 8000...")

# Register functions
server.register_function(get_customer, "get_customer")
server.register_function(calculate_total, "calculate_total")

# Run the server
server.serve_forever()
