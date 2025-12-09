import ast

async def extract_functions(state):
    code = state.get("code")
    tree = ast.parse(code)
    funcs = [n.name for n in tree.body if isinstance(n, ast.FunctionDef)]
    return {"functions": funcs, "quality_score": 1}

async def check_complexity(state):
    funcs = state.get("functions")
    return {"complexity": len(funcs)}

async def detect_issues(state):
    complexity = state.get("complexity")
    issues = max(0, 5 - complexity)
    return {"issues": issues}

async def suggest_improvements(state):
    issues = state.get("issues")
    score = state.get("quality_score") + (2 if issues == 0 else -1)
    return {"quality_score": score}
