# 💣 Jogo da Bomba

Um jogo simples em Python para terminal onde o jogador tem **30 segundos para desarmar uma bomba** digitando a combinação correta de 3 dígitos.  
O jogo oferece **dois modos de dificuldade** e inclui cronômetro em tempo real.

---

## 🎮 Como jogar

Ao iniciar o jogo, você deve escolher um dos modos:

- `[1] Fácil`: você deve adivinhar **um dígito por vez** na sequência correta.
- `[2] Difícil`: você deve digitar **os três dígitos de uma vez só** (ex: `042`).

Mas atenção! Você tem apenas **30 segundos** para descobrir o código. Caso contrário... 💥

---

## 🛠 Requisitos

- Python 3.x
- Terminal com suporte a `clear` (Linux/macOS) ou `cls` (Windows)

---

## ▶️ Executando o jogo

Clone o repositório e execute o script:

```bash
git clone https://github.com/guilhermededeus/bomb-game.git
cd bomb-game
python bomb-game.py
