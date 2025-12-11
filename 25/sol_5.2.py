import sys

class Ranges:
    def __init__(self):
        self.ranges: list[(int, int)] = []

    def add(self, new_r):
        changed = 0
        for i in range(len(self.ranges)):
            match (new_r[1] < self.ranges[i][0] - 1, 
                   new_r[0] > self.ranges[i][1] + 1, 
                   new_r[0] <= self.ranges[i][0], 
                   new_r[1] <= self.ranges[i][1]):
                # le nouveau range est plus grand en avant et a la fin
                case (False, False, True, False):
                    self.ranges[i] = new_r
                    changed = i
                    break
                # on concatene le nouveau range en avant
                case (False, False, True, True):
                    self.ranges[i] = (new_r[0], self.ranges[i][1])
                    changed = i
                    break
                # on concatene le nouveau range a la fin
                case (False, False, False, False):
                    self.ranges[i] = (self.ranges[i][0], new_r[1])
                    changed = i
                    break
                # la nouveau range est deja contenu dans un range
                case (False, False, False, True):
                    return
                case _:
                    continue
        else:
            self.ranges.append(new_r)
            return
        
        r = self.ranges.pop(changed)
        self.add(r)
                
    def get_total_ranges_item(self):
        res = 0
        for r in self.ranges:
            res += (r[1] - r[0] + 1)
        return res

with open(sys.argv[1], 'r') as f:
    lines = f.readlines()

i = lines.index('\n')
ranges = [
    (int(r.strip().split('-')[0]), int(r.strip().split('-')[1])) 
    for r in lines[:i]
]

considered_fresh = Ranges()

for r in ranges:
    considered_fresh.add(r)

print(considered_fresh.get_total_ranges_item())
