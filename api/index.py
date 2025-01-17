import json
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs

students_data = [
  {"name": "nk", "marks": 0},
  {"name": "gy5", "marks": 81},
  {"name": "iWe7ZbxL", "marks": 45},
  {"name": "xdBaFxD", "marks": 93},
  {"name": "cLrfH", "marks": 1},
  {"name": "v3AijVSei", "marks": 32},
  {"name": "GvW9F", "marks": 64},
  {"name": "gcVimc", "marks": 68},
  {"name": "rrlA", "marks": 11},
  {"name": "IumveD", "marks": 49},
  {"name": "C9YmYWJ7f", "marks": 83},
  {"name": "B", "marks": 97},
  {"name": "WihpK", "marks": 20},
  {"name": "SC7hEt8N", "marks": 74},
  {"name": "edJ59G", "marks": 83},
  {"name": "Y", "marks": 89},
  {"name": "9iq8r", "marks": 0},
  {"name": "s", "marks": 25},
  {"name": "6dNzHEO", "marks": 91},
  {"name": "Gvtrqf", "marks": 9},
  {"name": "Gpqqk7W", "marks": 58},
  {"name": "ZDNEp31a", "marks": 36},
  {"name": "pFlBLTb1N", "marks": 58},
  {"name": "gQF5pE", "marks": 80},
  {"name": "qDON", "marks": 52},
  {"name": "ySOPVNRtt", "marks": 40},
  {"name": "T1dUAMn", "marks": 10},
  {"name": "Cm", "marks": 25},
  {"name": "W2Ymg5", "marks": 10},
  {"name": "hQ", "marks": 40},
  {"name": "4FIS", "marks": 75},
  {"name": "5dezXtzpz", "marks": 62},
  {"name": "EkZYySZ9", "marks": 27},
  {"name": "g60govs", "marks": 51},
  {"name": "ng7E", "marks": 2},
  {"name": "je0FhYZZ7F", "marks": 33},
  {"name": "xR3odJiG", "marks": 58},
  {"name": "O", "marks": 2},
  {"name": "1n", "marks": 13},
  {"name": "mmCO6QSp", "marks": 13},
  {"name": "Hu5d1OneAU", "marks": 10},
  {"name": "rtiziwuG9", "marks": 12},
  {"name": "1Klh2GuV0H", "marks": 26},
  {"name": "T1b0IEuKc", "marks": 47},
  {"name": "wO8Vxwj6", "marks": 63},
  {"name": "625d6BHXhP", "marks": 36},
  {"name": "I", "marks": 90},
  {"name": "U7vthT", "marks": 89},
  {"name": "XJG6y", "marks": 97},
  {"name": "5oOPruL", "marks": 82},
  {"name": "9A", "marks": 1},
  {"name": "6lRjZ", "marks": 0},
  {"name": "CFhMH", "marks": 73},
  {"name": "26XN1VJutB", "marks": 60},
  {"name": "Pb", "marks": 6},
  {"name": "6Nv6L", "marks": 65},
  {"name": "84X", "marks": 20},
  {"name": "pYt", "marks": 95},
  {"name": "x", "marks": 97},
  {"name": "cCrIba2r", "marks": 24},
  {"name": "pU3uKHZ", "marks": 82},
  {"name": "Bk", "marks": 84},
  {"name": "MZqQF", "marks": 28},
  {"name": "afrC", "marks": 93},
  {"name": "ORZ", "marks": 1},
  {"name": "SBlX", "marks": 28},
  {"name": "Nu", "marks": 31},
  {"name": "z", "marks": 10},
  {"name": "s", "marks": 95},
  {"name": "2dCH", "marks": 15},
  {"name": "56poe", "marks": 5},
  {"name": "2Eukjk591", "marks": 9},
  {"name": "XZF", "marks": 72},
  {"name": "4XA5HgjJ", "marks": 98},
  {"name": "T5UdZsR9k", "marks": 45},
  {"name": "EiK", "marks": 45},
  {"name": "kTe", "marks": 58},
  {"name": "UhesW", "marks": 90},
  {"name": "HA9f7pnRSn", "marks": 42},
  {"name": "bRVx", "marks": 80},
  {"name": "qoxft", "marks": 22},
  {"name": "AFJt5V", "marks": 4},
  {"name": "k1BXS9eqoO", "marks": 69},
  {"name": "IRYdxk2ww", "marks": 5},
  {"name": "YNdE", "marks": 97},
  {"name": "0eDSoHzDW1", "marks": 47},
  {"name": "svwx", "marks": 16},
  {"name": "rBW", "marks": 15},
  {"name": "c0tIM1M", "marks": 51},
  {"name": "FIVKqP2", "marks": 79},
  {"name": "W", "marks": 40},
  {"name": "MpksTm", "marks": 17},
  {"name": "jGIe", "marks": 34},
  {"name": "Hnqo", "marks": 38},
  {"name": "Zc4", "marks": 39},
  {"name": "XFdmSAP", "marks": 27},
  {"name": "vKDiR", "marks": 49},
  {"name": "EQxUz", "marks": 90},
  {"name": "uq", "marks": 7},
  {"name": "I93zNDORY", "marks": 10}
];

class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Parse the query string
        query_components = parse_qs(urlparse(self.path).query)

        # Check the path and handle accordingly
        if self.path.startswith('/api'):
            self.handle_api(query_components)
        else:
            self.handle_home()

    def handle_home(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        response = {"message": "Hello!"}
        self.wfile.write(json.dumps(response).encode('utf-8'))

    def handle_api(self, query_components):
        names = query_components.get('name', [])
        marks = [student['marks'] for student in students_data if student['name'] in names]

        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        response = {"marks": marks}
        self.wfile.write(json.dumps(response).encode('utf-8'))

def run(server_class=HTTPServer, handler_class=RequestHandler, port=8000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f"Server running on port {port}")
    httpd.serve_forever()

if __name__ == "__main__":
    run()