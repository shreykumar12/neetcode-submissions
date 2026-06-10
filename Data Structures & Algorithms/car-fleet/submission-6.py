class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # Create a list of pairs containing [p, s]
        pairs = [(p, s) for p, s in zip(position, speed)]
        # Sort the list of pairs by their position in descending order
        pairs = sorted(pairs, reverse=True)
        # Stack keeps track of how many fleets
        st = []
        print(pairs)
        #Loop through every pair starting at the one closest to finish
        for p, s in pairs:
            # Compute it's time to the target
            time = (target - p) / s
            # If the stack is empty then its the first car (i.e the car closeset to the dest)
            # so we append it to the stack representing the first fleet
            # Otherwise, if the time of the current car is greater than the time at the top 
            # of the stack we know it is not included in a fleet because it is going to reach 
            # after the fleet at the top of the stack.
            # This works because of the pairs being sorted in descending order as if we 
            # encounter a time that's less than or equal to the time at the top of the stack,
            # we know it is a part of that fleet becasue it will catch up
            if not st or st[-1] < time:
                # Add the time representing the fleet to the stack
                st.append(time)
        # At the end the length of the stack will be the # of fleets
        # becasue we only add to the stack when a car will reach after the current fleet at the top
        return len(st)