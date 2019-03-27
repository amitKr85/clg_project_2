# hospital/resident problem
# pref_1 = hospital pref.   pref_2 = resident_pref.


def extended_sma(pref_1, pref_2):
    pairs = list()
    res_partner = dict()
    res_count_in_pref = len(pref_1.keys()) * len(pref_2.keys())

    while res_count_in_pref > 0:

        # for each hospital
        for h, pref in pref_1.items():
            # print("for h=",h)
            # for each resident in pref.
            for r in pref:
                # if already paired with ith hospital
                # print("for r=",r)
                if (h, r) in pairs:
                    # print("already found!")
                    continue
                elif r in res_partner:
                    # print("pair found n breaking")
                    pairs.remove((res_partner[r], r))
                    res_partner.pop(r)
                    res_count_in_pref += 1
                # print("paired",(h,r))
                pairs.append((h, r))
                res_partner[r] = h
                res_count_in_pref -= 1

                # for each successor h_ of h in r's pref. remove h_ and r from each other
                # using index from h+1 to end of r's pref
                # print("h found in r's pref. at ",pref_2[r].index(h),"len of r's pref. is",len(pref_2[r]))
                hpos = pref_2[r].index(h)
                for h_i in range(hpos + 1, len(pref_2[r])):
                    # print("removing h_(s) n r h_=",pref_2[r][hpos+1],"h_i=",h_i,"pref.=",pref_2[r])
                    # removing r from h_'s pref
                    pref_1[pref_2[r][hpos + 1]].remove(r)
                    res_count_in_pref -= 1
                    # removing h_ from r's pref
                    pref_2[r].pop(hpos + 1)

                break

    return pairs
