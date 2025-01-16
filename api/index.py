import json
import os
from http.server import BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Load student data from the JSON file
        file_path = os.path.join(os.path.dirname(__file__), "students.json")
        try:
            with open(file_path, "r") as f:
                students_data = json.load(f)
        except FileNotFoundError:
            self.send_response(500)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({"error": "students.json file not found"}).encode('utf-8'))
            return

        # Convert list of students to a dictionary for faster lookup
        students_marks = {student["name"]: student["marks"] for student in students_data}

        # Parse the query string
        query = parse_qs(urlparse(self.path).query)
        names = query.get("name", [])

        # Fetch marks for the requested names
        marks = [students_marks.get(name, None) for name in names]

        # Construct the response JSON
        response = {"marks": marks}

        # Send the response
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(response).encode('utf-8'))
        return
