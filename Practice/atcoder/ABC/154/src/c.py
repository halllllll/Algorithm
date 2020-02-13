n = int(input())
print("YES" if n == len(set(list(map(int, input().split())))) else "NO")
