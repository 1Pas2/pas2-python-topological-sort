import pas2_topological_sort as api

print(api.sort_dependencies({"app": ["database"], "database": ["network"]}))
