import uuid

class GraphEngine:
    def __init__(self):
        self.graphs = {}
        self.running = {}

    def create_graph(self, nodes, edges):
        gid = str(uuid.uuid4())
        self.graphs[gid] = {"nodes": nodes, "edges": edges}
        return gid

    async def run_graph(self, gid, state):
        graph = self.graphs[gid]
        nodes = graph["nodes"]
        edges = graph["edges"]

        log = []
        current = list(nodes.keys())[0]

        while current:
            log.append(current)
            node = nodes[current]
            await node.run(state)

            if "loop_until" in edges:
                cond_key, threshold = edges["loop_until"]
                if state.get(cond_key) < threshold:
                    current = list(nodes.keys())[0]
                    continue

            current = edges.get(current)

        return state.data, log


graph_engine = GraphEngine()
