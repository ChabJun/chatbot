import http.server

HTTPHandler = http.server.SimpleHTTPRequestHandler

HTTPHandler.extension_map.update ({

    '.m3u8' : 'application/x-xmpegURL',

    '.ts' : 'video/MP2T'

})

httpd = http.server.HTTPServer(('0.0.0.0', 8080), HTTPHandler)

httpd.server_forever()
