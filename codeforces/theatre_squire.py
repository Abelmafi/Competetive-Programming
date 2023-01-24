    import math
     
    if __name__ == '__main__':
        input_list = list(map(int, input().split(' ')))
        length = input_list[0]
        width = input_list[1]
        a = input_list[2]
        result = math.ceil(length / a) * math.ceil(width / a)
        print(result)
