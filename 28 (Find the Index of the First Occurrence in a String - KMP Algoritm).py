def strStr(haystack, needle):

    # Preprocessing for LPS

    lps = [0] * len(needle)

    previous_lps_pointer, current_lps_pointer = 0, 1

    while current_lps_pointer < len(needle):
        if needle[current_lps_pointer] == needle[previous_lps_pointer]:
            lps[current_lps_pointer] = previous_lps_pointer + 1
            previous_lps_pointer += 1
            current_lps_pointer += 1
        elif lps[previous_lps_pointer] == 0:
            lps[current_lps_pointer] = 0
            current_lps_pointer += 1
        else:
            previous_lps_pointer = lps[previous_lps_pointer - 1]


    # Searching the haystack for the needle

    needle_pointer, haystack_pointer  = 0, 0    

    while haystack_pointer < len(haystack):
        if haystack[haystack_pointer] == needle[needle_pointer]:
            haystack_pointer += 1
            needle_pointer += 1
        else:
            if needle_pointer == 0:
                haystack_pointer += 1
            else:
                needle_pointer = lps[needle_pointer-1]
        if needle_pointer == len(needle):
            return haystack_pointer - len(needle)
    
    return -1
    


haystack = "mississippi"
needle = "issip"

print(strStr(haystack, needle))
