# fastapi-transformers

[![Ruff Lint](https://github.com/youzarsiph/fastapi-transformers/actions/workflows/ruff.yml/badge.svg)](https://github.com/youzarsiph/fastapi-transformers/actions/workflows/ruff.yml)
[![Black Format](https://github.com/youzarsiph/fastapi-transformers/actions/workflows/black.yml/badge.svg)](https://github.com/youzarsiph/fastapi-transformers/actions/workflows/black.yml)
[![Django CI](https://github.com/youzarsiph/fastapi-transformers/actions/workflows/fastapi.yml/badge.svg)](https://github.com/youzarsiph/fastapi-transformers/actions/workflows/fastapi.yml)

FastAPI AI microservice using Phi 3 from HuggingFace Hub

## Get started

Clone the repo:

```console
git clone https://github.com/youzarsiph/fastapi-transformers
```

Install `poetry`, a Python tool for building and publishing packages:

```console
python -m pip install poetry
```

Install dependencies:

```console
python -m poetry install
```

Activate virtual environment

```console
python -m poetry env use python
```

Create a `.env` file that contains your HuggingFace access token, you may need to create an account on [HuggingFace](https://huggingface.co/):

```bash
# Your HF access token
HF_TOKEN=hf_**********************************

```

Or you can export `HF_TOKEN` env variable.

Run the server

```console
fastapi run fastapi_transformers/main.py
```

Now you are ready to go.
