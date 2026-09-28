# SpaceCorps OpenAPI Documentation

Markdown documentation twin for `openapi.json`.

## Specification
- **Title**: SpaceCorps Systems & Simulation API
- **Version**: 1.0.0
- **Base URL**: `https://spaceemit-api.sliplane.app`
- **Specification Source**: [openapi.json](https://spacecorps.github.io/openapi.json)

## Primary Endpoints
- `GET /health`: Health probe and cluster readiness.
- `GET /api/v1/telemetry`: Real-time Newtonian physics and active player counts.
- `GET /api/v1/sessions`: List active multiplayer player sessions.
- `POST /api/v1/actions`: Dispatch simulation action or task.
- `POST /api/v1/batch`: Bulk operation pipeline.
- `POST /api/v1/jobs`: Asynchronous simulation task submission.
- `GET /api/v1/jobs/{job_id}`: Poll asynchronous simulation job status.

## Rate Limiting & Errors
All responses include RFC standard headers:
- `RateLimit-Limit`
- `RateLimit-Remaining`
- `RateLimit-Reset`
- `Retry-After` (on 429)

Error payloads conform to RFC 9457 `application/problem+json`.
