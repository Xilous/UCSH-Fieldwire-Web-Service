import json
from pathlib import Path
from typing import List, Optional
from ..models.project import Project, ProjectList
from ..config import get_settings

class ProjectManager:
    def __init__(self):
        self.settings = get_settings()
        self.projects_file = self.settings.PROJECTS_FILE
        self._ensure_projects_file()
        self._load_projects()

    def _ensure_projects_file(self):
        """Ensure the projects file exists and create it if it doesn't."""
        self.projects_file.parent.mkdir(parents=True, exist_ok=True)
        if not self.projects_file.exists():
            self._save_projects(ProjectList())

    def _load_projects(self):
        """Load projects from the JSON file."""
        with open(self.projects_file, 'r') as f:
            data = json.load(f)
            self.projects = ProjectList(**data)

    def _save_projects(self, projects: ProjectList):
        """Save projects to the JSON file."""
        with open(self.projects_file, 'w') as f:
            json.dump(projects.dict(), f, indent=2)

    def get_projects(self) -> List[Project]:
        """Get all projects."""
        return self.projects.projects

    def add_project(self, name: str, project_id: str) -> Project:
        """Add a new project to the list."""
        project = Project(name=name, id=project_id)
        self.projects.projects.append(project)
        self._save_projects(self.projects)
        return project

    def remove_project(self, project_id: str) -> bool:
        """Remove a project from the list."""
        initial_length = len(self.projects.projects)
        self.projects.projects = [p for p in self.projects.projects if p.id != project_id]
        if len(self.projects.projects) < initial_length:
            self._save_projects(self.projects)
            return True
        return False

    def get_project(self, project_id: str) -> Optional[Project]:
        """Get a specific project by ID."""
        for project in self.projects.projects:
            if project.id == project_id:
                return project
        return None

    def update_project(self, project_id: str, enabled: bool = None) -> Optional[Project]:
        """Update a project's enabled status."""
        project = self.get_project(project_id)
        if project:
            if enabled is not None:
                project.enabled = enabled
            self._save_projects(self.projects)
        return project 