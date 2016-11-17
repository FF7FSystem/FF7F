 def app (environ, start_response):
  status = '200 OK'
  response_headers = [('Content-type','text/plain')]
  start_response(status, response_headers)
  resp = environ['QUERY_STRING'].split("&")
  resp = [i+"\n" for i in resp]
  return resp
