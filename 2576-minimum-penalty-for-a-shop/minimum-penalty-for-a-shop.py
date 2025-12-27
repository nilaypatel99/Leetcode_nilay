class Solution:
    def bestClosingTime(self, customers: str) -> int:
        min_pen=customers.count("Y")
        pen=min_pen
        best_hr=0

        for i in range(len(customers)):
            if customers[i]=="Y":
                pen-=1
            else:
                pen+=1

            if pen<min_pen:
                min_pen=pen
                best_hr=i+1

        return best_hr