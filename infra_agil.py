import os
import subprocess
import re

def analyze_agile_infra_report(pdf_path, output_dir="./"):
    """
    Analisa um relatório de aula prática sobre infraestrutura ágil em formato PDF,
    extrai informações sobre aplicações e procedimentos, e gera um relatório completo em Markdown.

    Args:
        pdf_path (str): O caminho completo para o arquivo PDF do relatório.
        output_dir (str): O diretório onde o relatório de saída será salvo.

    Returns:
        str: O caminho para o relatório Markdown gerado.
    """
    if not os.path.exists(pdf_path):
        return f"Erro: O arquivo PDF não foi encontrado em {pdf_path}"

    # 1. Extrair texto do PDF
    txt_path = os.path.join(output_dir, "extracted_report.txt")
    try:
        subprocess.run(["pdftotext", pdf_path, txt_path], check=True)
    except subprocess.CalledProcessError as e:
        return f"Erro ao extrair texto do PDF: {e}"
    except FileNotFoundError:
        return "Erro: 'pdftotext' não encontrado. Certifique-se de que está instalado."

    with open(txt_path, "r", encoding="utf-8") as f:
        report_content = f.read()

    # 2. Analisar o conteúdo para extrair informações
    applications = {}

    # Extrair GIT
    git_match = re.search(r"GIT\.\s*Descrição do software:\s*(.*?)(?:\nEquipamento de Proteção Individual|PROCEDIMENTOS PRÁTICOS)", report_content, re.DOTALL)
    if git_match:
        git_desc = git_match.group(1).strip()
        git_install_link = "https://git-scm.com/downloads"
        applications["GIT"] = {
            "description": git_desc,
            "usage": "Controle de versão, monitoramento de pipeline de entrega.",
            "resources": [{"name": "Instalação", "link": git_install_link}]
        }

    # Extrair GitLab CI/CD
    gitlab_ci_match = re.search(r"GitLab CI/CD o pipeline é definido dentro de um arquivo denominado \.gitlab-ci\.yml,(.*?)(?:Vamos dar início a definição do pipeline para o projeto de uma Loja Virtual|Conforme a documentação oficial, jobs são:)", report_content, re.DOTALL)
    if gitlab_ci_match:
        gitlab_ci_desc = "Ferramenta de Integração Contínua e Entrega Contínua (CI/CD) integrada ao GitLab. Permite definir pipelines de entrega de software usando arquivos .gitlab-ci.yml."
        gitlab_ci_usage = "Definição de pipeline, orquestração de jobs, automação de CI/CD."
        gitlab_ci_account_link = "https://gitlab.com/users/"
        applications["GitLab CI/CD"] = {
            "description": gitlab_ci_desc,
            "usage": gitlab_ci_usage,
            "resources": [{"name": "Criação de Conta", "link": gitlab_ci_account_link}]
        }

    # Extrair Docker Hub
    docker_hub_match = re.search(r"Também iremos criar uma conta no hub\.docker: (https://hub\.docker\.com/) para o container\.", report_content)
    if docker_hub_match:
        docker_hub_link = docker_hub_match.group(1)
        docker_hub_desc = "Serviço de registro de imagens de contêineres para armazenar, compartilhar e gerenciar imagens Docker."
        docker_hub_usage = "Busca e registro de imagens Docker para construção da aplicação."
        applications["Docker Hub"] = {
            "description": docker_hub_desc,
            "usage": docker_hub_usage,
            "resources": [{"name": "Criação de Conta", "link": docker_hub_link}]
        }

    # 3. Gerar o relatório Markdown
    report_filename = os.path.join(output_dir, "relatorio_analise_infra_agil.md")
    with open(report_filename, "w", encoding="utf-8") as f:
        f.write("# Relatório de Análise de Infraestrutura Ágil Automatizado\n\n")
        f.write("**Gerado por:** Agente Automatizado Manus AI\n")
        f.write(f"**Data:** {os.fspath(os.path.getmtime(pdf_path))}\n\n") # Using file modification time as a proxy for report date
        f.write("Este relatório foi gerado automaticamente a partir da análise de um documento PDF sobre infraestrutura ágil.\n\n")

        f.write("## Aplicações e Ferramentas Identificadas\n\n")
        for app_name, data in applications.items():
            f.write(f"### {app_name}\n\n")
            f.write(f"*   **Descrição:** {data['description']}\n")
            f.write(f"*   **Uso na Atividade:** {data['usage']}\n")
            if data['resources']:
                f.write(f"*   **Recursos:**\n")
                for res in data['resources']:
                    f.write(f"    *   {res['name']}: [{res['link']}]({res['link']})\n")
            f.write("\n")

        f.write("## Procedimentos Chave\n\n")
        f.write("Com base na análise, os procedimentos chave incluem:\n")
        f.write("*   Instalação do sistema GIT.\n")
        f.write("*   Criação de contas no GitLab e Docker Hub.\n")
        f.write("*   Definição de pipelines de CI/CD usando arquivos `.gitlab-ci.yml`.\n")
        f.write("*   Utilização do Docker Hub para imagens de contêiner.\n")
        f.write("*   Simulação e monitoramento da execução de jobs em pipelines.\n")

        f.write("\n---\n")
        f.write("\n*Este relatório é uma sumarização automatizada e pode não conter todos os detalhes do documento original.*\n")

    os.remove(txt_path) # Limpar o arquivo de texto extraído
    return report_filename

if __name__ == "__main__":
    # Exemplo de uso (assumindo que o PDF está no mesmo diretório ou caminho especificado)
    # Para uso real, o caminho do PDF seria passado como argumento ou obtido de outra forma.
    # Este é um placeholder para demonstração.
    # pdf_file = "/home/ubuntu/upload/1709317510599.pdf"
    # output_report = analyze_agile_infra_report(pdf_file)
    # print(f"Relatório gerado em: {output_report}")
    pass

