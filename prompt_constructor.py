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

        {"3. **Contextualização Adicional**" if self.contexto_adicional else ""}
        {"   - Contexto fornecido: " + self.contexto_adicional if self.contexto_adicional else ""}

        4. **Validação com Fontes Confiáveis**
           - Consulte as seguintes fontes para fact-checking:
             {self._format_sources()}
           - Documente confirmações, discrepâncias e omissões

        5. **Avaliação Filosófica**
           - Aplique conceitos de verdade lógica (Russell)
           - Analise intencionalidade dos agentes (Davidson)

        6. **Relatório Final**
           - Sintetize resultados com:
             - Fatos verificados
             - Vieses detectados
             - Limitações metodológicas
        """
        
        return prompt_template

    def _format_sources(self):
        """Formata a lista de fontes para exibição no prompt"""
        return '\n             '.join([f"- {fonte}" for fonte in self.fontes_confiáveis])

    def __str__(self):
        return self.generate_prompt()


# Exemplo de uso
if __name__ == "__main__":
    # Construção com parâmetros obrigatórios
    prompt_base = PromptConstructor(
        link_noticia="https://exemplo.com/noticia-urgente"
    )
    
    # Construção com parâmetros opcionais
    prompt_completo = PromptConstructor(
        link_noticia="https://exemplo.com/noticia-geopolitica",
        contexto_adicional="Conflito histórico entre as nações desde 2001",
        fontes_confiáveis=["ONU", "BBC", "Reuters", "DW"]
    )
    
    print("=== Prompt Base ===")
    print(prompt_base)
    
    print("\n=== Prompt Completo ===")
    print(prompt_completo)
