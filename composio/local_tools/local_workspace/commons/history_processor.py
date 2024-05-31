import os
from collections import defaultdict
from functools import wraps
import json
from datetime import datetime
from pathlib import Path

from composio.local_tools.local_workspace.commons.get_logger import get_logger


logger = get_logger()
script_path = Path(__file__)
script_dir = script_path.parent
submit_logs_dir = script_dir / Path("../../../examples/swe/submit_logs/")


class HistoryProcessor:
    def __init__(self):
        self.history = defaultdict(list)
        # make submit_path directory
        try:
            date_time_folder = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            base_dir = script_dir / Path(date_time_folder)
            if not os.path.exists(base_dir):
                os.makedirs(base_dir)
            self.base_dir = base_dir
        except Exception as e:
            raise Exception("error in making submit-path directory") from e

    def log_command(self, workspace_id, command, output, state):
        entry = {"command": command, "output": output, "state": state}
        self.history[workspace_id].append(entry)

    def get_history(self, workspace_id, n=5):
        all_history = self.history.get(workspace_id, [])
        return all_history[-n:]

    def save_history_to_file(self, workspace_id: str, instance_id: str):
        # Define the file path using instance-id and ensure it's unique per workspace
        file_path = self.base_dir / Path(f"{workspace_id}_instance_{instance_id}.json")
        history_logs = self.history.get(workspace_id, [])
        with open(file_path, 'w') as file:
            json.dump(history_logs, file)


def history_recorder():
    def decorator(func):
        @wraps(func)
        def wrapper(self, *args, **kwargs):
            output, return_code = func(self, *args, **kwargs)
            is_submit_command = False
            if hasattr(self, "history_processor") and hasattr(self, "workspace_id"):
                command = ""
                if hasattr(self, "command"):
                    is_submit_command = "submit" in self.command
                    command = self.command + " " + args[0].json()
                else:
                    logger.error(
                        "command is not set in command-runner action class. History will have empty command for this"
                    )
                # Assume the state check and logging are meant to be done after the command execution
                # state = self.workspace_factory.get_workspace_state(workspace_id)
                state = None
                self.history_processor.log_command(
                    self.workspace_id, command, output, state
                )

                # save history to file-path once submit command is submitted
                if is_submit_command:
                    self.history_processor.save_history_to_file(self.workspace_id, self.instance_id)

            return output, return_code

        return wrapper

    return decorator
