if __name__ == "__main__":
    n_ops = int(input())
    states = list()
    s = ""
    for _ in range(n_ops):
        op = input().split(" ")
        op_arg = None
        op_code = int(op[0])
        if op_code != 4:
            op_arg = op[1]
        if op_code == 1:
            states.append(s)
            s = s + op_arg
        elif op_code == 2:
            states.append(s)
            s_size = len(s)
            s = s[0: s_size-int(op_arg)]
        elif op_code == 3:
            print(s[int(op_arg)-1])
        elif op_code == 4:
            s = states.pop()
