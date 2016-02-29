def wsgi_application(environ, start_respons);
    status = '200';
    headers = [
        ('Content-Type', 'text/plain')
    ]
    body = 'Hello World';
    start_response(status, headers);
    return [ body ]
