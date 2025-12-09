
# AI Workflow Engine (FastAPI)

## How to Run
1. Install dependencies:


2. Run the server:


3. API Endpoints
- POST `/graph/create`
- POST `/graph/run`
- GET `/graph/state/{run_id}`

## What the Engine Supports
- Node-based workflow execution
- Shared mutable state
- Branching
- Looping until condition
- Execution logs
- Extensible tool registry

## Improvements If More Time
- Persist runs in SQLite
- WebSocket streaming logs
- Proper DAG validation
- Async background workers
