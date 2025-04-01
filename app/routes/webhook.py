from fastapi import APIRouter, Request, HTTPException
from typing import Dict, Any
from ..services.webhook import WebhookHandler

router = APIRouter()
webhook_handler = WebhookHandler()

@router.post("/webhook")
async def handle_webhook(request: Request) -> Dict[str, Any]:
    """Handle incoming webhook from Fieldwire."""
    try:
        payload = await request.json()
        return await webhook_handler.handle_webhook(payload)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e)) 