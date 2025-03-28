from logic import *

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")

# Puzzle 0
# A says "I am both a knight and a knave."
knowledge0 = And( AKnave, Implication (AKnight, And(AKnight, AKnave)))
    


# Puzzle 1
# A says "We are both knaves."
# B says nothing.
knowledge1 = And( AKnave, Implication(AKnight, And(AKnave, BKnave)), BKnight
    # TODO
)

# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."
knowledge2 = And(
    # A must be either a knight or a knave (but not both)
    Or(AKnight, AKnave),
    Not(And(AKnight, AKnave)),

    # B must be either a knight or a knave (but not both)
    Or(BKnight, BKnave),
    Not(And(BKnight, BKnave)),

    # If A is a knight, then A and B are the same (both knights or both knaves)
    Implication(AKnight, Biconditional(AKnight, BKnight)),

    # If A is a knave, then A and B are different (one knight, one knave)
    Implication(AKnave, Not(Biconditional(AKnight, BKnight))),

    # If B is a Knight, then A must be a Knave
    Implication(BKnight, AKnave)
)




# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.
# B says "A said 'I am a knave'."
# B says "C is a knave."
# C says "A is a knight."
knowledge3 = And(
    # A can only be one of these two
    Or(AKnight, AKnave),
    Not(And(AKnight, AKnave)),

    # B can only be one of these two
    Or(BKnight, BKnave),
    Not(And(BKnight, BKnave)),

    # C can only be one of these two
    Or(CKnight, CKnave),
    Not(And(CKnight, CKnave)),

    # B's first statement: "A said 'I am a knave.'"
    Implication(BKnight, Biconditional(AKnight, AKnave)),

    # B's second statement: "C is a knave."
    Implication(BKnight, CKnave),
    Implication(BKnave, CKnight),

    # C's statement: "A is a knight."
    Implication(CKnight, AKnight)
)






def main():
    symbols = [AKnight, AKnave, BKnight, BKnave, CKnight, CKnave]
    puzzles = [
        ("Puzzle 0", knowledge0),
        ("Puzzle 1", knowledge1),
        ("Puzzle 2", knowledge2),
        ("Puzzle 3", knowledge3)
    ]
    for puzzle, knowledge in puzzles:
        print(puzzle)
        if len(knowledge.conjuncts) == 0:
            print("    Not yet implemented.")
        else:
            for symbol in symbols:
                if model_check(knowledge, symbol):
                    print(f"    {symbol}")


if __name__ == "__main__":
    main()
