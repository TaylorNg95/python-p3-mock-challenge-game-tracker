class Game:
    def __init__(self, title):
        self.title = title
    
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        if not hasattr(self,'title') and isinstance(title, str) and len(title) > 0:
            self._title = title
        """ else:
            raise ValueError('Title must be a non-empty string.') """

    def results(self):
        return [result for result in Result.all if result.game == self]

    def players(self):
        st = {}
        for result in Result.all:
            if result.game == self:
                st[result.player] = True
        return [key for key, value in st.items()]

    def average_score(self, player):
        results = self.results()
        matching_scores = [result.score for result in results if result.player == player]
        return sum(matching_scores) / len(matching_scores)

class Player:
    def __init__(self, username):
        self.username = username

    @property
    def username(self):
        return self._username
    
    @username.setter
    def username(self, username):
        if isinstance(username, str) and 2 <= len(username) <= 16:
            self._username = username
        """ else:
            raise Exception('Username must be a string between 2 and 16 characters.') """

    def results(self):
        return [result for result in Result.all if result.player == self]

    def games_played(self):
        st = {}
        for result in Result.all:
            if result.player == self:
                st[result.game] = True
        return [key for key, value in st.items()]

    def played_game(self, game):
        games_played = self.games_played()
        return True if game in games_played else False

    def num_times_played(self, game):
        games = [result.game for result in Result.all if result.player == self]
        return len([gm for gm in games if gm == game])

    @classmethod
    def highest_scored(cls, game):
        ## average score for each of those players
        ## maximum
        unique_players = game.players()
        if unique_players:
            average_scores = {}
            for player in unique_players:
                average_scores[player] = game.average_score(player)
            max_score = max([value for key, value in average_scores.items()])
            return [key for key, value in average_scores.items() if average_scores[key] == max_score][0] 
        else:
            return None

class Result:
    all = []

    def __init__(self, player, game, score):
        self.player = player
        self.game = game
        self.score = score
        Result.all.append(self)

    @property
    def player(self):
        return self._player

    @player.setter
    def player(self, player):
        if isinstance(player, Player):
            self._player = player

    @property
    def game(self):
        return self._game

    @game.setter
    def game(self, game):
        if isinstance(game, Game):
            self._game = game

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, score):
        if not hasattr(self, 'score') and isinstance(score, int) and 1 <= score <= 5000:
            self._score = score