# Análise Automatizada de Relatórios de Infraestrutura Ágil

Este repositório contém os resultados da análise de um "Relatório de Aula Prática - Infraestrutura Ágil" e um agente automatizado desenvolvido para replicar essa análise em outros documentos similares.

## Conteúdo do Repositório

*   `relatorio_completo_infraestrutura_agil.md`: Um relatório detalhado que sumariza as aplicações, ferramentas e procedimentos identificados no documento original. Este relatório foi gerado a partir da análise do PDF fornecido.
*   `agente_infra_agil.py`: Um script Python que atua como um agente automatizado. Ele é capaz de analisar um arquivo PDF de relatório de infraestrutura ágil, extrair informações chave sobre ferramentas e procedimentos, e gerar um novo relatório em formato Markdown.

## Como Usar o Agente (`agente_infra_agil.py`)

O agente Python foi projetado para automatizar a extração e sumarização de informações de relatórios de aula prática sobre infraestrutura ágil.

### Pré-requisitos

Para executar o agente, você precisará ter o `pdftotext` instalado em seu sistema. Este é um utilitário de linha de comando que faz parte do pacote `poppler-utils` (ou `xpdf` em alguns sistemas).

**Instalação no Ubuntu/Debian:**

```bash
sudo apt-get update
sudo apt-get install poppler-utils
```

**Instalação no macOS (via Homebrew):**

```bash
brew install poppler
```

### Execução

Para usar o agente, execute o script Python, passando o caminho para o arquivo PDF que deseja analisar como argumento. Você também pode especificar um diretório de saída opcional.

```bash
python3 agente_infra_agil.py <caminho_para_o_arquivo.pdf> [diretorio_de_saida]
```

**Exemplo:**

```bash
python3 agente_infra_agil.py /caminho/para/seu/relatorio.pdf ./output_reports/
```

Se nenhum diretório de saída for especificado, o relatório gerado será salvo no diretório atual.

### Saída

O agente irá gerar um arquivo Markdown (`relatorio_analise_infra_agil.md`) no diretório especificado (ou no diretório atual) contendo a análise das aplicações e procedimentos identificados no PDF.

## Relatório Completo Gerado

O `relatorio_completo_infraestrutura_agil.md` é um documento abrangente que detalha:

*   **Introdução:** Contexto e objetivos da análise.
*   **Análise do Relatório Original:** Resumo dos objetivos, infraestrutura, procedimentos e checklist da aula prática.
*   **Aplicações e Ferramentas:** Descrição detalhada do GIT, GitLab CI/CD e Docker Hub, incluindo suas funções na atividade e links para recursos.
*   **Processo de Integração Contínua:** Explicação passo a passo do fluxo de CI/CD conforme descrito no relatório original.
*   **Conclusão:** Sumarização dos aprendizados e da importância das ferramentas no contexto de DevOps.

## Tecnologias Utilizadas

*   **Python:** Para o desenvolvimento do agente automatizado.
*   **Git:** Sistema de controle de versões.
*   **GitLab CI/CD:** Plataforma de Integração Contínua e Entrega Contínua.
*   **Docker Hub:** Registro de imagens de contêineres.

## Autor

Este projeto e o agente automatizado foram desenvolvidos por **Manus AI**.

