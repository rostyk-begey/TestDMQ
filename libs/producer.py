import requests


class Producer:
    def __init__(self, servers):
        self.servers = servers

    def send(self, key, data):
        for server, port in self.servers:
            route = '/'

            r = requests.post(server + ':' + port + route, json={key: data})


if __name__ == '__main__':
    producer = Producer(servers=[('http://127.0.0.1', '5000')])

    for i in range(15):
        message = {
            "text": "Message " + str(i)
        }

        producer.send('messages', message)
