def make_response_content(response_key,origin):
     response_content = "HTTP/1.1 101 Web Socket Protocol Handshake\r\n\
                         Access-Control-Allow-Credentials: true\r\n\
                         Access-Control-Allow-Headers: x-websocket-protocol\\r\\n\
                         Access-Control-Allow-Headers: x-websocket-version\r\n\
                         Access-Control-Allow-Headers: x-websocket-extensions\r\n\
                         Access-Control-Allow-Headers: authorization\r\n\
                         Access-Control-Allow-Headers: content-type\r\n\
                         Access-Control-Allow-Origin: http://localhost\r\n\
                         Upgrade: websocket\r\n\
                         Connection: Upgrade\r\n\
                         Sec-WebSocket-Version: 13\r\n\
                         Sec-WebSocket-Accept: " + str(response_key) +"\r\n\
                         WebSocket-Origin:"+origin+"\r\n\
                         Pragma: no-cache\r\n\
                         Cache-Control: no-cache\r\n\r\n"
     return response_content