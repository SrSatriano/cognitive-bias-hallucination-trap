# Cognitive Bias & Hallucination Trap Framework

Ambiente de testes adversariais para LLMs locais — paradoxos financeiros e dados envenenados.

## Stack

- Python, LangChain, vLLM

## Matriz de confusão

|  | Predito OK | Predito FAIL |
|--|------------|--------------|
| Real OK | TN | FP |
| Real FAIL | FN | TP |

Métricas: precisão de detecção de alucinação, taxa de falso positivo.

## Categorias de falha

- `math_hallucination` — conta errada
- `logic_paradox` — contradiz premissas
- `poisoned_context` — segue dado falso injetado
- `overconfidence` — certeza sem base

## Calibração

Após testes, ajustar `temperature`, `top_k`, `top_p` — ver [docs/CALIBRATION.md](docs/CALIBRATION.md)

```bash
python -m src.run_suite --model qwen2.5-7b --vllm-url http://localhost:8000
```
