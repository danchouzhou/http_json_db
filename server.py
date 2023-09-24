import http.server
from urllib.parse import urlparse
import json

PORT = 9693
j_dict = {}

class Handler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        p = urlparse(self.path).path
        print(p)
        
        if (p == "/get_json"): 
            self.send_response(200)
            self.send_header('Content-type','application/json')
            self.end_headers()
            self.wfile.write(json.dumps(j_dict).encode('utf-8')) # Dictionary to string

        else : 
            self.send_response(200)
            self.send_header('Content-type','text/html')
            self.end_headers()
            f = open("index.html", "r")
            self.wfile.write(f.read(-1).encode('utf-8'))
            f.close()

        # HTTP GET to JSON
        q = urlparse(self.path).query
        # print(q)
        try: 
            r = {}
            for s in q.split("&"):
                # print(s)
                t = s.split("=")
                # print(t)
                r[t[0]] = t[1]
            # print(r)
            j_dict.update(r)
        except Exception as e:
            print('Error occurred.', e)

try: 
    httpd = http.server.ThreadingHTTPServer(('', PORT), Handler)
    print("serving at port", PORT)
    httpd.serve_forever()
except Exception as e:
    print('Error occurred.', e)
except KeyboardInterrupt:
    httpd.shutdown()
