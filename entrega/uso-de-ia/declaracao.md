# Declaração de uso de IA

## Ferramenta e modelo

- **Ferramenta:** Claude Code (extensão para VS Code)
- **Modelo:** Claude Opus 5.5 (`claude-opus-5-5`)
- **Sessão:** exportação em `sessao.md`, nesta pasta

## O que eu fiz (sem IA)

Antes da sessão com IA, investiguei as falhas dos testes fornecidos e corrigi quatro defeitos, um commit para cada:

| Commit | Defeito |
|-|-|
| `c9d5cdd` | `convert_to_brl` dividia o valor pela taxa em vez de multiplicar |
| `1f4e89a` | `is_billable` usava `!= "CANCELLED"` e faturava `NO_SHOW` |
| `45f4f59` | `calculate_room_nights` subtraía o dia do mês (`.day`) e ignorava a virada de mês/ano |
| `6255748` | `top_hotels` era ordenado em ordem crescente de valor |

Depois troquei o `reverse=True` do último commit pela chave `(-total, hotel_id)`, para manter o desempate por `hotel_id` em ordem crescente. Também escrevi a primeira versão do `README-ENTREGA.md`.

Com isso, os 5 testes fornecidos e a amostra de validação do README passavam.

## O que a IA fez

1. **Análise:** leu o README, todo o código e os testes, rodou `pytest` e a amostra de validação. Os dois já passavam.
2. **Conferência independente:** escreveu um script avulso, fora do repositório, que calcula o relatório direto das regras do README, e comparou o resultado com a saída do CLI no `data/reservas_hoteis.csv`. Todos os campos divergiam: o CLI contava 200 reservas e o arquivo tem 300.
3. **Defeitos encontrados** que os testes fornecidos e a amostra não cobrem:
   - `CsvReservationRepository.read()` parava após 200 linhas (`if len(rows) == 200: break`), descartando reservas sem avisar.
   - `convert_to_brl` ainda calculava em `float`. Isso fazia 23 das 300 conversões divergirem do valor exato; por exemplo, USD 0.75 × 5.42 = 4.065 virava `4.0649999…` e arredondava para `4.06` em vez de `4.07`.
   - A IA também apontou que o `reverse=True` do commit `6255748` invertia o desempate e que a minha troca para `(-total, hotel_id)` estava correta.
4. **Testes e correções**, a meu pedido:
   - escreveu 6 testes adicionais, um por arquivo, seguindo o padrão dos testes fornecidos: `test_input_reading.py`, `test_currency_precision.py`, `test_top_hotels_tiebreak.py`, `test_nights_year_boundary.py`, `test_no_billable_reservations.py` e `test_full_dataset_report.py`. Confirmou que 3 deles falhavam antes da correção;
   - removeu o limite de 200 linhas no repositório de reservas;
   - trocou a conversão por `amount * rates[currency]`, inteiramente em `Decimal`.
5. **Validação:** `pytest -q` com 11 testes passando, o comando oficial gerando `output/report.json`, a conferência independente igual nos dois CSVs, `--top 0` saindo com código 2 e `ruff` sem apontamentos.
6. **Redação:** escreveu esta declaração.

## Responsabilidade

Revisei as alterações sugeridas pela IA antes de aceitá-las. Os commits, o `README-ENTREGA.md` e a publicação do repositório ficaram comigo.
