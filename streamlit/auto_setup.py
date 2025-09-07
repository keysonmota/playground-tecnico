#!/usr/bin/env python3
"""
Script Python para automação completa do setup do projeto Streamlit
"""

import os
import sys
import subprocess
import platform
from pathlib import Path

class StreamlitSetup:
    def __init__(self):
        self.project_dir = Path.cwd()
        self.venv_dir = self.project_dir / ".venv"
        self.requirements_file = self.project_dir / "requirements.txt"

    def print_status(self, message, status="INFO"):
        """Imprime mensagens com cores"""
        colors = {
            "INFO": "\033[0;34m",
            "SUCCESS": "\033[0;32m",
            "WARNING": "\033[1;33m",
            "ERROR": "\033[0;31m"
        }
        reset = "\033[0m"
        print(f"{colors.get(status, '')}[{status}]{reset} {message}")

    def check_python(self):
        """Verifica se Python está instalado e na versão correta"""
        try:
            result = subprocess.run([sys.executable, "--version"],
                                  capture_output=True, text=True)
            version = result.stdout.strip()
            self.print_status(f"Python detectado: {version}")

            # Verificar versão mínima
            version_parts = version.split()[1].split('.')
            major, minor = int(version_parts[0]), int(version_parts[1])

            if major < 3 or (major == 3 and minor < 8):
                self.print_status("Python 3.8+ é recomendado", "WARNING")

            return True
        except Exception as e:
            self.print_status(f"Erro ao verificar Python: {e}", "ERROR")
            return False

    def create_venv(self):
        """Cria ambiente virtual se não existir"""
        if self.venv_dir.exists():
            self.print_status("Ambiente virtual já existe. Reutilizando...", "WARNING")
            return True

        try:
            self.print_status("Criando ambiente virtual...")
            subprocess.run([sys.executable, "-m", "venv", str(self.venv_dir)],
                         check=True)
            self.print_status("Ambiente virtual criado com sucesso!", "SUCCESS")
            return True
        except subprocess.CalledProcessError as e:
            self.print_status(f"Erro ao criar ambiente virtual: {e}", "ERROR")
            return False

    def get_venv_python(self):
        """Retorna o caminho do Python do ambiente virtual"""
        if platform.system() == "Windows":
            return self.venv_dir / "Scripts" / "python.exe"
        else:
            return self.venv_dir / "bin" / "python"

    def get_venv_pip(self):
        """Retorna o caminho do pip do ambiente virtual"""
        if platform.system() == "Windows":
            return self.venv_dir / "Scripts" / "pip.exe"
        else:
            return self.venv_dir / "bin" / "pip"

    def install_dependencies(self):
        """Instala dependências do requirements.txt"""
        if not self.requirements_file.exists():
            self.print_status("Arquivo requirements.txt não encontrado", "ERROR")
            return False

        try:
            venv_pip = self.get_venv_pip()

            # Atualizar pip
            self.print_status("Atualizando pip...")
            subprocess.run([str(venv_pip), "install", "--upgrade", "pip"],
                         check=True)

            # Instalar dependências
            self.print_status("Instalando dependências...")
            subprocess.run([str(venv_pip), "install", "-r", str(self.requirements_file)],
                         check=True)

            self.print_status("Dependências instaladas com sucesso!", "SUCCESS")
            return True

        except subprocess.CalledProcessError as e:
            self.print_status(f"Erro ao instalar dependências: {e}", "ERROR")
            return False

    def find_py_files(self):
        """Encontra arquivos Python no projeto"""
        py_files = []
        for file_path in self.project_dir.rglob("*.py"):
            if ".venv" not in str(file_path):
                py_files.append(file_path)
        return py_files

    def run_streamlit(self, file_path=None):
        """Executa aplicação Streamlit"""
        if not file_path:
            py_files = self.find_py_files()
            if not py_files:
                self.print_status("Nenhum arquivo Python encontrado", "WARNING")
                return False
            file_path = py_files[0]

        try:
            venv_python = self.get_venv_python()
            self.print_status(f"Executando: {file_path}")

            # Executar streamlit
            subprocess.run([str(venv_python), "-m", "streamlit", "run", str(file_path)],
                         check=True)
            return True

        except subprocess.CalledProcessError as e:
            self.print_status(f"Erro ao executar Streamlit: {e}", "ERROR")
            return False
        except KeyboardInterrupt:
            self.print_status("Execução interrompida pelo usuário", "WARNING")
            return True

    def setup(self, auto_run=False):
        """Executa setup completo"""
        self.print_status("🚀 Iniciando setup automático do projeto Streamlit...")

        # Verificações
        if not self.check_python():
            return False

        if not self.requirements_file.exists():
            self.print_status("Arquivo requirements.txt não encontrado", "ERROR")
            return False

        # Setup
        if not self.create_venv():
            return False

        if not self.install_dependencies():
            return False

        self.print_status("Setup concluído com sucesso! 🎉", "SUCCESS")

        # Executar automaticamente se solicitado
        if auto_run:
            py_files = self.find_py_files()
            if py_files:
                self.print_status("Executando aplicação automaticamente...")
                return self.run_streamlit()
            else:
                self.print_status("Nenhum arquivo Python encontrado para executar", "WARNING")

        return True

def main():
    setup = StreamlitSetup()

    # Verificar argumentos
    auto_run = "--run" in sys.argv or "-r" in sys.argv

    if setup.setup(auto_run=auto_run):
        if not auto_run:
            py_files = setup.find_py_files()
            if py_files:
                print(f"\n📋 Para executar manualmente:")
                print(f"   source .venv/bin/activate")
                print(f"   streamlit run {py_files[0].name}")
            else:
                print(f"\n📋 Para criar um exemplo:")
                print(f"   python3 create_example.py")
    else:
        sys.exit(1)

if __name__ == "__main__":
    main()