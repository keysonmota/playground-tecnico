# Experimentos com Streamlit

Esta pasta contém experimentos, exemplos e protótipos utilizando o [Streamlit](https://streamlit.io/), um framework open-source para criação rápida de aplicações web interativas em Python.

## Propósito

Reunir códigos, testes e ideias que utilizam o Streamlit, servindo como base para estudos, reuso e documentação de boas práticas.

##  Setup Automatizado (Recomendado)

### Opção 1: Script Bash (Linux/macOS)
```bash
# Torne o script executável
chmod +x setup.sh

# Execute o setup automático
./setup.sh
```

### Opção 2: Script Python (Multiplataforma)
```bash
# Setup básico
python3 auto_setup.py

# Setup e execução automática
python3 auto_setup.py --run
```

### Opção 3: Setup Manual (Tradicional)
1. **Crie e ative um ambiente virtual (venv):**

```bash
python3.10 -m venv .venv
source .venv/bin/activate
```

2. **Instale as dependências:**

```bash
pip install -r requirements.txt
```

3. **Execute o exemplo desejado:**

```bash
streamlit run nome_do_arquivo.py
```

> Substitua `nome_do_arquivo.py` pelo script que deseja executar.

##  Criando Exemplos

Para criar um exemplo básico automaticamente:

```bash
python3 create_example.py
```

Isso criará um arquivo `exemplo_basico.py` com widgets, gráficos e funcionalidades básicas do Streamlit.

## 📦 Dependências

### requirements.txt atual:
```txt
streamlit>=1.25.0
```

### Dependências adicionais recomendadas:
```txt
streamlit>=1.25.0
pandas>=1.5.0
numpy>=1.24.0
plotly>=5.15.0
matplotlib>=3.7.0
seaborn>=0.12.0
```

## ️ Scripts de Automação

- **`setup.sh`**: Script bash para setup completo (Linux/macOS)
- **`auto_setup.py`**: Script Python multiplataforma para setup
- **`create_example.py`**: Cria exemplo básico de aplicação Streamlit

## 📋 Comandos Úteis

```bash
# Ativar ambiente virtual
source .venv/bin/activate

# Desativar ambiente virtual
deactivate

# Instalar nova dependência
pip install nome_da_dependencia

# Salvar dependências
pip freeze > requirements.txt

# Executar aplicação
streamlit run app.py

# Executar em porta específica
streamlit run app.py --server.port 8502
```

##  Configurações Avançadas

### Configuração do Streamlit
Crie um arquivo `.streamlit/config.toml`:

```toml
[server]
port = 8501
headless = true

[theme]
primaryColor = "#FF6B6B"
backgroundColor = "#FFFFFF"
secondaryBackgroundColor = "#F0F2F6"
textColor = "#262730"
```

## 📚 Recursos Úteis

- [Documentação oficial do Streamlit](https://docs.streamlit.io/)
- [Streamlit Gallery](https://streamlit.io/gallery)
- [Streamlit Components](https://streamlit.io/components)
- [Streamlit Cloud](https://streamlit.io/cloud)

## Observações
- Sempre utilize ambientes virtuais para isolar as dependências.
- Prefira Python 3.8 ou superior.
- Os scripts de automação verificam automaticamente a versão do Python.
- Adicione neste README instruções específicas para cada novo experimento, se necessário.