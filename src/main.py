import customtkinter as ctk

from autoclicker import AutoClicker
from interface import criar_janela

def main():
    ctk.set_appearance_mode("light")
    janela = ctk.CTk()
    app = AutoClicker(janela)
    criar_janela(app)
    janela.mainloop()

if __name__ == "__main__":
    main()
