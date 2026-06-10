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
            if not st or st[-1] < time:
                print(time)
                st.append(time)
        
        return len(st)