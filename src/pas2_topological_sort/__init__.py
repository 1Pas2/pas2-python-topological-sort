from collections import deque


def sort_dependencies(graph):
    nodes = dict.fromkeys(graph)
    dependencies = {node: list(dict.fromkeys(items)) for node, items in graph.items()}
    for items in dependencies.values():
        for node in items:
            nodes.setdefault(node, None)
    counts = {node: len(dependencies.get(node, [])) for node in nodes}
    dependents = {node: [] for node in nodes}
    for node, items in dependencies.items():
        for dependency in items:
            dependents[dependency].append(node)
    ready = deque(node for node in nodes if counts[node] == 0)
    result = []
    while ready:
        node = ready.popleft()
        result.append(node)
        for child in dependents[node]:
            counts[child] -= 1
            if counts[child] == 0:
                ready.append(child)
    if len(result) != len(nodes):
        raise ValueError("Dependency graph contains a cycle")
    return result
