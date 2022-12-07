import json
import os
import sys

from typing import Dict, Any


State = Dict[str, Any]


def cond(node):
    return node["size"] < 100_00


def run(cmdline: str, state: State):
    """
    Change the state based on the command and return the new state.
    """
    cmd_parts = cmdline.split(" ")
    # first component is $: ignore
    cmd = cmd_parts[1]

    # put current cmd in state
    state["cmd"] = cmd

    if cmd == "cd":
        arg = cmd_parts[2]
        # update the cwd
        state["cwd"] = os.path.normpath(os.path.join(state.get("cwd", "/"), arg))


def set_path(node, path, obj):
    """
    Updates the tree to add obj under path and update parent size.
    """
    if path[0] == "/":
        path = path[1:]  # drop leading /

    if "/" not in path:
        # found leaf
        node["tree"][path] = obj
        node["size"] += obj["size"]
        return

    head, tail = path.split("/", 1)
    subtree = node["tree"].get(head, {"size": 0, "tree": {}})
    set_path(subtree, tail, obj)
    node["tree"][head] = subtree
    node["size"] += obj["size"]


def parse_output(line: str, state: State):
    """
    Parse command output and update state.
    """
    cmd = state["cmd"]
    root = state.get("/", {"size": 0, "tree": {}})
    cwdpath = state["cwd"]
    stat, fname = line.split(" ", 1)

    value: Any = None
    if cmd == "ls":
        # parse ls output
        if stat == "dir":
            value = {"size": 0, "tree": {}}
        else:
            # file discovered: add size
            value = {"size": int(stat), "tree": None}

    else:
        raise ValueError(f"got output line {line} from command {cmd}, but command should not produce output")

    # update state
    newpath = os.path.join(cwdpath, fname)
    set_path(root, newpath, value)
    state["/"] = root


def find_nodes(node, cond):
    nodes = []

    for name in node.keys():
        subnode = node.get(name)
        if tree := subnode.get("tree"):  # only consider directories
            if cond(subnode):
                nodes.append((name, subnode["size"]))
            nodes.extend(find_nodes(tree, cond))

    return nodes


fname = sys.argv[1]

state: State = {}
with open(fname, encoding="utf-8") as infile:
    # the real input is one line long but let's iterate so we can run all the examples from a single file
    for line in infile:
        line = line.strip()
        if line[0] == "$":
            run(line, state)
        else:
            parse_output(line, state)

print(json.dumps(state, indent=2))


small_dirs = []
root = state["/"]
if cond(root):
    small_dirs.append(("/", root["size"]))

small_dirs = find_nodes(state["/"]["tree"], cond=lambda x: x["size"] < 100_000)
print(small_dirs)
print(sum(sd[1] for sd in small_dirs))
