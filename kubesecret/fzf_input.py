import subprocess
from subprocess import Popen


def fzf_input(choices, header="", preview="", height="", position="", multiselect=False):
    choices_str = "\n".join(choices)
    command = Popen(["echo", choices_str], stdout=subprocess.PIPE)

    raw_fzf_cmd = ["fzf"]
    raw_fzf_cmd = raw_fzf_cmd + ["--height", height] if height != "" else raw_fzf_cmd
    raw_fzf_cmd = raw_fzf_cmd + ["--header", header] if header != "" else raw_fzf_cmd
    raw_fzf_cmd = raw_fzf_cmd + ["--preview", preview] if preview != "" else raw_fzf_cmd
    raw_fzf_cmd = raw_fzf_cmd + ["--preview-window", position] if position != "" else raw_fzf_cmd
    raw_fzf_cmd = raw_fzf_cmd + ["-m", "--bind", "ctrl-t:toggle-all"] if multiselect else raw_fzf_cmd
    fzf_cmd = Popen(raw_fzf_cmd, stdin=command.stdout, stdout=subprocess.PIPE)

    command.stdout.close()
    output = fzf_cmd.communicate()[0].strip().decode("utf-8")
    if multiselect:
        return str(output).split("\n")
    return str(output)
