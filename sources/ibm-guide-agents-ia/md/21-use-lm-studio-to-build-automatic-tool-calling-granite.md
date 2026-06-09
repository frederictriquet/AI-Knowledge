> Source : https://www.ibm.com/fr-fr/think/tutorials/use-lm-studio-to-build-automatic-tool-calling-granite

# Utiliser LM Studio pour automatiser l’appel d’outils avec Granite

Dans ce tutoriel détaillé, vous utiliserez LM Studio avec le modèle d’instruction open source IBM®  Granite 3.3-8b sur votre machine locale. Dans un premier temps, vous testerez le modèle local tel quel, puis vous écrirez des fonctions Python que le modèle pourra utiliser pour l’appel automatique d’outils. Enfin, vous développerez d’autres fonctions pour jouer à un jeu d’échecs avec un [agent IA](https://www.ibm.com/fr-fr/think/topics/ai-agents). Ce tutoriel est également disponible sur GitHubGranite Snackbook de la communauté IBM Granite sous la forme d’un Jupyter Notebook.

## LM Studio

LM Studio est une application qui permet de travailler localement avec les \[grands modèles de langage\] (https://ibm.com/fr-fr/think/topics/large-language-models) (LLM). Vous pouvez utiliser n’importe quel [modèle open source](https://ibm.com/fr-fr/think/topics/open-source-llms) avec LM Studio, comme les modèles \[Mistral AI\](https://ibm.com/fr-fr /think/topics/mistral-ai), [Gemma de Google](https://ibm.com/fr-fr/think/topics/google-gemma), Llama de Meta ou \[R1 de DeepSeek\] (https://ibm.com/fr-fr/think/topics/deepseek) (série).

Grâce à LM Studio, les utilisateurs (débutants ou avancés) peuvent exécuter des LLM avec le processeur de leur ordinateur ou même un [GPU](https://www.ibm.com/fr-fr/think/topics/gpu). LM Studio offre une interface de type chat pour interagir avec les LLM locaux, similaire à celle de [ChatGPT](https://www.ibm.com/fr-fr/think/topics/chatgpt).  

Avec un modèle d’IA local, vous pouvez [affiner](https://www.ibm.com/fr-fr/think/topics/fine-tuning), [réaliser des inférences](https://www.ibm.com/fr-fr/think/topics/ai-inference) et plus encore, sans avoir à vous soucier des appels d’\[API\] externes (https://www.ibm.com/fr-fr/think/topics/api) (comme les interfaces de programmation d’application OpenAI ou IBM watsonx.ai), ni de l’utilisation de tokens. LM Studio permet également aux utilisateurs de « discuter avec les documents » en local et en privé. L’utilisateur peut joindre un document à la session de chat et poser des questions à ce sujet. Si le document est long, LM Studio configurera un système de [génération augmentée par récupération](https://www.ibm.com/fr-fr/think/topics/retrieval-augmented-generation) (RAG) pour l’interrogation.

## Appel d’outil

Si les LLM excellent dans la compréhension et la production de textes à caractère humain, ils se heurtent souvent à des limites lorsque les tâches exigent des calculs précis, l’accès à des données externes en temps réel ou l’exécution de procédures spécifiques et bien définies. En mettant en œuvre [l’appel d’outils](https://www.ibm.com/fr-fr/think/topics/tool-calling), nous équipons les LLM d’un ensemble d’« outils », c’est-à-dire de fonctions externes, qu’ils peuvent choisir d’appeler et qui peuvent étendre considérablement leurs capacités. Ce tutoriel montrera comment définir ces outils et les intégrer, ce qui permettra au LLM d’effectuer un plus grand nombre de tâches avec une plus grande fiabilité.

## Étapes

### Étape 1. Installer LM Studio

Avant d’installer LM Studio, vérifiez si votre machine locale répond à la configuration minimale requise.

Ensuite, téléchargez le programme d'installation correspondant au système d’exploitation de votre ordinateur (Windows, macOS ou Linux). Suivez ensuite ces instructions pour télécharger les modèles sur votre machine locale.

Ici, nous utiliserons le modèle d’instruction Granite 3.3-8b, mais n’hésitez pas à utiliser le LLM de votre choix. Si vous utilisez le modèle Granite, vous pouvez rechercher la chaîne d’utilisateur/de modèle correspondante`ibm-granite/granite-3.3-8b-instruct-GGUF` dans le`Select a model to load` dans LM Studio.

Ensuite, démarrez le serveur local LM Studio à l’aide de`Developer` l’icône verte en haut à gauche de LM Studio. Faites basculer la`Status` barre en haut à gauche pour`Running` .

### Étape 2. Installer les dépendances

Nous devons d’abord installer les bibliothèques nécessaires, notamment le SDK LM Studio et la bibliothèque d’échecs.

```
%pip install git+https://github.com/ibm-granite-community/utils \
    lmstudio \
    chess
```

```python
import lmstudio as lms
```

### Étape 3. Charger le modèle

Nous spécifierons ensuite le modèle que nous souhaitons utiliser dans cette recette. Dans notre cas, il s’agira du modèle que nous avons téléchargé dans LM Studio, Granite 3.3-8b instruction.

Nous commencerons à discuter avec lui en appelant 'model.respond()' avec un premier message.

```python
model = lms.llm("ibm-granite/granite-3.3-8b-instruct-GGUF")

print(model.respond("Hello Granite!"))
```

### Étape 4. Effectuer un calcul sans outils

Commençons par demander au modèle de faire un calcul simple.

```python
print(model.respond("What is 26.97 divided by 6.28? Don't round."))
```

Si le modèle est capable de fournir une approximation proche, il ne renverra pas la réponse exacte, car il ne peut pas calculer le quotient seul.

### Étape 5. Créer des outils de calcul avec les fonctions Python

Pour résoudre ce problème, nous fournirons des outils au modèle. Les outils sont des fonctions Python que nous fournissons au modèle lors de l’inférence. Le modèle peut choisir d’appeler un ou plusieurs de ces outils pour répondre à la requête de l’utilisateur.

Consultez la documentation LM Studio pour en savoir plus sur la création d’outils. En général, vous devez vous assurer que vos fonctions d’outil ont un nom approprié, des types d’entrée et de sortie définis, ainsi qu’une description qui explique l’objectif de l’outil. Toutes ces informations sont transmises au modèle pour l’aider à sélectionner l’outil approprié pour répondre à votre requête.

Nous écrirons plusieurs fonctions mathématiques simples, que le modèle pourra utiliser comme outils :

```python
def add(a: float, b:float):
    """Given two numbers a and b, return a + b."""
    return a + b

def subtract(a: float, b:float):
    """Given two numbers a and b, return a - b."""
    return a - b

def multiply(a: float, b: float):
    """Given two numbers a and b, return a * b."""
    return a * b

def divide(a: float, b: float):
    """Given two numbers a and b, return a / b."""
    return a / b

def exp(a: float, b:float):
    """Given two numbers a and b, return a^b"""
    return a ** b
```

Maintenant, nous pouvons réexécuter la même requête tout en fournissant au modèle quelques outils pour l’aider à répondre. Nous utiliserons « model.act() » pour appeler automatiquement l’outil et indiquer au modèle qu’il peut utiliser les fonctions que nous avons créées.

```
model.act(
  "What is 26.97 divided by 6.28? Don't round.",
  [add, subtract, multiply, divide, exp],
  on_message=print,
)
```

Nous constatons que le modèle a pu sélectionner l’outil approprié sous « ToolCallRequest », « name », a utilisé les entrées appropriées sous « arguments » (les arguments pour transmettre à la fonction) et a évité d’utiliser les outils non pertinents. Enfin, sous « AssistantResponse », « content », « text » est affichée la réponse du modèle, une réponse exacte à la question.

### Combien de R dans le mot « strawberry » ?

Une question très simple, à laquelle se heurtent même les modèles de langage les plus intelligents. Presque tous les LLM avec une date limite d’entraînement antérieure à 2024 répondent qu’il n’y a que 2 R dans le mot « strawberry ». En prime, ils peuvent même halluciner quant à la position des lettres.

De nos jours, les LLM ont tendance à répondre correctement à cette question, simplement parce que sa viralité l’a fait figurer dans la plupart des jeux de données. Cependant, les LLM échouent encore souvent à des tâches similaires de comptage des lettres.

```python
print(model.respond("How many Bs are in the word 'blackberry'?"))
```

Nous allons écrire un outil pour aider le modèle à faire un meilleur travail.

```python
def get_letter_frequency(word: str) -> dict:
    """Takes in a word (string) and returns a dictionary containing the counts of each letter that appears in the word. """

    letter_frequencies = {}

    for letter in word:
        if letter in letter_frequencies:
            letter_frequencies[letter] += 1
        else:
            letter_frequencies[letter] = 1

    return letter_frequencies
```

Maintenant, nous pouvons transmettre l’outil au modèle et réexécuter le prompt.

```
model.act(
  "How many Bs are in the word 'blackberry'?",
  [get_letter_frequency],
  on_message=print,
)
```

Grâce à l’outil « get_letter_frequency() », le modèle a pu compter avec précision le nombre de « b » dans le mot « blackberry ».

### Étape 6. Mettre en œuvre un outil d’appel automatique pour un agent

L’un des meilleurs cas d’utilisation de ce workflow d’appel automatique d’outils consiste à donner à votre modèle la possibilité d’interagir avec son environnement externe. Créons un agent qui utilise des outils pour jouer aux échecs !

Bien que les modèles de langage puissent avoir une solide connaissance conceptuelle des échecs, ils ne sont pas intrinsèquement conçus pour comprendre un échiquier. Si vous essayez de jouer à un jeu d’échecs avec un chatbot en ligne, il déraille souvent après plusieurs tours, effectuant des déplacements illégitimes ou irrationnels.

Nous fournissons au modèle plusieurs outils qui l’aident à comprendre et à interagir avec le conseil d’administration.

- **legal_moves()** : fournit la liste de tous les mouvements légaux dans la position actuelle
- **possible_captures()** : fournit une liste de toutes les prises possibles à la position actuelle
- **possible_checks()** : fournit une liste de tous les contrôles possibles à la position actuelle
- **get_move_history()** : fournit la liste de tous les mouvements joués jusqu’à présent
- **get_book_moves()** : fournit une liste de tous les mouvements de livres
- **make_ai_move()** : une interface permettant au modèle d’entrer son mouvement

Ce n’est pas beaucoup, mais c’est suffisant pour que le modèle puisse jouer une partie d’échecs complète sans halluciner et utiliser un raisonnement intelligent pour fonder ses décisions.

```python
import chess
import chess.polyglot
from IPython.display import display, SVG, clear_output
import random
import os, requests, shutil, pathlib

board = chess.Board()
ai_pos = 0

# Download book moves
RAW_URL   = ("https://raw.githubusercontent.com/"
             "niklasf/python-chess/master/data/polyglot/performance.bin")
DEST_FILE = "performance.bin"

if not os.path.exists(DEST_FILE):
    print("Downloading performance.bin …")
    try:
        with requests.get(RAW_URL, stream=True, timeout=15) as r:
            r.raise_for_status()
            with open(DEST_FILE, "wb") as out:
                shutil.copyfileobj(r.raw, out, 1 << 16)  # 64 KB chunks
    except requests.exceptions.RequestException as e:
        raise RuntimeError(f"Download failed: {e}")

def legal_moves() -> list[str]:
    """
    Returns a list of legal moves in standard algebraic notation.
    """
    return [board.san(move) for move in board.legal_moves]

def possible_captures() -> list[dict]:
    """
    Returns all legal captures with metadata:
    - san: SAN notation of the capture move.
    - captured_piece: The piece type being captured ('P','N','B','R','Q','K').
    - is_hanging: True if the captured piece was undefended before the capture.
    """
    result = []
    for move in board.generate_legal_captures():
        piece = board.piece_at(move.to_square)
        piece_type = piece.symbol().upper() if piece else "?"
        # Check defenders of the target square
        defenders = board.attackers(not board.turn, move.to_square)
        is_hanging = len(defenders) == 0  # no defenders => hanging

        result.append({
            "san": board.san(move),
            "captured_piece": piece_type,
            "is_hanging": is_hanging
        })
    return result

def possible_checks() -> list[dict]:
    """
    Returns all legal checking moves with metadata:
    - san: SAN notation of the checking move.
    - can_be_captured: True if after the move, the checking piece can be captured.
    - can_be_blocked: True if the check can be legally blocked.
    - can_escape_by_moving_king: True if the king can move out of check.
    """
    result = []
    for move in board.legal_moves:
        if not board.gives_check(move):
            continue
        temp = board.copy()
        temp.push(move)

        can_capture = any(
            temp.is_capture(reply) and reply.to_square == move.to_square
            for reply in temp.legal_moves
        )

        # King escapes by moving
        king_sq = temp.king(not board.turn)
        can_escape = any(
            reply.from_square == king_sq for reply in temp.legal_moves
        )

        # Blocking: legal non-capture, non-king move that resolves check
        can_block = any(
            not temp.is_capture(reply)
            and reply.from_square != king_sq
            and not temp.gives_check(reply)
            for reply in temp.legal_moves
        )

        result.append({
            "san": board.san(move),
            "can_be_captured": can_capture,
            "can_be_blocked": can_block,
            "can_escape_by_moving_king": can_escape
        })
    return result

def get_move_history() -> list[str]:
    """
    Returns a list of moves made in the game so far in standard algebraic notation.
    """
    return [board.san(move) for move in board.move_stack]

def get_book_moves() -> list[str]:
    """
    Returns a list of book moves in standard algebraic notation from performance.bin
    for the current board position. If no book moves exist, returns an empty list.
    """
    moves = []
    with chess.polyglot.open_reader("performance.bin") as reader:
        for entry in reader.find_all(board):
            san_move = board.san(entry.move)
            moves.append(san_move)
    return moves

def is_ai_turn() -> bool:
    return bool(board.turn) == (ai_pos == 0)

def make_ai_move(move: str) -> None:
    """
    Given a string representing a valid move in chess notation, pushes move onto chess board.
    If non-valid move, raises a ValueError with message "Illegal move.
    If called when it is not the AI's turn, raises a ValueError with message "Not AI's turn."
    THIS FUNCTION DIRECTLY ENABLES THE AI TO MAKE A MOVE ON THE CHESS BOARD.
    """
    if is_ai_turn():
        try:
            board.push_san(move)
        except ValueError as e:
            raise ValueError(e)
    else:
        raise ValueError("Not AI's turn.")

def make_user_move(move: str) -> None:
    """
    Given a string representing a valid move in chess notation, pushes move onto chess board.
    If non-valid move, raises a ValueError with message "Illegal move.
    If called when it is not the player's turn, raises a ValueError with message "Not player's turn."
    If valid-move, updates the board and displays the current state of the board.
    """
    if not is_ai_turn():
        try:
            board.push_san(move)
        except ValueError as e:
            raise ValueError(e)
    else:
        raise ValueError("Not player's turn.")

def print_fragment(fragment, round_index=0):
    print(fragment.content, end="", flush=True)
```

Ensuite, nous préparerons la partie d’échecs avec un agent IA. En utilisant l’appel `lms.Chat()`, nous fournirons des instructions à notre agent IA pour les échecs lorsque l’agent joue pour les blancs ou les noirs.

```
chat_white = lms.Chat("""You are a chess AI, playing for white. Your task is to make the best move in the current position, using the provided tools.
                      You should use your overall chess knowledge, including openings, tactics, and strategies, as your primary method to determine good moves.
                      Use the provided tools as an assistant to improve your understanding of the board state and to make your moves. Always use the book moves
                      if they are available. Be prudicious with your checks and captures. Understand whether the capturable piece is hanging, and its value in
                      comparison to the piece you are using to capture. Consider the different ways the opponent can defend a check, to pick the best option.""")

chat_black = lms.Chat("""You are a chess AI, playing for black. Your task is to make the best move in the current position, using the provided tools.
                      You should use your overall chess knowledge, including openings, tactics, and strategies, as your primary method to determine good moves.
                      Use the provided tools as an assistant to improve your understanding of the board state and to make your moves. Always use the book moves
                      if they are available. Be prudicious with your checks and captures. Understand whether the capturable piece is hanging, and its value in
                      comparison to the piece you are using to capture. Consider the different ways the opponent can defend a check, to pick the best option.""")
```

Enfin, nous mettrons en place deux fonctions pour suivre le match : `update_board()` et `get_end_state()`.

En utilisant l’appel `model.act()` que nous avons utilisé pour l’outil précédemment, nous allons donner à l’agent les instructions (`chat`) que nous avons définies, les outils disponibles pour son utilisation et établir un `max_prediction_rounds`. Cette fonction indique le nombre maximum d’appels d’outils indépendants que l’agent peut effectuer pour déplacer un mouvement spécifique.

Après l’exécution de la cellule suivante, un champ d’entrée vide devrait s’afficher pour que vous puissiez écrire vos déplacements. Si vous n’êtes pas sûre des déplacements disponibles, tapez « help » et la notation des déplacements disponibles sera affichée, la première initiale étant le nom de la pièce (\\ "B \\ est bishop, \\ " Q \\ " est queen, etc. Mais \\N\\ est Knight, car \\K\\ représente le roi et qu’il n’y a pas de première initiale pour un pion). La lettre et le chiffre suivants indiquent la ligne et la colonne où déplacer la pièce. Pour la notation de cas particuliers comme le roque ou le déplacement de pièces ambiguës, voir la page Wikipédia sur la notation algébrique (échecs).

Bonne chance !

```python
move = 0
import chess.svg

board.reset()
ai_pos = round(random.random())

def update_board(move = move, ai_pos = ai_pos):
    """
    Updates the chess board display in the notebook.
    """
    clear_output(wait=True)  # Clear previous output
    print(f"Board after move {move+1}")
    if (ai_pos == 1):
        display(SVG(chess.svg.board(board, size=400)))
    else:
        display(SVG(chess.svg.board(board, size=400, orientation = chess.BLACK)))

def get_end_state():
    """
    Returns the end state of the chess game.
    """
    if board.is_checkmate():
        return "Checkmate!"
    elif board.is_stalemate():
        return "Stalemate!"
    elif board.is_insufficient_material():
        return "Draw by insufficient material!"
    elif board.is_seventyfive_moves():
        return "Draw by 75-move rule!"
    elif board.is_fivefold_repetition():
        return "Draw by fivefold repetition!"
    else:
        return None

clear_output(wait=True) # Clear any previous output from the cell
if (ai_pos == 1):
    display(SVG(chess.svg.board(board, size=400)))
else:
    display(SVG(chess.svg.board(board, size=400, orientation = chess.BLACK)))

# 2. Loop through moves, apply each move, clear previous output, and display new board
userEndGame = False
while True:

    if ai_pos == 0:
        # AI's turn
        model.act(
            chat_white,
            [get_move_history, legal_moves, possible_captures, possible_checks, get_book_moves, make_ai_move],
            on_message=print,
            max_prediction_rounds = 8,
        )

        if is_ai_turn(): # failsafe in case AI does not make a move
           make_ai_move(legal_moves()[0])  # Default to the first legal move if AI does not respond

        update_board(move)
        move += 1
        game_over_message = get_end_state()
        if game_over_message:
            print(game_over_message)
            break

        # User's turn
        while True:
            user_move = input("User (Playing Black): Input your move. Input 'help' to see the list of possible moves. Input 'quit' to end the game ->")
            if user_move.lower() == 'quit':
                print("Game ended by user.")
                userEndGame = True
                break
            if user_move.lower() == 'help':
                print("Possible moves:", legal_moves())
                continue
            try:
                make_user_move(user_move)
                break
            except ValueError as e:
                print(e)

        if userEndGame:
            break

        update_board(move)
        move += 1
        game_over_message = get_end_state()
        if game_over_message:
            print(game_over_message)
            break
    else:
        # User's turn
        while True:
            user_move = input("User (Playing White): Input your move. Input 'help' to see the list of possible moves. Input 'quit' to end the game ->")
            if user_move.lower() == 'quit':
                print("Game ended by user.")
                userEndGame = True
                break
            if user_move.lower() == 'help':
                print("Possible moves:", legal_moves())
                continue
            try:
                make_user_move(user_move)
                break
            except ValueError as e:
                print(e)

        if userEndGame:
            break

        update_board(move)
        move += 1
        game_over_message = get_end_state()
        if game_over_message:
            print(game_over_message)
            break

        model.act(
            chat_black,
            [get_move_history, legal_moves, possible_captures, possible_checks, get_book_moves, make_ai_move],
            max_prediction_rounds = 8,
            on_message=print,
        )

        if is_ai_turn(): # failsafe in case AI does not make a move
           make_ai_move(legal_moves()[0])  # Default to the first legal move if AI does not respond

        update_board(move)
        move += 1
        game_over_message = get_end_state()
        if game_over_message:
            print(game_over_message)
            break
```

## Récapitulatif

Dans ce notebook, nous avons démontré comment l’intégration des outils améliore la fonctionnalité et les capacités agentiques des LLM. Nous avons vu qu’en fournissant au LLM un accès à des fonctions externes prédéfinies, il peut dépasser ses capacités de base en matière de traitement du langage pour effectuer des tâches telles que les calculs précis ou l’interfaçage avec des systèmes externes. Il ne peut pas le faire efficacement tout seul. L’essentiel à retenir est que l’utilisation d’outils permet aux LLM de déléguer des sous-problèmes aux routines spécialisées, ce qui leur permet de fonder leurs réponses sur des données factuelles ou des opérations précises. Cette approche améliore leur précision et permet également aux LLM de s’engager dans des workflows interactifs plus complexes pour devenir des assistants plus polyvalents et plus puissants.
