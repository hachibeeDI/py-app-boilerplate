## Setup

```sh
$ python --version
Python 3.6.x

$ python -m venv .venv
$ pip install -r requirements.txt
```


## Register your function as JSON_-RPC

```python
# rpc/example/foo.py


def hoge_func(x, y):
    return x + y
```


## Run

```sh
$ python run.py
DEBUG:__main__:register RPC example.foo.hoge_func
...
```


### Confirm

```sh
$ curl -i -X POST "http://localhost:8888/rpc" -d '{"jsonrpc": "2.0", "method": "example.foo.hoge_func", "params": {"x": 1, "y":20}, "id": "111"}'
HTTP/1.1 200 OK
Server: TornadoServer/5.0.1
Content-Type: application/json
Date: Wed, 28 Mar 2018 02:27:06 GMT
Content-Length: 45

{"jsonrpc": "2.0", "result": 21, "id": "111"}
```

:clap:
