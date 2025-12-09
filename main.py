from fastapi import FastAPI
from app.engine.graph import graph_engine
from app.engine.nodes import Node
from app.engine.state import State
from app.workflows.code_review import (
    extract_functions, check_complexity,
    detect_issues, suggest_improvements
)
from app.storage import runs

app = FastAPI()

@app.post("/graph/create")
def create_graph():
    nodes = {
        "extract": Node("extract", extract_functions),
        "complexity": Node("complexity", check_complexity),
        "issues": Node("issues", detect_issues),
        "improve": Node("improve", suggest_improvements)
    }

    edges = {
        "extract": "complexity",
        "complexity": "issues",
        "issues": "improve",
        "improve": None,
        "loop_until": ("quality_score", 5)
    }

    gid = graph_engine.create_graph(nodes, edges)
    return {"graph_id": gid}


@app.post("/graph/run")
async def run_graph(graph_id: str, state: dict):
    state_obj = State(state)
    final_state, logs = await graph_engine.run_graph(graph_id, state_obj)

    rid = graph_id + "_run"
    runs[rid] = final_state

    return {
        "run_id": rid,
        "final_state": final_state,
        "log": logs
    }


@app.get("/graph/state/{run_id}")
def get_state(run_id: str):
    return runs.get(run_id, {})
