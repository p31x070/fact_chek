# Fact Check Prompt Builder

This project provides a Python class `PromptConstructor` to generate structured prompts for fact-checking news articles.

## Usage

To use the `PromptConstructor` class, you need to have Python installed.

1.  Create an instance of `PromptConstructor` with the news link and optional parameters:

    ```python
    from fact_check_prompt_builder.prompt_constructor import PromptConstructor

    prompt_base = PromptConstructor(
        link_noticia="https://exemplo.com/noticia-urgente"
    )

    prompt_completo = PromptConstructor(
        link_noticia="https://exemplo.com/noticia-geopolitica",
        contexto_adicional="Conflito histórico entre as nações desde 2001",
        fontes_confiáveis=["ONU", "BBC", "Reuters", "DW"]
    )
    ```

2.  Generate the prompt using the `generate_prompt()` method or by printing the object directly:

    ```python
    print(prompt_base.generate_prompt())
    print(prompt_completo)
    ```

## Files

*   `prompt_constructor.py`: Contains the `PromptConstructor` class definition.
*   `README.md`: This file, providing project information.
*   `.gitignore`: Specifies intentionally untracked files that Git should ignore.

## Git Repository

The project is intended to be pushed to a Git repository. Git is initialized in the project.

## Virtual Environment

A Python virtual environment is recommended for development.
