import customtkinter as ctk

def criar_janela(app):
    janela = app.janela
    janela.resizable(False, False)
    pos_x = int((janela.winfo_screenwidth() / 2) - 150)
    pos_y = int((janela.winfo_screenheight() / 2) - 100)
    janela.geometry(f"300x200+{pos_x}+{pos_y}")
    opcoes = ctk.CTkFrame(janela)
    opcoes.pack(fill="both", expand=True)
    for i in range(6):
        opcoes.rowconfigure(i, weight=1)
    for i in range(5):
        opcoes.columnconfigure(i, weight=1)
    ctk.CTkLabel(opcoes, text="YB Auto Clicker", font=("Verdana", 20)).grid(row=1, column=2)
    botao_start = ctk.CTkButton(opcoes, text="Start", font=("Verdana", 15), command=app.iniciar_autoclicker)
    botao_start.grid(row=3, column=2)
    app.definir_botao_start(botao_start)
    ctk.CTkButton(opcoes, text="Options", font=("Verdana", 13), command=app.opcoes_interface).grid(row=4, column=2)
