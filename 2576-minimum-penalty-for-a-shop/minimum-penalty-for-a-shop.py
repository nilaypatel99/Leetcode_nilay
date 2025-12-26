class Solution:
    def bestClosingTime(self, customers: str) -> int:
        pen=customers.count('Y')
        min_pen=pen
        best_hr=0
        n=len(customers)

        for j in range(n):
            if customers[j]=="Y":
                pen-=1  #open and customer so no penalty
            else:
                pen+=1  #open but no customer so penalty

            if pen<min_pen:
                min_pen=pen
                best_hr=j+1

        return best_hr