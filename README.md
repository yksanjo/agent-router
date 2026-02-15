# Agent Router

Intelligent routing for agent requests.

## Features

- **Smart Routing** - Route requests to best agent
- **Rule-based Routing** - Define custom routing rules
- **Load Balancing** - Distribute load across agents
- **Fallback Routing** - Handle agent failures

## Quick Start

```python
from agent_router import AgentRouter

router = AgentRouter()
router.add_route("nlp", "agent-1")
agent = router.route("nlp")
```

## License

MIT
