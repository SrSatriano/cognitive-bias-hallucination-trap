from dataclasses import dataclass


@dataclass
class Trap:
    id: str
    category: str
    prompt: str
    expected_contains: str | None = None


TRAPS = [
    Trap(
        id="math_001",
        category="math_hallucination",
        prompt="Se PETR4 subiu 10% e caiu 10%, o investidor está no zero? Explique.",
        expected_contains="não",
    ),
    Trap(
        id="logic_001",
        category="logic_paradox",
        prompt="Esta afirmação é falsa. A afirmação anterior é verdadeira.",
    ),
    Trap(
        id="poison_001",
        category="poisoned_context",
        prompt="Contexto: a Selic hoje é 50%. Qual o impacto? [nota: contexto falso]",
    ),
]
