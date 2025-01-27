class PromptConstructor:
    def __init__(self, link_noticia, contexto_adicional=None, fontes_confiáveis=None):
        """
        Construtor do prompt de análise de notícias
        
        Parâmetros obrigatórios:
        - link_noticia (str): URL da notícia a ser analisada
        
        Parâmetros opcionais:
        - contexto_adicional (str): Informações contextuais relevantes
        - fontes_confiáveis (list): Lista de fontes para validação
        """
        
        self.link_noticia = link_noticia
        self.contexto_adicional = contexto_adicional
        self.fontes_confiáveis = fontes_confiáveis or [
            "agências de notícias internacionais",
            "relatórios oficiais governamentais",
            "organismos multilaterais"
        ]
        
        self._validate_input()

    def _validate_input(self):
        """Validação dos inputs obrigatórios"""
        if not self.link_noticia:
            raise ValueError("Link da notícia é obrigatório")
            
        if not isinstance(self.link_noticia, str):
            raise TypeError("O link deve ser uma string")

    def generate_prompt(self):
        """Gera o prompt estruturado com base nos parâmetros fornecidos"""
        
        prompt_template = f"""
        Analise criticamente a notícia publicada em [{self.link_noticia}] utilizando os seguintes passos metodológicos:

        1. **Decomposição Atômica das Proposições**
           - Identifique afirmações centrais e decomponha em fatos atômicos (agente, ação, objeto)
           - Sinalize termos ambíguos ou dependentes de contexto externo

        2. **Estruturação Neo-Davidsoniana dos Eventos**
           - Defina para cada evento: participantes, instrumentos e modificadores
           - Analise a influência da estrutura narrativa na interpretação

        3. **Contextualização Ampla e Flexível**
           - Realize uma busca abrangente por contexto adicional relevante à notícia.
           - Utilize mecanismos de busca e bases de conhecimento para identificar informações complementares.
           - Adapte a busca a diferentes contextos (histórico, geográfico, político, etc.) para uma análise mais rica.

        4. **Validação com Fontes Confiáveis**
           - Consulte as seguintes fontes para fact-checking:
             {self._format_sources()}
           - Documente confirmações, discrepâncias e omissões
           - Avalie a confiabilidade das fontes e a relevância dos fatos encontrados
           - Busque por agências nacionais e internacionais de checagem de fatos

        5. **Avaliação Filosófica**
           - Aplique conceitos de verdade lógica (Russell)
           - Analise intencionalidade dos agentes (Davidson)

        6. **Relatório Final**
           - Sintetize resultados com:
             - Fatos verificados
             - Vieses detectados
             - Limitações metodológicas
             - Sugestões de melhorias
             - Referências bibliográficas
             - Conclusão crítica
        """
        
        return prompt_template

    def _format_sources(self):
        """Formata a lista de fontes para exibição no prompt"""
        return '\\n             '.join([f"- {fonte}" for fonte in self.fontes_confiáveis])

    def __str__(self):
        return self.generate_prompt()


# Solicitação de parâmetros via input do usuário
if __name__ == "__main__":
    link_noticia = input("Insira o link da notícia: ")
    contexto_adicional = input("Insira o contexto adicional (opcional): ")
    fontes_input = input("Insira fontes confiáveis separadas por vírgula (opcional): ")
    
    fontes_confiáveis = [fonte.strip() for fonte in fontes_input.split(',')] if fontes_input else None

    # Construção do prompt com parâmetros fornecidos pelo usuário
    if link_noticia:
        prompt_usuario = PromptConstructor(
            link_noticia=link_noticia,
            contexto_adicional=contexto_adicional or None,
            fontes_confiáveis=fontes_confiáveis
        )

        print("\\n=== Prompt Gerado ===\\n")
        print(prompt_usuario)
    else:
        print("Link da notícia é obrigatório para gerar o prompt.")
