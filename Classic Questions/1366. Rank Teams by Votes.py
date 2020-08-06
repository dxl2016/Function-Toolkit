class Solution:
    def rankTeams(self, votes: List[str]) -> str:
        if len(votes) == 1:
            return votes[0]
        
        n = len(votes[0])
        teams = {}

        for v in votes:
            for i, c in enumerate(v):
                if c not in teams:
                    teams[c] = [0] * n
                teams[c][i] += 1
        
        result = []
        for (k,v) in teams.items():
            result.append(v + [-ord(k)])
        result = sorted(result, reverse=True)
        
        return "".join(chr(-v[-1]) for v in result)

