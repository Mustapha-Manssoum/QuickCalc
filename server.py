import http.server
from urllib.parse import urlparse, parse_qs
import os


# HTTP request handler
class MyHttpRequestHandler(http.server.SimpleHTTPRequestHandler):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=os.path.join(os.getcwd(), 'static'), **kwargs)

    # Handle Get request:
    def do_GET(self) -> None:
        parsed_url = urlparse(self.path)
        query_params = parse_qs(parsed_url.query)

        try:

            if parsed_url.path == '/calcul':

                # retrieve values from the query parameters
                operand1 = query_params.get('operand1', [None])[0]
                operation = query_params.get('operation',[None])[0]
                operand2 = query_params.get('operand2', [None])[0]

                result = None
                
                # Process the calculations
                if operand1 and operation and operand2:
                    if operation == '+':
                        result = float(operand1) + float(operand2)
                    elif operation == '-':
                        result = float(operand1) - float(operand2)
                    elif operation == '*':
                        result = float(operand1) * float(operand2)
                    elif operation == '/':
                        if float(operand2) == 0:
                            result = f"Error: Division by Zero"
                        else:
                            result = float(operand1) / float(operand2)

                # send the response back to the client
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(f"{result}".encode())

            else:
                # Serve static files in the current directory
                return super().do_GET()
            
        except Exception as e:
            self.send_error(500, f"Internal Server Error: {e}")


if __name__ == '__main__':
    server_address = ('localhost', 8000)
    httpd = http.server.HTTPServer(server_address, MyHttpRequestHandler)
    print('Server running on port 8000')
    httpd.serve_forever()