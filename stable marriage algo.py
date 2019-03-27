def stable_marriage(prefer):
    people_count = len(prefer)
    print("people count",people_count)
    free_men = people_count//2
    couples = [-1 for i in range(people_count)]
    while free_men > 0:
        m = -1
        for i in range(people_count//2):
            if couples[i] == -1:
                m = i
                break

        for w in prefer[m]:
            if couples[w] == -1:
                couples[m] = w
                couples[w] = m
                free_men -= 1
                break
            else:
                for prefer_men in prefer[w]:
                    if prefer_men == m:
                        couples[ couples[w] ] = -1
                        couples[w] = m
                        couples[m] = w
                        break
                    elif prefer_men == couples[w]:
                        break

    for i in range(people_count//2):
        print("men",i,"engaged to",couples[i],"women")


def main():
    prefer = [[7, 5, 6, 4],
                [5, 4, 6, 7],
                [4, 5, 6, 7],
                [4, 5, 6, 7],
                [0, 1, 2, 3],
                [0, 1, 2, 3],
                [0, 1, 2, 3],
                [0, 1, 2, 3]]
    stable_marriage(prefer)


if __name__ == "__main__":
    main()