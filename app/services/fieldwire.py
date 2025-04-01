import aiohttp
from typing import Dict, Any, List
from ..config import get_settings

class FieldwireClient:
    def __init__(self):
        self.settings = get_settings()
        self.headers = {
            "Authorization": f"Bearer {self.settings.FIELDWIRE_ACCESS_TOKEN}",
            "Content-Type": "application/json"
        }

    async def create_webhook_subscription(self, post_url: str, project_ids: List[str]) -> Dict[str, Any]:
        """Create a new webhook subscription."""
        url = f"{self.settings.FIELDWIRE_WEBHOOK_BASE_URL}/{self.settings.FIELDWIRE_ACCOUNT_ID}/subscriptions"
        
        payload = {
            "subscription_name": "Fieldwire Activity Monitor",
            "description": "Monitors specific projects for activity",
            "post_url": post_url,
            "subscription_status": "enabled",
            "entity_filters": [
                "tag.created",
                "tag.updated",
                "tag.deleted",
                "tagging.created",
                "tagging.deleted",
                "task.created",
                "task.updated",
                "task.deleted",
                "task_check_item.created",
                "task_check_item.updated",
                "task_check_item.deleted"
            ],
            "project_filters": project_ids
        }

        async with aiohttp.ClientSession() as session:
            async with session.post(url, headers=self.headers, json=payload) as response:
                return await response.json()

    async def get_project_by_name(self, project_name: str) -> Dict[str, Any]:
        """Get project details by name."""
        url = f"{self.settings.FIELDWIRE_API_BASE_URL}/projects"
        
        async with aiohttp.ClientSession() as session:
            async with session.get(url, headers=self.headers) as response:
                projects = await response.json()
                for project in projects:
                    if project["name"] == project_name:
                        return project
                return None

    async def make_api_request(self, method: str, endpoint: str, data: Dict[str, Any] = None) -> Dict[str, Any]:
        """Make a generic API request to Fieldwire."""
        url = f"{self.settings.FIELDWIRE_API_BASE_URL}/{endpoint}"
        
        async with aiohttp.ClientSession() as session:
            async with session.request(method, url, headers=self.headers, json=data) as response:
                return await response.json() 