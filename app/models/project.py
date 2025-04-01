from pydantic import BaseModel
from typing import Optional

class Project(BaseModel):
    name: str
    id: str
    enabled: bool = True

class ProjectList(BaseModel):
    projects: list[Project] = []

    def get_enabled_project_ids(self) -> list[str]:
        return [project.id for project in self.projects if project.enabled] 