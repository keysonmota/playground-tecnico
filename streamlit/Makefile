.PHONY: help setup run clean install example

# Variáveis
VENV = .venv
PYTHON = $(VENV)/bin/python
PIP = $(VENV)/bin/pip
STREAMLIT = $(VENV)/bin/streamlit

help: ## Mostra esta ajuda
	@echo "Comandos disponíveis:"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

setup: ## Configura o ambiente virtual e instala dependências
	@echo "🚀 Configurando ambiente..."
	python3 -m venv $(VENV)
	$(PIP) install --upgrade pip
	$(PIP) install -r requirements.txt
	@echo "✅ Setup concluído!"

install: ## Instala dependências no ambiente virtual
	$(PIP) install -r requirements.txt

run: ## Executa a aplicação Streamlit
	$(STREAMLIT) run exemplo_basico.py

run-auto: ## Executa setup e aplicação automaticamente
	@$(MAKE) setup
	@$(MAKE) example
	@$(MAKE) run

example: ## Cria exemplo básico
	python3 create_example.py

clean: ## Remove ambiente virtual
	rm -rf $(VENV)
	@echo "🧹 Ambiente virtual removido"

activate: ## Mostra comando para ativar ambiente virtual
	@echo "Para ativar o ambiente virtual, execute:"
	@echo "source $(VENV)/bin/activate"

check: ## Verifica se o ambiente está configurado
	@if [ -d "$(VENV)" ]; then \
		echo "✅ Ambiente virtual existe"; \
		$(PYTHON) --version; \
	else \
		echo "❌ Ambiente virtual não encontrado. Execute 'make setup'"; \
	fi