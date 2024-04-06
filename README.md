# catapp


A cat monitoring app (mostly a docker tutorial)



# Database



## Run the database

Run only the postgres database using docker.

```bash
docker run --name postgresql -e POSTGRES_USER=guaiguai -e POSTGRES_PASSWORD=mdp -p 5432:5432 -v ./data:/var/lib/postgresql/data -d postgres 
```



Check the image.

```bash
docker images
```



Check the container.

```bash
docker ps
```



To get a shell inside the container.

```bash
docker exec -it postgresql bash
```



## Add data to the database

in the `scripts` directory are scripts to add data to the database. First set up the environment.

```bash
cd scripts/
python -m venv .venv
source .venv/bin/activate
poetry install --no-root
```



Then run the fill script.

```bash
python fill_db.py
```



Check that it worked.

```bash
python print_db.py
```



# Streamlit App



First set-up the environment.

```bash
 cd catmonitor/
 python -m venv .venv
 source .venv/bin/activate
 poetry install
 cd ..
```



## Run locally

With the `catmonitor/.venv` activated and from the root of the project.

```bash
streamlit run catmonitor/catmonitor/catdisplay.py
```



## Run as a docker container with a Dockerfile

From the root of the project.

```bash
docker build -t catmonitor_img -f catmonitor/Dockerfile . &&if docker ps -a|grep -q catmonitor; then docker rm -f catmonitor; fi &&docker run --name catmonitor -p 8501:8501 catmonitor_img
```



## Run as a docker container with docker-compose

See below.



# FastAPI App



First set-up the environment.

```bash
 cd catapi/
 python -m venv .venv
 source .venv/bin/activate
 poetry install
 cd ..
```



## Run locally

With the `catapi/.venv` activated and from the root of the project.

```bash
uvicorn api:app --app-dir=catapi/catapi/
```



## Run as a docker container with a Dockerfile

same.



## Run as a docker container with docker-compose

See below.



## Test that the API is working



In a terminal.

```bash
curl -X POST 127.0.0.1:8000/masse -H "Content-Type:application/json" --data '{"name": "Guaiguai"}'
```

```bash
curl 127.0.0.1:8000/ -H "Content-Type:application/json"
```



# Docker compose



From the root of the project.

```bash
docker compose up --build -d
```



To get the logs.

```bash
docker compose logs -f
```



For a specific service.

```bash
docker compose logs -f catapi
```



Then to clean up.

```bash
docker compose down
```

