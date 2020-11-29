def camisa_to_n(text):
    if (s == "XS"):
        return 1
	if (s == "S"):
        return 2
	if (s == "M"):
        return 3
	if (s == "L"):
        return 4
	if (s == "XL"):
        return 5;
	return 6;

def verificar(x):
    if (x==m):
        check=True
        return True
    if check:
        return True
    if disp[tam[x][0]]>0:
        disp[tam[x][0]]-=1
		verificar(x + 1)
		disp[tam[x][0]]+=1
    if (disp[tam[x][1]]>0):
		disp[tam[x][1]]-=1
		verificar(x + 1)
		disp[tam[x][1]]+=1


n_testes=int(input())
disp=[0]*10
tam=[[0]*2]*40
while(n_testes!=0):
    text=input()
    text_list=text.split(" ")
    n=int(text_list[0])
    m=int(text_list[1])
    for i in range(len(disp)):
        disp[i]=n/6
    for i in range(0,m):
        camisas=input()
        camisas_list=camisas.split(" ")
        tam[i][0]=camisa_to_n(camisas_list[0])
        tam[i][1]=camisa_to_n(camisas_list[1])
    check=False
    verificar(0)
    n_tests-=1
