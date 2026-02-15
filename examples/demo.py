#!/usr/bin/env python3
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from src import AgentRouter, RoutingStrategy
def main():
    print("Agent Router Demo")
    r = AgentRouter()
    r.add_route("nlp", "a1", RoutingStrategy.ROUND_ROBIN)
    r.add_route("nlp", "a2", RoutingStrategy.ROUND_ROBIN)
    a = r.route("nlp")
    print(f"Routed to: {a}")
    print("Done!")
if __name__ == "__main__": main()
