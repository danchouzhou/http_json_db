import http.server
from urllib.parse import urlparse
import json
import sys

# Default port
PORT = 8000
# Empty JSON dictionary
j_dict = {}

# Get server listing port number or use default port number
try: 
    PORT = int(sys.argv[1])
except Exception as e:
    print('Error while reading port number.', e)
    print('Use default port number:', PORT)

# Read saved JSON db
try:
    f = open('db.json', 'r')
    j_str = f.read()
    f.close()
    j_dict = json.loads(j_str)
except Exception as e:
    print('Error while reading JSON file.', e)
    print('Use empty JSON dictionary.')

class Handler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        p = urlparse(self.path).path
        print(p)
        
        if (p.find("/get_json") != -1): 
            self.send_response(200)
            self.send_header('Content-type','application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            j_str = json.dumps(j_dict) # Dictionary to string
            self.wfile.write(j_str.encode('utf-8'))

        else : 
            self.send_response(200)
            self.send_header('Content-type','text/html')
            self.end_headers()
            f = open("index.html", "r")
            self.wfile.write(f.read(-1).encode('utf-8'))
            f.close()

        # HTTP GET query string to JSON
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
            if (p.find("/append") != -1):
                for k, v in r.items():
                    # Check if key exist
                    if bool(j_dict.get(k)):
                        j_dict[k] += "," + v
                    else :
                        j_dict[k] = v
            else :
                j_dict.update(r)
        except Exception as e:
            print('Error occurred.', e)

try: 
    httpd = http.server.ThreadingHTTPServer(('', PORT), Handler)
    print("serving at port", PORT)
    httpd.serve_forever()
except Exception as e:
    print('Error occurred.', e)
except KeyboardInterrupt: # Stop the server and save JSON db
    httpd.shutdown()
    f = open('db.json', 'w')
    j_str = json.dumps(j_dict)
    f.write(j_str)
    f.close()
