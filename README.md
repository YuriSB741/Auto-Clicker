<<<<<<< HEAD
# YB Auto Clicker

Programa simples que fiz para automatizar cliques do mouse em um intervalo de tempo escolhido pelo usuário. Também dá pra configurar um atalho pra ligar/desligar sem precisar clicar na tela.

## O que ele faz

- Você escolhe o intervalo entre os cliques (horas, minutos, segundos, milissegundos)
- Dá pra começar e parar pela própria interface
- Dá pra configurar um atalho do teclado pra iniciar/parar
- Valida os campos pra não deixar passar valor errado
- Interface feita com CustomTkinter

## Requisitos

- Python 3.10+
- Só funciona no Windows por enquanto, porque uso a lib `keyboard` pra pegar os atalhos globais

## Como instalar

1. Baixe o repositório
2. Cria um ambiente virtual (recomendado):

```powershell
py -m venv venv
.\venv\Scripts\Activate.ps1
```

3. Instala as dependências:

```powershell
pip install -r requirements.txt
```

Obs: se o comando `py` não funcionar, verifica se o Python tá instalado e se foi adicionado ao PATH na hora de instalar.

## Como rodar

```powershell
py -m src.main
```

## Como usar

1. Abre o app
2. Vai em Options
3. Preenche o intervalo entre os cliques (o total tem que ser maior que zero)
4. Se quiser, clique no campo de atalho e pressione a tecla ou combinação desejada, como `F6` ou `Ctrl` + `Shift` + `A`.
5. Clica em Aplicar
6. Clica em Start (ou usa o atalho) pra começar
7. Clica em Stop (ou o mesmo atalho) pra parar

## Estrutura

```
src/
  autoclicker.py   -> lógica dos cliques e atalhos
  interface.py     -> a tela do programa
  main.py          -> onde tudo começa
requirements.txt
README.md
LICENSE
```

## Bibliotecas usadas

- CustomTkinter - pra interface
- PyAutoGUI - pra simular os cliques
- keyboard - pra pegar os atalhos globais

## Problemas comuns

- **`py` não é reconhecido**: instala o Python de novo marcando a opção de adicionar ao PATH
- **Não consigo ativar o venv**: roda `Set-ExecutionPolicy -Scope Process Bypass` no PowerShell antes
- **Atalho não funciona**: tenta outra combinação, tem atalho que o Windows já usa pra outra coisa
- **Não clica nada**: confere se aplicou o intervalo antes de dar Start

## Licença

MIT
=======
# Auto-Clicker
Auto Clicker para automação de mouse
>>>>>>> d3457fcce7f338140b9e33f7bac6c7c862005d3c
