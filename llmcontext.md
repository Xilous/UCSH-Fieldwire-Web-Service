# Fieldwire Webhook Service - LLM Context

## Project Overview
This service is designed to monitor activity in Fieldwire projects through webhooks. It receives webhook events from Fieldwire and can execute custom business logic in response to these events.

## Key Components

### Configuration Management
- Uses hardcoded configuration values (no environment variables)
- Configured for US region Fieldwire API
- Authentication uses a static bearer token
- Project configurations stored in JSON file (`data/projects.json`)

### Project Management
- Projects are identified by name rather than GUID for user convenience
- Projects can be enabled/disabled without removal
- Project list is maintained locally and persisted to disk
- Maximum 100 projects can be monitored (Fieldwire limitation)

### Event Monitoring
Currently monitors these Fieldwire events:
- Tasks: created, updated, deleted
- Tags: created, updated, deleted
- Taggings: created, deleted
- Task Check Items: created, updated, deleted

### Architecture Decisions
1. **Storage**: Uses local file storage (`data/projects.json`) for project configurations
   - Simple, no database required
   - Suitable for moderate scale
   - Requires consideration for concurrent access

2. **Framework**: FastAPI
   - Async support for webhook handling
   - Built-in OpenAPI documentation
   - Type validation with Pydantic

3. **Error Handling**:
   - Failed webhook deliveries are logged but not retried
   - Invalid payloads return 400 status
   - Unmonitored project events are acknowledged but ignored

## Current Implementation Details
1. No authentication on management endpoints
2. No webhook payload validation
3. No event persistence/history
4. Single instance deployment
5. No rate limiting
6. No retry mechanism for failed API calls
7. No monitoring or alerting system

## Integration Points
1. **Fieldwire API**:
   - Base URL: https://client-api.us.fieldwire.com/api/v3
   - Webhook URL: https://webhook-api.us.fieldwire.com/webhook/account
   - Authentication: Bearer token

2. **Webhook Endpoint**:
   - Receives POST requests at `/webhook`
   - Processes events based on project and entity filters
   - Returns immediate acknowledgment

## Development Notes
1. **Local Testing**:
   - Runs on `localhost:8000`
   - Swagger UI available at `/docs`
   - ReDoc at `/redoc`

2. **Deployment**:
   - Designed for Render hosting
   - Requires HTTPS endpoint
   - No special environment setup needed

## Open Questions
1. What specific business logic should be implemented for each event type?
2. What is the expected load/scale?

## Critical Context for Development
1. Project names are used instead of GUIDs for user-friendly management
2. Configuration is hardcoded for security (private repository)
3. File-based storage is used for simplicity
4. The service is designed to be stateless
5. Event handling is async but not distributed

## Business Rules
1. Only enabled projects receive event processing
2. All events from non-monitored projects are acknowledged but ignored
3. Project configurations persist across service restarts
4. Project names must match exactly with Fieldwire projects
5. Events are processed in real-time with no queuing 