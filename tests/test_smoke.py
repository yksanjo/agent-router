import importlib


def test_main_exists():
    mod = importlib.import_module("agent_router.cli")
    assert hasattr(mod, "main")
