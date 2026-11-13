## OBJETIVO

Encontra-se no README.md na raiz do projeto.

## INVESTIGAÇÃO

Após analise estrutural do projeto e estudo de regra de negocio, foi indentificado bugs em 4 funções que reproduzia as 
falhas dos tests.


**`test_currency.py`**
```
E       AssertionError: assert '118.45' == '642.00'
E         
E         - 642.00
E         + 118.45
```
Espera-se multiplicação de amount por rate_to_brl. O bug que resultou na falha no test de integridade foi indentificado em 
`currency_converter.py`, na def convert_to_brl, onde o operador aritmetico era divisorio.

**`test_status_rules.py`**
```
E       AssertionError: assert '120.00' == '100.00'
E         
E         - 100.00
E         ?  ^
E         + 120.00
E         ?  ^
```

A def is_billable deveria verificar apenas status com igualdade (==) "CONFIRMED". Ao usar a diferença (!=) "CANCELLED",
o sistema valida "NO_SHOW" como faturável, o que vai contra a regra de negocio que diz: só `CONFIRMED` é faturável.

Correção: is_billable return igualdade (==) "CONFIRMED".


**`test_nights.py`**
```
E       assert -28 == 3

tests\test_nights.py:19: AssertionError
```

A def calculate_room_nights deveria considerar (checkout_date - checkin_date).days * rooms. Ao pegar checkout.day - checkin.day, 
a função pega a sutração de dias, não considerando a virada de mês ou ano. 

Correção: (checkout_date - checkin_date).days * rooms; days considera a os dias com base em datas, mesmo após virada de mês ou ano.

**`test_top_hotels.py`**
```
E       AssertionError: assert ['H04', 'H03', 'H02'] == ['H01', 'H02', 'H03']
E         
E         At index 0 diff: 'H04' != 'H01'
E         Use -v to get more diff

tests\test_top_hotels.py:18: AssertionError
```

A regra de negocio estabelece que `top\_hotels`: `total\_brl` deve ser decrescente. Apos análise, foi indentificado que a ordenação em **ranked_hotels = sorted(hotels.items(), key=lambda item: (item[1]["amount"], item[0]))** era ascendente.

Correção: A function sorted() pode receber o parâmetro reverse para obter o resultado em ordem decrescente, onde foi ocultado. Após correção: **ranked_hotels = sorted(hotels.items(), key=lambda item: (item[1]["amount"], item[0]), reverse=True)**.