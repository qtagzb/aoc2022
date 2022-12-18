# [W] [V]     [P]                    
# [B] [T]     [C] [B]     [G]        
# [G] [S]     [V] [H] [N] [T]        
# [Z] [B] [W] [J] [D] [M] [S]        
# [R] [C] [N] [N] [F] [W] [C]     [W]
# [D] [F] [S] [M] [L] [T] [L] [Z] [Z]
# [C] [W] [B] [G] [S] [V] [F] [D] [N]
# [V] [G] [C] [Q] [T] [J] [P] [B] [M]
#  1   2   3   4   5   6   7   8   9 

# crate1 = ["V", "C", "D", "R", "Z", "G", "B", "W"]
# crate2 = ["G", "W", "F", "C", "B", "S", "T", "V"]
# crate3 = ["C", "B", "S", "N", "W"]
# crate4 = ["Q", "G", "M", "N", "J", "V", "C", "P"]
# crate5 = ["T", "S", "L", "F", "D", "H", "B"]
# crate6 = ["J", "V", "T", "W", "M", "N"]
# crate7 = ["P", "F", "L", "C", "S", "T", "G"]
# crate8 = ["B", "D", "Z"]
# crate9 = ["M", "N", "Z", "W"]

crates = [["V", "C", "D", "R", "Z", "G", "B", "W"], ["G", "W", "F", "C", "B", "S", "T", "V"], ["C", "B", "S", "N", "W"], ["Q", "G", "M", "N", "J", "V", "C", "P"], ["T", "S", "L", "F", "D", "H", "B"], ["J", "V", "T", "W", "M", "N"], ["P", "F", "L", "C", "S", "T", "G"], ["B", "D", "Z"], ["M", "N", "Z", "W"]]

with open("input.txt", 'r') as data:
    for i in data:
        move_count = int(i.split(" ")[1])
        from_crate = int(i.split(" ")[3]) - 1
        to_crate = int(i.split(" ")[5]) - 1

        crate_holder = []
        for i in range(move_count):
            crate_holder.append(crates[from_crate][-1])
            crates[from_crate].pop(-1)

        crate_holder.reverse()

        for i in crate_holder:
            crates[to_crate].append(i)
            
    for i in crates:
        print(i[-1])