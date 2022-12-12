

from dataclasses import dataclass

raw = """A Y
B X
C Z
"""


@dataclass
class Guide:
    input1: str
    input2: str

    @staticmethod
    def parse_guide(s):
        input1, input2 = s.split()
        return Guide(input1, input2)
    
    
@dataclass
class Score:
    score1: int
    score2: int

    def calc_score1(self, guide: Guide):

        # calculate shape scores
        if guide.input2 == "X":
            self.score1 += 1
        if guide.input2 == "Y":
            self.score1 += 2
        if guide.input2 == "Z":
            self.score1 += 3

        # calculate outcome scores: draw
        if guide.input1 == "A" and guide.input2 == "X":
            self.score1 += 3

        if guide.input1 == "B" and guide.input2 == "Y":
            self.score1 += 3

        if guide.input1 == "C" and guide.input2 == "Z":
            self.score1 += 3

        # calculate outcome scores: won
        if guide.input1 == "A" and guide.input2 == "Y":
            self.score1 += 6

        if guide.input1 == "B" and guide.input2 == "Z":
            self.score1 += 6

        if guide.input1 == "C" and guide.input2 == "X":
            self.score1 += 6

    def calc_score2(self, guide: Guide):

        # calculate outcome scores
        if guide.input2 == "X":
            self.score2 += 0
        if guide.input2 == "Y":
            self.score2 += 3
        if guide.input2 == "Z":
            self.score2 += 6

        # calculate shape scores
        if guide.input1 == "A" and guide.input2 == "X":
            self.score2 += 3

        if guide.input1 == "A" and guide.input2 == "Y":
            self.score2 += 1

        if guide.input1 == "A" and guide.input2 == "Z":
            self.score2 += 2

        if guide.input1 == "B" and guide.input2 == "X":
            self.score2 += 1

        if guide.input1 == "B" and guide.input2 == "Y":
            self.score2 += 2

        if guide.input1 == "B" and guide.input2 == "Z":
            self.score2 += 3

        if guide.input1 == "C" and guide.input2 == "X":
            self.score2 += 2

        if guide.input1 == "C" and guide.input2 == "Y":
            self.score2 += 3

        if guide.input1 == "C" and guide.input2 == "Z":
            self.score2 += 1


if __name__ == "__main__":
    # example
    guides = [Guide.parse_guide(s) for s in raw.splitlines()]
    score = Score(score1=0, score2=0)
    for guide in guides:
        score.calc_score1(guide=guide)
        score.calc_score2(guide=guide)

    print(f'Example #1 solution: {score.score1}')
    print(f'Example #2 solution: {score.score2}')

    # task
    with open("./data/day02.txt") as f:
        raw = f.read()
    guides = [Guide.parse_guide(s) for s in raw.splitlines()]
    score = Score(score1=0, score2=0)
    for guide in guides:
        score.calc_score1(guide=guide)
        score.calc_score2(guide=guide)

    print(f'Task #1 solution: {score.score1}')
    print(f'Task #1 solution: {score.score2}')
