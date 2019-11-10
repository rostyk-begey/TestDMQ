from flask import Flask, jsonify, abort, request
from threading import Lock, Condition
from queue import Queue

app = Flask(__name__)


queue = Queue(10)
condition = Condition()


@app.route('/', methods=['GET'])
def get_task():
    global tasks
    global queue
    request.args.get('topic')

    condition.acquire()
    if queue.empty():
        print("Nothing in queue, consumer is waiting")
        condition.wait()
        print("Producer added something to queue and notified the consumer")
    task = queue.get()
    print("Consumed", task)
    condition.release()

    return jsonify(task)


@app.route('/', methods=['POST'])
def store_task():
    global tasks
    global queue

    condition.acquire()

    if not request.json:
        print('abort', request.json)
        abort(400)
    task = request.json

    queue.put(task)

    condition.notify()
    condition.release()
    return jsonify({'response': {"done": True}})


if __name__ == '__main__':
    app.run(debug=True)
