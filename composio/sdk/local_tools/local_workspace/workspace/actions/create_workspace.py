from pydantic import BaseModel, Field

from composio.sdk.local_tools.lib.action import Action
from composio.sdk.local_tools.local_workspace.commons.get_logger import get_logger
from composio.sdk.local_tools.local_workspace.commons.local_docker_workspace import LocalDockerArgumentsModel
from composio.sdk.local_tools.local_workspace.commons.local_docker_workspace import WorkspaceManagerFactory
from composio.sdk.local_tools.local_workspace.commons.history_processor import HistoryProcessor


logger = get_logger()


class CreateWorkspaceRequest(BaseModel):
    image_name: str = Field(..., description="the workspace is a docker container. To create a workspace"
                                             "image name needs to be given, so container can start from the image")


class CreateWorkspaceResponse(BaseModel):
    workspace_id: str = Field(..., description="workspace-id for the created workspace")


class CreateWorkspaceAction(Action):
    """
    creates a workspace, and returns workspace-id
    """
    _display_name = "Create workspace"
    _request_schema = CreateWorkspaceRequest
    _response_schema = CreateWorkspaceResponse
    _tags = ["workspace"]
    workspace_factory: WorkspaceManagerFactory = None
    history_processor: HistoryProcessor = None

    def execute(self, request_data: CreateWorkspaceRequest, authorisation_data: dict) -> CreateWorkspaceResponse:
        args: LocalDockerArgumentsModel = LocalDockerArgumentsModel(image_name=request_data.image_name)
        workspace_id = self.workspace_factory.get_workspace_manager(args)
        return CreateWorkspaceResponse(workspace_id=workspace_id)

    def set_workspace_and_history(self, workspace_factory: WorkspaceManagerFactory,
                                  history_processor: HistoryProcessor):
        self.workspace_factory = workspace_factory
        self.history_processor = history_processor


