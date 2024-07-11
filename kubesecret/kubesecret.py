import argparse
import base64
import json
import logging
from subprocess import check_output

from kubesecret import __version__

from .fzf_input import fzf_input

parser = argparse.ArgumentParser(prog="kubesecret", description="Interactively lookup in kubernetes secrets")
parser.add_argument("-n", "--namespace", help="Namespace to search in. Default is current namespace")
parser.add_argument("-s", "--size", help="Size of the fzf window. Default: 30%%", default="30%")
parser.add_argument(
    "-pp",
    "--preview-position",
    help="Preview window position. Default: up",
    default="up",
    choices=["up", "down", "left", "right"],
)
parser.add_argument("-ps", "--preview-size", help="Preview window size (in terminal lines). Default: 3", default=3)
parser.add_argument("-v", "--version", action="version", version=f"%(prog)s {__version__}")


class KubesecretSearcher:
    def __init__(self, options):
        self.namespace = options.namespace or self._current_namespace()
        self.size = options.size
        self.preview_position = options.preview_position
        self.preview_size = options.preview_size

    def _current_namespace(self):
        return (
            check_output("kubectl config view --minify -o jsonpath='{..namespace}'", shell=True).strip().decode("utf-8")
        )

    def secrets(self):
        return (
            check_output("kubectl get secrets | tail -n +2 | awk '{print $1}'", shell=True)
            .strip()
            .decode("utf-8")
            .splitlines()
        )

    def execute(self):
        selected_secret = fzf_input(self.secrets(), height=self.size, header=f"Searching secrets in {self.namespace}")
        if not selected_secret or selected_secret == "":
            logging.info("No secret selected")
            return

        secrets = (
            check_output(f"kubectl get secret -n {self.namespace} -o json {selected_secret}", shell=True)
            .strip()
            .decode("utf-8")
        )
        secrets = json.loads(secrets)
        key = fzf_input(
            secrets["data"].keys(),
            height=self.size,
            header=f"Searching in {selected_secret} of {self.namespace}",
            preview=f"echo '{json.dumps(secrets['data'])}' | jq  --raw-output '.{{}}' | base64 -d",
            position=f"{self.preview_position}:{self.preview_size}:wrap",
        )

        logging.info(f"Searched in {selected_secret} of {self.namespace}")
        try:
            result = base64.b64decode(secrets["data"][key]).decode("utf-8")
            print(json.dumps({key: result}, indent=2))
        except KeyError:
            print(secrets['data'][key]) if key in secrets['data'] else print("")


def execute():
    KubesecretSearcher(parser.parse_args()).execute()
