import random
import socketserver
import urllib.parse  # Built-in library to parse/build query strings

from django.core.management.base import BaseCommand


class MyTCPHandler(socketserver.StreamRequestHandler):
    """
    Reads a newline-terminated URL query string carrying the authorization
    request, then randomly authorizes, rejects, or times out the payment 
    """

    def handle(self):
        raw_data = self.rfile.readline(10000).rstrip()
        query_string = raw_data.decode("utf-8")
        request = dict(urllib.parse.parse_qsl(query_string))
        print(f"[*] Authorization request: {request}")

        outcome = random.choice(["yes", "no", "timeout"])
        if outcome == "timeout":
            response = {"status": "timeout"}
        elif outcome == "yes":
            response = {"status": "accepted"}
        else:
            response = {"status": "rejected"}
        response_string = urllib.parse.urlencode(response) + "\n"
        self.wfile.write(response_string.encode("utf-8"))
        print(f"[*] Decision: {response['status']}")


class ThreadedTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    allow_reuse_address = True


class Command(BaseCommand):
    def handle(self, *args, **options):
        HOST, PORT = "0.0.0.0", 9999
        self.stdout.write(f"Bank TCP listener running on {HOST}:{PORT}")
        with ThreadedTCPServer((HOST, PORT), MyTCPHandler) as server:
            server.serve_forever()
