from cgi import parse_qs
from tempalte2 import html




def application(environ, start_response):
        d = parse_qs(environ['QUERY_STRING'])
        a = d.get('a', [''])[0]
        b = d.get('b', [''])[0]

        sum = 0
        multi = 0
	txt = ''
	Message = {'success': 'SUCCESS!', 'ValueError' : 'ONLY NUMBER!'}
	if '' not in [a,b]:
		try:
        	        a,b = float(a) ,float(b)
                	sum = a + b
                	multi = a * b
			txt = Message['success']
		except ValueError:
			txt = Message['ValueError']
	else:
		txt = 'Please Enter The Numbers!'

        response_body = html % {
                'sum' : sum,
                'multi' : multi,
		'txt' : txt,
        }

        start_response('200 OK', [
                ('Content-Type', 'text/html'),
                ('Content-Length',str(len(response_body)))
        ])
        return [response_body]
~                                                  
