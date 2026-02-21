#!/usr/bin/env python3
import argparse
import json


def route(task: str, agents: list[str]) -> list[dict[str, str]]:
    task_lower = task.lower()
    selected = []

    rules = [
        ("research", ["research", "compare", "analyze"]),
        ("code", ["code", "bug", "refactor", "implement"]),
        ("ops", ["deploy", "incident", "latency", "infra"]),
        ("comms", ["email", "write", "summary", "memo"]),
    ]

    for agent, keywords in rules:
        if any(k in task_lower for k in keywords) and agent in agents:
            selected.append({"agent": agent, "reason": "keyword_match"})

    if not selected and agents:
        selected.append({"agent": agents[0], "reason": "fallback"})

    return selected


def main() -> int:
    parser = argparse.ArgumentParser(description="Route task to best-fit agents")
    parser.add_argument("--task", required=True)
    parser.add_argument("--agents", required=True, help="Comma separated agent names")
    ns = parser.parse_args()

    agents = [a.strip() for a in ns.agents.split(",") if a.strip()]
    result = {"task": ns.task, "assignments": route(ns.task, agents)}
    print(json.dumps(result, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
