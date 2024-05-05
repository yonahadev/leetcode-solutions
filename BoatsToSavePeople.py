    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        frontPointer = 0
        rearPointer = len(people)-1
        boatCount = 0
        while frontPointer <= rearPointer:
            currentTotal = people[frontPointer] + people[rearPointer]
            if currentTotal <= limit:
                frontPointer += 1
            rearPointer -= 1
            boatCount += 1
        return boatCount
