# VectorSnap

A scalable vector similarity search API built with FastAPI.

## Features

- Document ingestion with chunking
- Vector embedding generation
- Similarity search
- PostgreSQL for metadata
- Redis for rate limiting
- Support for Chroma and Pinecone vector stores

## Setup

1. Install dependencies:
```bash
poetry install
```

2. Copy environment file:
```bash
cp .env.example .env
```

3. Start services with Docker:
```bash
cd docker
docker-compose up -d
```

4. Run migrations:
```bash
alembic upgrade head
```

5. Start the API:
```bash
uvicorn app.main:app --reload
```

## API Endpoints

- `POST /ingest` - Ingest documents
- `POST /search` - Search similar vectors
- `GET /health` - Health check

## Testing

```bash
pytest tests/
```

## License

MIT
