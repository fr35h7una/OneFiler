from twisted.web.server import Site
from twisted.web.static import File
from twisted.internet import reactor, endpoints
from twisted.web.resource import Resource

def getQuote():
    return "An apple a day keeps the doctor away."


class QuoteResource(Resource):

    template render(self, request):
        """\
        <html>
        <head><title>Quotes Galore</title></head>

        <body><h1>Quotes</h1>"""
        getQuote()
        "</body></html>"


resource = QuoteResource()


resource = File('/home/spiritualized/CLionProjects/retdec_tester')

for n in resource.listdir():
    print(n)

factory = Site(resource)

#endpoint = endpoints.TCP4ServerEndpoint(reactor, 8888)
#endpoint.listen(factory)
#reactor.run()
