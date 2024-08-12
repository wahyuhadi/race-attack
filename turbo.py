def queueRequests(target, wordlists):
    engine = RequestEngine(endpoint=target.endpoint,
                           concurrentConnections=20,
                           requestsPerConnection=100,
                           pipeline=False,
                           maxRetriesPerRequest=0,
                           engine=Engine.THREADED
                           )
    for i in range (0, 1000):
        engine.queue(target.req)



def handleResponse(req, interesting):
    table.add(req)

