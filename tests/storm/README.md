# locust tests

Docs:
* home: https://locust.io/
* quickstart: https://docs.locust.io/en/stable/quickstart.html
* async requests with locust: https://github.com/pglass/how-do-i-locust


## Run locust

Run:
```
locust -f tests/storm/locustfile.py
```

And select the rook server to test in the web interface:
http://0.0.0.0:8089

## Example

Remove log and sqlite db:
```
make clean
```

Start emu:
```
emu start --parallelprocesses 4 --maxprocesses 30
```

Check logs:
```
tail -f pywps.log
```

Check database:
- use https://sqlitebrowser.org/
- open `pywps-logs.sqlite`

Launch locust:
```
locust -f tests/storm/locustfile.py
```

Open: http://0.0.0.0:8089

Start with 2 Users.
