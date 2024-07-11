# Kubesecret

Kubesecret is a simple wrapper over fzf and kubectl to view configmaps effectively.

## Table of Contents


* [Installation](#installation)
* [Quickstart](#quickstart)
* [Usage](#usage)
* [Related repo:](#related-repo)


## Installation

* On macos
```bash
brew install handofgod94/tap/kubesecret
```

* Verify installation
```bash
kubesecret --version
```

## Quickstart

```bash
kubesecret # to launch the search window with default config
```

```bash
kubesecret -n <namespace> # to search of secrets in a specific namespace
```

That's it. It opens up search window with list of secrets in your current context and current namespace. 
You can search and view the secrets in a search window.

> [!WARNING]  
> Note: It only supports base64 encoded secrets for now.

## Usage
```
usage: kubesecret [-h] [-n NAMESPACE] [-s SIZE] [-pp {up,down,left,right}]
                [-ps PREVIEW_SIZE] [-v]

Interactively lookup in kubernetes secrets

optional arguments:
  -h, --help            show this help message and exit
  -n NAMESPACE, --namespace NAMESPACE
                        Namespace to search in. Default is current namespace
  -s SIZE, --size SIZE  Size of the fzf window. Default: 30%
  -pp {up,down,left,right}, --preview-position {up,down,left,right}
                        Preview window position. Default: up
  -ps PREVIEW_SIZE, --preview-size PREVIEW_SIZE
                        Preview window size (in terminal lines). Default: 3
  -v, --version         show program's version number and exit

```

## Related repo:
- [kubeconf](https://github.com/HandOfGod94/kubeconf): A similar tool to view kubernetes configmaps
