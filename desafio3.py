#%%
N = int(input())

for i in range(N):
    A, B = list(map(str,input().split()))
    if A[-len(B):] == B:
        print("encaixa")
    else:
        print("nao encaixa")
# %%
