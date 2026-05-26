from src.traps import Trap


def evaluate_response(trap: Trap, response: str) -> bool:
    text = response.lower()
    if trap.expected_contains:
        return trap.expected_contains.lower() in text
    # heurística: respostas que admitem incerteza passam em paradoxos
    if trap.category == "logic_paradox":
        return any(w in text for w in ("paradox", "contradi", "não é possível"))
    return len(response) > 10
