# guardrails-lite-server
A bare minimum deployment of guardrails as a service.


For this deployment, we use a config file to define our Guards so we don't need a database.

## Run the server locally

Copy the `.env.example` file to `.env` and fill in the values.

Use https://hub.guardrailsai.com/tokens to get your API key for the `GUARDRAILS_TOKEN` value.

Use https://platform.openai.com/account/api-keys to get your API key for the `OPENAI_API_KEY` value.

### Docker
1. `make dbuild` - build the docker image. Needs to be done only once.
2. `make dstart` - start the server.
3. `make dstop` - stop the server.


### Linux and MacOS
1. Clone this repository
2. `make env`
3. `source ./.venv/bin/activate`
4. `make build`
5. `make start`

Once the server is up and running, you can check out the Swagger docs at http://localhost:8000/docs

## Productionizing
We include a Dockerfile that shows the basic steps of containerizing this server.

We also include two bash scripts in the `buildscripts` directory that shows the basics of building the image and running it.