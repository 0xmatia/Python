def chocolate_maker(small, big, x):
    big *= 5;  # 5 cm
    if big + small >= x:
        return True
    return False


print(chocolate_maker(3, 2, 10))
