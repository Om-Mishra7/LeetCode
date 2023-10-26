def strStr(haystack, needle):
    if haystack == needle:
        return 0

    len_haystack = len(haystack)
    len_needle = len(needle)

    if len_haystack < len_needle:
        return -1

    for i in range(0, (len_haystack-len_needle) + 1):
        if haystack[i] == needle[0]:
            for j in range(1, len_needle):
                if needle[j] != haystack[i+j]:
                    break
                if j == len_needle - 1:
                    return i
            if len_needle == 1:
                return i
    return -1


haystack = "mississippi"
needle = "issip"

print(strStr(haystack, needle))
