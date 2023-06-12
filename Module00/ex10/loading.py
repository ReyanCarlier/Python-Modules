def ft_progress(lst):
    for i in range(len(lst)):
        progress = "="
        percent = i / len(lst) * 100
        for n in range(int(percent)):
            if (n % 5 == 0 and n > 0):
                progress += "="
        progress += ">"
        print("\033[F[{:3d}%] [{}] {}/{}".format(int(percent) + 1, progress.ljust(20), i + 1, len(lst)))
        yield lst[i]

# import time
# def main():
# 	listy = range(1000)
# 	ret = 0
# 	for elem in ft_progress(listy):
# 		ret += (elem + 3) % 5
# 		time.sleep(0.01)
# 	print()
# 	print(ret)

# if (__name__ == "__main__"):
#     main()