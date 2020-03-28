from R_ev3dev import server
from optparse import OptionParser


if __name__ == "__main__":
    parser = OptionParser()
    parser.add_option("-H", "--host", dest="host", default='', 
                      help="host (default is '')")
    parser.add_option("-p", "--port", dest="port", default=9999, 
                      help="port (default is 9999)")
    parser.add_option("-c", "--max-clients", dest="max_clients", default=1,
                      help="max count of clients allowed (default is 1)")
    (options, _) = parser.parse_args()

    s = server(host=options.host,
               port=int(options.port),
               buffer_size=2048,
               max_clients=int(options.max_clients))
    s.run()
