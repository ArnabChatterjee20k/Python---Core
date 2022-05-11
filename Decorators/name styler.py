def person_lister(f):
    def inner(people):
        # complete the function
        length = len(people)
        for i in range(length):
            for j in range(length-i-1):
                if people[j][2] > people[j + 1][2] :
                    people[j], people[j + 1] = people[j + 1], people[j]
        for i in people:
            yield f(i)
        
    return inner

@person_lister
def name_format(person):
    return ("Mr. " if person[3] == "M" else "Ms. ") + person[0] + " " + person[1]

if __name__ == '__main__':
    people = [input().split() for i in range(int(input()))]
    print(*name_format(people), sep='\n')
