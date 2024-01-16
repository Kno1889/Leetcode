class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        winners = {}
        losers = {}
        no_losses = []
        one_loss = []

        for match in matches:
            winners[match[0]] = winners.get(match[0], 0) + 1
            losers[match[1]] = losers.get(match[1], 0) + 1
        
        for player in winners:
            if not player in losers:
                no_losses.append(player)

        for player in losers:
            if losers[player] == 1:
                one_loss.append(player)

        return [sorted(no_losses), sorted(one_loss)] 
        