#!/bin/bash

# Script de automação para setup do projeto Streamlit
# Autor: Automatização de setup
# Descrição: Cria ambiente virtual, instala dependências e executa o projeto

set -e  # Para o script se houver erro

echo "🚀 Iniciando setup automático do projeto Streamlit..."

# Cores para output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Função para imprimir mensagens coloridas
print_status() {
    echo -e "${BLUE}[INFO]${NC} $1"
}

print_success() {
    echo -e "${GREEN}[SUCCESS]${NC} $1"
}

print_warning() {
    echo -e "${YELLOW}[WARNING]${NC} $1"
}

print_error() {
    echo -e "${RED}[ERROR]${NC} $1"
}

# Verificar se Python está instalado
if ! command -v python3 &> /dev/null; then
    print_error "Python3 não encontrado. Por favor, instale Python 3.10 ou superior."
    exit 1
fi

# Verificar versão do Python
PYTHON_VERSION=$(python3 -c 'import sys; print(".".join(map(str, sys.version_info[:2])))')
print_status "Versão do Python detectada: $PYTHON_VERSION"

# Verificar se estamos no diretório correto
if [ ! -f "requirements.txt" ]; then
    print_error "Arquivo requirements.txt não encontrado. Execute este script no diretório streamlit/"
    exit 1
fi

# 1. Criar ambiente virtual se não existir
if [ ! -d ".venv" ]; then
    print_status "Criando ambiente virtual..."
    python3 -m venv .venv
    print_success "Ambiente virtual criado com sucesso!"
else
    print_warning "Ambiente virtual já existe. Reutilizando..."
fi

# 2. Ativar ambiente virtual
print_status "Ativando ambiente virtual..."
source .venv/bin/activate

# 3. Atualizar pip
print_status "Atualizando pip..."
pip install --upgrade pip

# 4. Instalar dependências
print_status "Instalando dependências do requirements.txt..."
pip install -r requirements.txt

print_success "Setup concluído com sucesso! 🎉"

# 5. Verificar se há arquivos .py para executar
PY_FILES=$(find . -name "*.py" -not -path "./.venv/*" | head -5)

if [ -z "$PY_FILES" ]; then
    print_warning "Nenhum arquivo Python encontrado para executar."
    print_status "Para criar um exemplo básico, execute:"
    echo "  python3 create_example.py"
    echo ""
    print_status "Para executar um arquivo específico:"
    echo "  source .venv/bin/activate"
    echo "  streamlit run seu_arquivo.py"
else
    print_status "Arquivos Python encontrados:"
    echo "$PY_FILES"
    echo ""

    # Perguntar se quer executar automaticamente
    read -p "Deseja executar o primeiro arquivo encontrado automaticamente? (y/n): " -n 1 -r
    echo
    if [[ $REPLY =~ ^[Yy]$ ]]; then
        FIRST_FILE=$(echo "$PY_FILES" | head -1)
        print_status "Executando: $FIRST_FILE"
        streamlit run "$FIRST_FILE"
    else
        print_status "Para executar manualmente:"
        echo "  source .venv/bin/activate"
        echo "  streamlit run nome_do_arquivo.py"
    fi
fi

print_success "Setup finalizado! Ambiente pronto para desenvolvimento. 🚀"