class YatzyScoresheet:
    def score_ones(self, hand):
        return sum(hand.ones)
    
    def _score_set(self, hand, set_size):
        scores = [0]
        for worth, count in hand._sets.items():
            if count == set_size:
                scores.append(worth*set_size)
        return max(scores)
    
    def score_one_pair(self, hand):
        return self._score_set(hand, 2)
    
    def score_chance(self, hand):
        return sum(hand)
    
    def score_yatzy(self, hand):
        if len(set(hand)) == 1:
            return 50
        else:
            return 0