from fastapi import FastAPI
from agent import Agent48
app = FastAPI(title="Compliance-Audit-Trail")
agent = Agent48()

@app.post("/execute")
async def execute(payload: dict):
    return agent.execute(payload)
