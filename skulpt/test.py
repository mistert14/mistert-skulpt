import chess

def montrer_echiquier(jeu):
    lines = str(jeu.board).split(' ')
    for l in lines:
        print l
    print "\n"

jeu = chess.Game(None,None)

montrer_echiquier(jeu)

jeu.move('d2-d4')
jeu.advance()

montrer_echiquier(jeu)

jeu.move('d7-d5')
jeu.advance()

montrer_echiquier(jeu)

