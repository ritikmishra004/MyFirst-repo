# 205. Isomorphic Strings

def isIsomorphic(s, t):
    map_s_t = {}
    map_t_s = {}

    for ch_s, ch_t in zip(s, t):
        if ch_s in map_s_t:
            if map_s_t[ch_s] != ch_t:
                return False
        else:
            map_s_t[ch_s] = ch_t
        
        if ch_t in map_t_s:
            if map_t_s[ch_t] != ch_s:
                return False
        else:
            map_t_s[ch_t] = ch_s

    return True


print(isIsomorphic("egg", "add"))  # Output: True
