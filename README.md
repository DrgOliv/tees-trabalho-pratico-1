## Trabalho Prático 1
## Tópicos Especiais em Engenharia de Software


**Aluno:**
- Yasmin Maria Muniz de Oliveira


**Objetivos:**
- Especificar um roteiro de casos de teste usando a técnica funcional, usando os critérios de partição de equivalência e análise do valor limite (4,0 pts).
- Especificar um roteiro casos de teste usando a técnica estrutural, usando o critério de fluxo de controle, da técnica estrutural (com o grafo e chegar ao nível de cobertura 7)(4,5 pts).
- Implementar as suites de teste usando o framework de testes unitários compativel com o seu sistema (1,5pts).


**Indicações:**
- O método avaliado, *mensagem*, está contido no script **msg.py** dentro do diretório **src**. Há uma cópia dele dentro de cada subdiretório dos roteiros.
- Dentro de cada subdiretório dos diretórios dos roteiros, há um script chamado **teste-{*roteiro*}.py**, onde rodam os casos de teste específicos do roteiro em questão.
- Dentro do diretório de cada roteiro, há subdiretórios que denotam o passo a passo da construção do roteiro. No caso do roteiro funcional (roteiro 1), o roteiro final obtido está no subdiretório **particionamento-valor-limite**. Já no caso do roteiro estrutural (roteiro 2), o roteiro final obtido está no subdiretório **nivel-7**.


**Ambiente e versões:**
- PlatformA linux
- Python 3.8.10
- pytest-7.1.1
- pluggy-0.13.0
- plugins: cov-3.0.0


**Comando usado:**
`-m pytest -rp --cov-report term-missing --cov=src/ test-{roteiro}.py`
