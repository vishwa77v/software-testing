# rpc_client.py
import xmlrpc.client

# Create server proxy
proxy = xmlrpc.client.ServerProxy("http://localhost:8000/RPC2")

# Remote function call
result = proxy.add(15, 5)
print(f"Result of remote addition: {result}")
