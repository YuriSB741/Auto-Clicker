import math
import threading
import time
from tkinter import messagebox

import customtkinter as ctk
import keyboard
import pyautogui as pa


class AutoClicker:

    def __init__(self, janela):
        self.shortcut = []
        self.hotkey_id = None
        self.intervalo_valor = []
        self.rodando = False
        self.janela = janela
        self.janela_opcoes = None
        self.botao_start = None
        self.aviso_id = None
        self.janela.title("YB Auto Clicker")
        self.janela.geometry("300x200")

    def definir_botao_start(self, botao_start):
        self.botao_start = botao_start

    def iniciar_autoclicker(self):
        if not self.intervalo_valor:
            messagebox.showwarning("Aviso", "Nenhum valor de intervalo foi inserido")
            return
        self._remover_atalho()
        self.botao_start.configure(text="Stop", command=self.parar_autoclicker, hover_color="red", fg_color="red")
        if not self.rodando:
            self.rodando = True
            threading.Thread(target=self.loop, daemon=True).start()
            if self.shortcut:
                self.hotkey_id = keyboard.add_hotkey(self.shortcut[0], self._agendar_parada)

    def parar_autoclicker(self):
        self._remover_atalho()
        self.botao_start.configure(text="Start", command=self.iniciar_autoclicker, hover_color="#144870", fg_color="#3a7ebf")
        self.rodando = False
        if self.shortcut:
            self.hotkey_id = keyboard.add_hotkey(self.shortcut[0], self._agendar_inicio)

    def _remover_atalho(self):
        if self.hotkey_id is not None:
            keyboard.remove_hotkey(self.hotkey_id)
            self.hotkey_id = None

    def _agendar_inicio(self):
        self.janela.after(0, self.iniciar_autoclicker)

    def _agendar_parada(self):
        self.janela.after(0, self.parar_autoclicker)

    def loop(self):
        while self.rodando:
            time.sleep(self.value)
            if self.rodando:
                pa.click()

    def opcoes_interface(self):
        if self.rodando:
            self.parar_autoclicker()
            messagebox.showerror("Erro", "Não é possível abrir esta janela no momento")
            return
        if self.janela_opcoes is not None and self.janela_opcoes.winfo_exists():
            self.janela_opcoes.focus()
            return
        self.janela_opcoes = ctk.CTkToplevel(self.janela)
        self.janela_opcoes.resizable(False, False)
        self.janela_opcoes.title("Options")
        self.janela_opcoes.geometry("550x300")
        self.janela_opcoes.attributes("-topmost", True)
        self.janela_opcoes.protocol("WM_DELETE_WINDOW", self._fechar_janela_opcoes)
        self.janela_opcoes.geometry(f"+{self.janela.winfo_x() + 50}+{self.janela.winfo_y() + 50}")
        for i in range(8):
            self.janela_opcoes.rowconfigure(i, weight=1)
        for i in range(10):
            self.janela_opcoes.columnconfigure(i, weight=1)
        ctk.CTkLabel(self.janela_opcoes, text="Interval:", font=("Verdana", 14)).grid(row=0, columnspan=2)
        self.entry_hours = self._criar_entrada(0, 2)
        ctk.CTkLabel(self.janela_opcoes, text="hours", font=("Verdana", 9)).grid(row=0, column=3)
        self.entry_minutes = self._criar_entrada(0, 4)
        ctk.CTkLabel(self.janela_opcoes, text="minutes", font=("Verdana", 9)).grid(row=0, column=5)
        self.entry_seconds = self._criar_entrada(0, 6)
        ctk.CTkLabel(self.janela_opcoes, text="seconds", font=("Verdana", 9)).grid(row=0, column=7)
        self.entry_milliseconds = self._criar_entrada(0, 8)
        ctk.CTkLabel(self.janela_opcoes, text="milliseconds", font=("Verdana", 9)).grid(row=0, column=9)
        self.botao_aplicar = ctk.CTkButton(self.janela_opcoes, text="Aplicar", font=("Verdana", 13), width=50, command=self.aplicar)
        self.botao_aplicar.grid(row=7, column=9)
        self.aviso_aplicado = ctk.CTkLabel(
            self.janela_opcoes,
            text="",
            font=("Verdana", 11),
            text_color="#218c4a",
        )
        self.aviso_aplicado.grid(row=6, column=6, columnspan=4)
        ctk.CTkLabel(self.janela_opcoes, text="Shortcut:", font=("Verdana", 14)).grid(row=2, columnspan=2)
        self.entry_hotkey = ctk.CTkEntry(
            self.janela_opcoes,
            width=120,
            height=20,
            justify="center",
            placeholder_text="Pressione uma tecla",
            state="readonly",
        )
        self.entry_hotkey.grid(row=2, column=2)
        self.entry_hotkey.bind("<KeyPress>", self.capturar_atalho)
        if self.shortcut:
            self._exibir_atalho(self.shortcut[0])

    def _criar_entrada(self, row, column):
        entrada = ctk.CTkEntry(self.janela_opcoes, width=50, justify="right")
        entrada.grid(row=row, column=column)
        return entrada

    def _fechar_janela_opcoes(self):
        """Cancela tarefas pendentes antes de destruir a janela de opções."""
        if self.aviso_id is not None:
            self.janela.after_cancel(self.aviso_id)
            self.aviso_id = None
        self.janela_opcoes.destroy()
        self.janela_opcoes = None

    def capturar_atalho(self, event):
        """Registra a tecla ou combinação pressionada no campo de atalho."""
        teclas_modificadoras = {"Control_L", "Control_R", "Shift_L", "Shift_R", "Alt_L", "Alt_R"}
        if event.keysym in teclas_modificadoras:
            return "break"

        if event.keysym in {"Escape", "BackSpace", "Delete"}:
            self._exibir_atalho("")
            return "break"

        nomes_teclas = {
            "Return": "enter",
            "Prior": "page up",
            "Next": "page down",
            "Caps_Lock": "caps lock",
            "Print": "print screen",
            "Scroll_Lock": "scroll lock",
            "Num_Lock": "num lock",
            "KP_Enter": "enter",
        }
        tecla = nomes_teclas.get(event.keysym, event.keysym.lower())
        modificadores = []
        if event.state & 0x0004:
            modificadores.append("ctrl")
        if event.state & 0x0001:
            modificadores.append("shift")
        if event.state & 0x0008:
            modificadores.append("alt")
        self._exibir_atalho("+".join([*modificadores, tecla]))
        return "break"

    def _exibir_atalho(self, atalho):
        self.entry_hotkey.configure(state="normal")
        self.entry_hotkey.delete(0, "end")
        self.entry_hotkey.insert(0, atalho)
        self.entry_hotkey.configure(state="readonly")

    def aplicar(self):
        try:
            valores = (float(self.entry_hours.get().strip() or 0) * 3600, float(self.entry_minutes.get().strip() or 0) * 60, float(self.entry_seconds.get().strip() or 0), float(self.entry_milliseconds.get().strip() or 0) / 1000)
        except ValueError:
            messagebox.showerror("Erro de Entrada", "Por favor insira apenas números válidos", parent=self.janela_opcoes)
            return
        if any(valor < 0 or not math.isfinite(valor) for valor in valores):
            messagebox.showerror("Erro de Entrada", "Por favor insira apenas números válidos", parent=self.janela_opcoes)
            return
        self.intervalo_total = sum(valores)
        if self.intervalo_total <= 0:
            messagebox.showwarning("Aviso", "Não foi encontrado valores", parent=self.janela_opcoes)
            return
        if self.intervalo_valor:
            self.intervalo_valor[0] = self.intervalo_total
        else:
            self.intervalo_valor.append(self.intervalo_total)
        self.value = self.intervalo_valor[0]
        hotkey = self.entry_hotkey.get().strip().lower()
        try:
            if hotkey:
                keyboard.parse_hotkey(hotkey)
                self._remover_atalho()
                self.shortcut[:] = [hotkey]
                self.hotkey_id = keyboard.add_hotkey(hotkey, self._agendar_inicio)
            elif self.shortcut:
                self._remover_atalho()
                self.shortcut.clear()
        except Exception:
            messagebox.showerror("Erro de Entrada", "Por favor insira um atalho válido", parent=self.janela_opcoes)
            return
        self.aviso_alteracao()

    def aviso_alteracao(self):
        if self.aviso_id is not None:
            self.janela.after_cancel(self.aviso_id)
        self.botao_aplicar.configure(text="Aplicado", font=("Verdana", 10), hover_color="green", fg_color="green")
        self.aviso_aplicado.configure(text="Alterações aplicadas!")
        self.aviso_id = self.janela.after(2000, self._restaurar_botao_aplicar)

    def _restaurar_botao_aplicar(self):
        self.botao_aplicar.configure(text="Aplicar", font=("Verdana", 13), hover_color="#144870", fg_color="#3a7ebf")
        self.aviso_aplicado.configure(text="")
        self.aviso_id = None
