# HTTP JSON database server
A JSON database based on Python http server. It's useful when building a IoT project.
## Usage
To run the server, simply execute the Python script.
```
python3 server.py
```
Upload parameter by HTTP GET query string
```
http://127.0.0.1:9693/?key=value
```
Get JSON
```
http://127.0.0.1:9693/get_json
```
Get JSON then update parameter
```
http://127.0.0.1:9693/get_json?key=value_new
```
Run the server automaticlly by systemd
```
sudo cp python-http-server.service /etc/systemd/system/
sudo systemctl daemon-reload
systemctl enable example.service
```