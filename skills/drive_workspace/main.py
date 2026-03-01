from pathlib import Path
from typing import Optional

BASE_PATH = Path("/mnt/gdrive/projects")

def _project_path(project_name: str) -> Path:
    return BASE_PATH / project_name

def create_project(project_name: str) -> str:
    """
    Creates a structured project workspace.
    """
    project_dir = _project_path(project_name)

    folders = [
        project_dir / "website-content",
        project_dir / "email-content" / "campaigns",
        project_dir / "press-releases",
        project_dir / "misc-images",
    ]

    for folder in folders:
        folder.mkdir(parents=True, exist_ok=True)

    return f"Project '{project_name}' created with standard structure."


def create_campaign(project_name: str, campaign_name: str) -> str:
    """
    Creates a campaign folder under email-content/campaigns.
    """
    campaign_dir = (
        _project_path(project_name)
        / "email-content"
        / "campaigns"
        / campaign_name
    )

    campaign_dir.mkdir(parents=True, exist_ok=True)

    return f"Campaign '{campaign_name}' created for project '{project_name}'."


def write_file(project_name: str, relative_path: str, content: str) -> str:
    """
    Writes content to a file inside a project.
    """
    project_dir = _project_path(project_name)
    file_path = project_dir / relative_path

    file_path.parent.mkdir(parents=True, exist_ok=True)

    file_path.write_text(content)

    return f"File written to {file_path}"


def read_file(project_name: str, relative_path: str) -> str:
    """
    Reads content from a file inside a project.
    """
    file_path = _project_path(project_name) / relative_path

    if not file_path.exists():
        return f"File not found: {file_path}"

    return file_path.read_text()


def list_files(project_name: str, relative_path: Optional[str] = "") -> list:
    """
    Lists files inside a folder in a project.
    """
    folder_path = _project_path(project_name) / relative_path

    if not folder_path.exists():
        return []

    return [str(p.name) for p in folder_path.iterdir()]


def move_file(project_name: str, source: str, destination: str) -> str:
    """
    Moves a file inside a project.
    """
    src_path = _project_path(project_name) / source
    dest_path = _project_path(project_name) / destination

    if not src_path.exists():
        return f"Source file not found: {src_path}"

    dest_path.parent.mkdir(parents=True, exist_ok=True)
    src_path.rename(dest_path)

    return f"Moved file to {dest_path}"
