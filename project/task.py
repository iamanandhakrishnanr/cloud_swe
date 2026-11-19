from pydantic import BaseModel, Field
from pathlib import Path

class TaskDefinition(BaseModel):
    task_id: str = Field(..., description="Unique identifier for the bugfix task")
    repo_path: Path = Field(..., description="Path to the repository workspace")
    test_cmd: list[str] = Field(..., description="Command to run visible tests")
    hidden_test_cmd: list[str] = Field(..., description="Command to run hidden evaluation tests")
    protected_globs: list[str] = Field(default_factory=list, description="Files/globs that the agent cannot modify")
    baseline_failure: str = Field(..., description="Expected baseline failure pattern or error message")
    max_iterations: int = Field(default=3, description="Max agent repair attempts")