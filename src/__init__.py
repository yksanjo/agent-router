"""Agent Router - Intelligent routing for agent requests."""

from typing import Dict, List, Any, Optional, Callable
from dataclasses import dataclass, field
from enum import Enum
from datetime import datetime
import random


class AgentType(Enum):
    NVIDIA_GPU = "nvidia"
    AWS_TRAINIUM = "trainium"
    GOOGLE_TPU = "tpu"
    CPU = "cpu"


class Protocol(Enum):
    MCP = "mcp"
    A2A = "a2a"
    CUSTOM = "custom"
    HTTP = "http"


class RoutingStrategy(Enum):
    ROUND_ROBIN = "round_robin"
    LEAST_LOADED = "least_loaded"
    RANDOM = "random"
    WEIGHTED = "weighted"


@dataclass
class Route:
    service: str
    agents: List[str]
    strategy: RoutingStrategy = RoutingStrategy.ROUND_ROBIN
    weights: Dict[str, int] = field(default_factory=dict)
    fallback: Optional[str] = None


class AgentRouter:
    def __init__(self):
        self.routes: Dict[str, Route] = {}
        self.agent_loads: Dict[str, int] = {}
        self.round_robin_index: Dict[str, int] = {}
    
    def add_route(self, service: str, agent: str, strategy: RoutingStrategy = RoutingStrategy.ROUND_ROBIN) -> None:
        if service not in self.routes:
            self.routes[service] = Route(service=service, agents=[], strategy=strategy)
            self.round_robin_index[service] = 0
        if agent not in self.routes[service].agents:
            self.routes[service].agents.append(agent)
            self.agent_loads[agent] = 0
    
    def route(self, service: str) -> Optional[str]:
        route = self.routes.get(service)
        if not route or not route.agents:
            return route.fallback if route else None
        
        if route.strategy == RoutingStrategy.ROUND_ROBIN:
            idx = self.round_robin_index.get(service, 0)
            agent = route.agents[idx % len(route.agents)]
            self.round_robin_index[service] = (idx + 1) % len(route.agents)
            return agent
        elif route.strategy == RoutingStrategy.LEAST_LOADED:
            available = [a for a in route.agents if a in self.agent_loads]
            return min(available, key=lambda a: self.agent_loads[a]) if available else route.agents[0]
        return random.choice(route.agents)
    
    def get_stats(self) -> Dict[str, Any]:
        return {"routes": len(self.routes), "agents": len(self.agent_loads)}

__all__ = ["AgentRouter", "Route", "RoutingStrategy", "AgentType", "Protocol"]
