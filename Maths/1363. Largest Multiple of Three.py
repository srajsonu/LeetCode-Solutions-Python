class Solution:
    def largestMultipleOfThree(self, A):
        A = sorted(A, reverse=True)

        one = [i for i in A if i % 3 == 1]
        two = [i for i in A if i % 3 == 2]

        sm = sum(A)

        if sm % 3 == 1:
            if one:
                A.remove(one[-1])
            else:
                A.remove(two[-1])
                A.remove(two[-2])

        if sm % 3 == 2:
            if two:
                A.remove(two[-1])
            else:
                A.remove(one[-1])
                A.remove(one[-2])

        return str(int("".join([str(i) for i in A]))) if A else ""
