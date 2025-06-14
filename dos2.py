# rpc_server.py
from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler
# Restrict to a particular path
class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

# Create server
with SimpleXMLRPCServer(('localhost', 8000),
                        requestHandler=RequestHandler) as server:
    server.register_introspection_functions()

    # Function to add two numbers remotely
    def add(x, y):
        return x + y

    # Register the function
    server.register_function(add, 'add')

    # Run the server
    print("Server listening on port 8000...")
    server.serve_forever()
