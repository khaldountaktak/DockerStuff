import http.server
import socketserver

class MyHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(b"Hello, World!")

PORT = 8000

with socketserver.TCPServer(("", PORT), MyHandler) as httpd:
    print(f"Server running on port {PORT}")
    httpd.serve_forever()

{
  "fqdns": "",
  "id": "/subscriptions/c233457e-0826-4b52-ace7-6340ca5e4107/resourceGroups/lampGroup/providers/Microsoft.Compute/virtualMachines/LampVM",
  "location": "westeurope",
  "macAddress": "00-0D-3A-44-15-83",
  "powerState": "VM running",
  "privateIpAddress": "10.0.0.4",
  "publicIpAddress": "20.4.27.107",
  "resourceGroup": "lampGroup",
  "zones": ""
}
