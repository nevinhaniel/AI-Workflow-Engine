class Node:
    def __init__(self, name, fn):
        self.name = name
        self.fn = fn

    async def run(self, state):
        result = await self.fn(state)
        if result:
            state.data.update(result)
        return state
