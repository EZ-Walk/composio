from composio.sdk.local_tools.lib.tool import Tool
from composio.sdk.local_tools.local_workspace.workspace.actions.workspace_setup import SetupWorkspace
from composio.sdk.local_tools.local_workspace.workspace.actions.workspace_status import WorkspaceStatus
from composio.sdk.local_tools.local_workspace.workspace.actions.setup_github_repo import SetupGithubRepo
from composio.sdk.local_tools.local_workspace.commons.local_docker_workspace import WorkspaceManagerFactory
from composio.sdk.local_tools.local_workspace.workspace.actions.create_workspace import CreateWorkspaceAction


class LocalWorkspace(Tool):
    """
    local workspace tool for creating local workspace
    """
    workspace_factory: WorkspaceManagerFactory = None

    def actions(self) -> list:
        return [WorkspaceStatus,
                SetupWorkspace,
                SetupGithubRepo,
                CreateWorkspaceAction]

    def triggers(self) -> list:
        return []

    def set_workspace_factory(self, workspace_factory: WorkspaceManagerFactory):
        self.workspace_factory = workspace_factory

    def get_workspace_factory(self) -> WorkspaceManagerFactory:
        return self.workspace_factory
