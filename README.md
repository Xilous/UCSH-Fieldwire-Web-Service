# Fieldwire Webhook Service

A microservice for monitoring Fieldwire project activity via webhooks and responding with custom business logic.

## Features

- Receive webhooks from Fieldwire
- Monitor specific projects
- Handle various event types (tasks, tags, task check items)
- Project management API
- Configurable business rules

## Setup

1. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Create a `.env` file with the following variables:
```
FIELDWIRE_ACCOUNT_ID=your_account_id
FIELDWIRE_ACCESS_TOKEN=your_access_token
```

4. Run the service:
```bash
uvicorn app.main:app --reload
```

## API Endpoints

### Webhook
- `POST /webhook` - Receive webhooks from Fieldwire

### Projects
- `GET /projects` - Get all monitored projects
- `POST /projects/{project_name}` - Add a project to monitor
- `DELETE /projects/{project_id}` - Remove a project from monitoring
- `PATCH /projects/{project_id}` - Update project status

## Development

The project structure is organized as follows:
```
webhooks-service/
├── app/
│   ├── main.py              # FastAPI application
│   ├── config.py            # Configuration management
│   ├── models/              # Data models
│   ├── services/            # Business logic
│   └── routes/              # API routes
├── data/                    # Data storage
├── requirements.txt
└── README.md
```

## Deployment

The service is designed to be deployed on Render. Make sure to:
1. Set up environment variables in Render
2. Configure the webhook URL in Fieldwire
3. Enable HTTPS for security

## Business Logic

The webhook handler in `app/services/webhook.py` contains placeholder methods for handling different event types. Implement your business logic in these methods:

- `_handle_task_created`
- `_handle_task_updated`
- `_handle_task_deleted`
- `_handle_tag_created`
- `_handle_tag_updated`
- `_handle_tag_deleted`
- `_handle_tagging_created`
- `_handle_tagging_deleted`
- `_handle_task_check_item_created`
- `_handle_task_check_item_updated`
- `_handle_task_check_item_deleted` 