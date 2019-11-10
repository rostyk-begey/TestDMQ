import requests


class Consumer:
    def __init__(self, server):
        self.host, self.port = server

    def __iter__(self):
        while True:
            route = '/'

            r = requests.get(self.host + ':' + self.port + route)
            if r.status_code == 200:
                yield r.json()


if __name__ == '__main__':
    consumer = Consumer(server=('http://127.0.0.1', '5000'))
    for task in consumer:
        print(task)