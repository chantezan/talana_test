class AbstractCharacter:
    def __init__(self):
        self.combos = [{'name': 'Puño', 'moves': '', 'hit': 'P', 'energy': 1},
                       {'name': 'Patada', 'moves': '', 'hit': 'K', 'energy': 1},
                       ]
        self.turn = 0
        self.end = False
        self.energy = 6

    def action(self):
        moves = self.plays['movimientos'][self.turn]
        hit = self.plays['golpes'][self.turn]
        self.moves_free = moves
        self.combo_hit = None
        for combo in self.combos:
            combo_len_temp = len(combo['moves'])
            #esto retorna el ultimo match ya que estan ordenados de menor a mayor fuerza y se prioriza eso
            if (moves[-combo_len_temp:] == combo['moves'] or combo_len_temp == 0) and hit == combo['hit']:
                self.moves_free = moves[:combo_len_temp]
                self.combo_hit = combo

    def dismiss(self,energy):
        self.energy = self.energy - energy

    #encagardo de hacer la siguien te jugada
    def play(self):
        if self.end:
            self.moves_free = ''
            self.combo_hit = None
            return
        self.action()
        self.turn = self.turn + 1
        if (self.turn >= self.max_plays):
            self.end = True

    def history(self):
        if not(self.combo_hit) and not(self.moves_free):
            print(f'{self.name} no hace nada')
        elif not(self.moves_free) and self.combo_hit:
            print(f'{self.name} golpea con {self.combo_hit["name"]}')
        elif self.moves_free and not(self.combo_hit):
            print(f'{self.name} se mueve')
        else:
            print(f'{self.name} se mueve y golpea con {self.combo_hit["name"]}')

    def win(self):
        print(f'{self.name} ha ganado y le quedan {self.energy} de energia')

    def compare(self, player):
        if self.combo_hit == player.combo_hit:
            return len(self.moves_free) <= len(player.moves_free)
        elif not self.combo_hit:
            return False
        elif not player.combo_hit:
            return True
        else:
            if len(self.combo_hit['moves']) != len(player.combo_hit['moves']):
                return len(self.combo_hit['moves']) < len(player.combo_hit['moves'])
            else:
                return len(self.moves_free) <= len(player.moves_free)
            
# los combos se setean de mayor a menor para que retorne el ultimo match desde action
class Stallone(AbstractCharacter):
    def __init__(self,plays):
        super().__init__()
        self.name = "Tonyn"
        self.combos.append({'name': 'Remuyuken', 'moves': 'SD', 'hit': 'K', 'energy': 2})
        self.combos.append({'name': 'Taladoken', 'moves': 'DSD', 'hit': 'P', 'energy': 3})
        self.plays = plays
        self.max_plays = len(plays['movimientos'])

class Arnaldoe(AbstractCharacter):
    def __init__(self,plays):
        super().__init__()
        self.name = "Arnaldor"
        self.combos.append({'name': 'Taladoken', 'moves': 'ASA', 'hit': 'P', 'energy': 2})
        self.combos.append({'name': 'Remuyuken', 'moves': 'SA', 'hit': 'K', 'energy': 3})
        self.plays = plays
        self.max_plays = len(plays['movimientos'])


class Game:
    def __init__(self,plays):
        self.player1 = Stallone(plays['player1'])
        self.player2 = Arnaldoe(plays['player2'])

    #esta funcion se encarga de iniciar el juego, haciendo un loop hasta que no quedan mas jugadas o termina el juego
    def start(self):
        players = [self.player1, self.player2]
        while self.player1.end == False or self.player2.end == False:
            for player in players:
                player.play()
            #si priority es True, comienza el jugador1 si es False comienza el jugador2
            priority = self.player1.compare(self.player2)
            # jugador que primero mueve
            if players[not(priority)].combo_hit:
                players[priority].dismiss(players[not(priority)].combo_hit['energy'])
            players[not(priority)].history()
            if(players[priority].energy < 1):
                players[not(priority)].win()
                return

            # jugador que mueve segundo
            if players[priority].combo_hit:
                players[not (priority)].dismiss(players[priority].combo_hit['energy'])
            players[priority].history()
            if (players[not (priority)].energy < 1):
                players[priority].win()
                return

        print("juego termino sin ganadores")


#ejemplos del enunciado
plays = {"player1":{"movimientos":["D","DSD","S","DSD","SD"],"golpes":["K","P","","K","P"]},"player2": {"movimientos":["SA","SA","SA","ASA","SA"],"golpes":["K","","K","P","P"]}}

a = Game(plays)
a.start()

plays2 = {"player1":{"movimientos":["SDD", "DSD", "SA", "DSD"] ,"golpes":["K", "P", "K", "P"]},
          "player2":{"movimientos":["DSD", "WSAW", "ASA", "", "ASA", "SA"],"golpes":["P", "K", "K", "K", "P", "K"]}}

b = Game(plays2)
b.start()

plays3 = {"player1":{"movimientos":["DSD", "S"] ,"golpes":[ "P", ""]},
"player2":{"movimientos":["", "ASA", "DA", "AAA", "", "SA"],"golpes":["P", "", "P", "K", "K", "K"]}}

c = Game(plays3)
c.start()
