from collections import deque

def populateRecipes(recipes, elf1, elf2,i,step):

    while i <= step:
    
        s = recipes[elf1] + recipes[elf2]

        if s >= 10:
            score1 = 1
            score2 = s % 10
            recipes.append(score1)
            recipes.append(score2)
        else:
            recipes.append(s)

        nextElf1 = recipes[elf1] + 1
        nextElf2 = recipes[elf2] + 1

        elf1 = getNextPointers(elf1, nextElf1, recipes)
        elf2 = getNextPointers(elf2, nextElf2, recipes)
        i += 1

    return recipes

def getNextPointers(i, steps, recipes):
    while steps > 0:
        i += 1
        if i >= len(recipes):
            i = 0
        steps  -= 1

    return i

def main():
    i = 0
    recipes = [3,7]
    elf1 = 0
    elf2 = 1
    step = 323081
    res = populateRecipes(recipes, elf1, elf2, i, step + 10)[step: step + 10]
    print(res)

if __name__ == "__main__":
    main()