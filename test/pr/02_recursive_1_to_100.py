def accu1_to_100(cnt, accu):
    if cnt <= 100:
        return accu1_to_100(cnt + 1, accu + cnt)
    else:
        return accu

print(accu1_to_100(0, 0))
