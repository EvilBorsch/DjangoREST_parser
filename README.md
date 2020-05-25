# Parser of the fedresurs site


DjangoREST + nginx + docker + gunicorn + PostgreSQL + requests

Docs in insomnia format (docs_insomnia) 

Logs in app/logs (nginx logs)

Env file is open so you can quickly build a project (on prod i will put it only on server ofc not in GitHub) 


```
To run:
make build-and-run

If already builded:
make run

If run first time(after you build project):
make first-time

Create SuperUser
make createsuperuser
```


