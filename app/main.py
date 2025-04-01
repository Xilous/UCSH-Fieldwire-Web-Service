from fastapi import FastAPI
from .routes import webhook, projects

app = FastAPI(
    title="Fieldwire Webhook Service",
    description="Service for monitoring Fieldwire project activity via webhooks",
    version="1.0.0"
)

# Include routers
app.include_router(webhook.router)
app.include_router(projects.router)

@app.get("/")
async def root():
    """Root endpoint for health checks."""
    return {"status": "healthy"} 