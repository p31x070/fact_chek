# Fact Check Prompt Builder

This project provides a Python class `PromptConstructor` to generate structured prompts for fact-checking news articles. 

## Usage

To use the `PromptConstructor` class, you need to instantiate it with the URL of the news article you want to analyze. 

```python
from prompt_constructor import PromptConstructor

# Basic prompt
prompt_base = PromptConstructor(link_noticia="https://exemplo.com/noticia-urgente")
print(prompt_base)

# Advanced prompt with additional context and sources
prompt_completo = PromptConstructor(
    link_noticia="https://exemplo.com/noticia-geopolitica",
    contexto_adicional="Historical conflict between nations since 2001",
    fontes_confiáveis=["ONU", "BBC", "Reuters", "DW"]
)
print(prompt_completo)
```

This will output the generated prompts to the console.
