


def getMaximumCategoryMaxCount(categories):
    # Write your code here
    d = {}
    m = {}
    for c in categories:
        if c not in d:
            d[c] = 1
        else: 
            d[c] += 1
        
        max_c = -1
        keys = []
        for k, v in d.items():
            if v > max_c:
                max_c = v
                keys = [k]
            if v == max_c:
                keys.append(k)


        keys = list(set(keys))

        for key in keys:
            if key not in m: m[key] = 1
            else: m[key] += 1
                
    return max(m.values())


if __name__ == '__main__':

    s = "adbcbcbcc"
    categories = s

    result = getMaximumCategoryMaxCount(categories)
    print(result)


