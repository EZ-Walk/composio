import logging

from composio_coders.constants import KEY_API_KEY
from composio_coders.context import Context, set_context
from composio_coders.swe import CoderAgent, CoderAgentArgs
from datasets import load_dataset
from rich.logging import RichHandler


# get logger
LOGGER_NAME = "local_workspace"

handler = RichHandler(show_time=False, show_path=False)
handler.setLevel(logging.DEBUG)
logger = logging.getLogger(LOGGER_NAME)
logger.setLevel(logging.DEBUG)
logger.addHandler(handler)
logger.propagate = False


# princeton swe bench lite dataset has these fields
# instance_id: (str) - A formatted instance identifier, usually as repo_owner__repo_name-PR-number.
# patch: (str) - The gold patch, the patch generated by the PR (minus test-related code), that resolved the issue.
# repo: (str) - The repository owner/name identifier from GitHub.
# base_commit: (str) - The commit hash of the repository representing the HEAD of the repository before the solution PR is applied.
# hints_text: (str) - Comments made on the issue prior to the creation of the solution PR’s first commit creation date.
# created_at: (str) - The creation date of the pull request.
# test_patch: (str) - A test-file patch that was contributed by the solution PR.
# problem_statement: (str) - The issue title and body.
# version: (str) - Installation version to use for running evaluation.
# environment_setup_commit: (str) - commit hash to use for environment setup and installation.
# FAIL_TO_PASS: (str) - A json list of strings that represent the set of tests resolved by the PR and tied to the issue resolution.
# PASS_TO_PASS: (str) - A json list of strings that represent tests that should pass before and after the PR application.


def filter_from_repo_name(curr_dataset, repo_name):
    filtered_dataset = curr_dataset.filter(
        lambda x: x["repo"] == repo_name.strip().lower()
    )
    return filtered_dataset


def get_issues_dataset():
    test_dataset = load_dataset("princeton-nlp/SWE-bench_Lite", split="test[23:33]")
    return test_dataset


def build_issue_description(hints, problem_statement):
    if not problem_statement or not problem_statement.strip():
        raise ValueError("problem statement is empty")
    tmpl = ""
    if hints:
        tmpl = f"Here are few hints to solve the issue described in problem_statement {hints}"

    tmpl += f"""\n\n
    Here is the issue, that you have to solve all on your own 
    {problem_statement}
    """
    return tmpl


def run():
    """
    Main function to load and display entries from the SWE-bench lite dataset.
    """

    issues = get_issues_dataset()
    for issue in issues:
        issue_description = build_issue_description(
            issue["hints_text"], issue["problem_statement"]
        )
        patch = issue["patch"]
        install_commit_id = issue["environment_setup_commit"]
        logger.info(
            "found patch-id: %s and install_commit_id: %s", patch, install_commit_id
        )
        issue_config = {
            "repo_name": issue["repo"],
            "issue_id": issue["instance_id"],
            "base_commit_id": issue["base_commit"],
            "issue_desc": issue_description,
        }
        logger.info(
            f"starting agent for issue-id: {issue['instance_id']}\n"
            f"issue-description: {issue_description}\n"
            f"repo_name: {issue['repo']}\n"
        )

        print("--------------------------------------------------")

        model_env_config = {

            KEY_API_KEY: "test-key",
            "azure_endpoint": "test-endpoint",
            "model_env": "azure",
        }
        ctx = Context()
        ctx.issue_config = issue_config
        ctx.model_env = model_env_config
        set_context(ctx)

        args = CoderAgentArgs(
            agent_logs_dir=ctx.agent_logs_dir,
            issue_config=ctx.issue_config,
            model_env_config=ctx.model_env,
        )
        coder = CoderAgent(args)
        coder.run()


if __name__ == "__main__":
    run()
