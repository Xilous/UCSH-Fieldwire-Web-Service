from fastapi import APIRouter, HTTPException
from typing import List
from ..models.project import Project
from ..services.project_manager import ProjectManager
from ..services.fieldwire import FieldwireClient

router = APIRouter()
project_manager = ProjectManager()
fieldwire_client = FieldwireClient()

@router.get("/projects", response_model=List[Project])
async def get_projects():
    """Get all monitored projects."""
    return project_manager.get_projects()

@router.post("/projects/{project_name}")
async def add_project(project_name: str):
    """Add a project to monitor by name."""
    # Get project details from Fieldwire
    project_data = await fieldwire_client.get_project_by_name(project_name)
    if not project_data:
        raise HTTPException(status_code=404, detail="Project not found in Fieldwire")
    
    # Add project to our monitoring list
    project = project_manager.add_project(
        name=project_data["name"],
        project_id=project_data["id"]
    )
    return project

@router.delete("/projects/{project_id}")
async def remove_project(project_id: str):
    """Remove a project from monitoring."""
    if project_manager.remove_project(project_id):
        return {"status": "success", "message": "Project removed"}
    raise HTTPException(status_code=404, detail="Project not found")

@router.patch("/projects/{project_id}")
async def update_project(project_id: str, enabled: bool):
    """Update a project's enabled status."""
    project = project_manager.update_project(project_id, enabled)
    if project:
        return project
    raise HTTPException(status_code=404, detail="Project not found") 