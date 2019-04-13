#acho que nao sei ficar importando .txt, separando string, blablabla. mt trabalho e eu realmente nao to conseguindo pensar????
M={
0:'0000010100000000010100100001000000000110',
1:'0000010100000000011000100001000000000111',
2:'0000010100000000011100100001000000001000',
3:'0000010100000000100000100001000000000101',
4:'0000010100000000010100000000000000000110',
5:'0000000000000000000000000000000000000001',
6:'0000000000000000000000000000000000000001',
7:'0000000000000000000000000000000000000001',
8:'0000000000000000000000000000000000000001'}


#[2:] mostrará os caracteres a posição 2 em diante, porque só o bin(0) imprimiria "0b0"

MBR=bin(0)[2:] 
MAR=bin(0)[2:]
IR=bin(0)[2:]
IBR=bin(0)[2:]
PC=0
AC=bin(0)[2:]
MQ=bin(0)[2:]


while IR != '00000000':	
	#significa que a próxima instrução está no MBR

	#Ciclo de busca

	if len(IBR)>1:
		
		IR=IBR[0:7]
		MAR=IBR[8:19]
		PC=PC+1
		IBR=bin(0)[2:] #volta pro IBR 
		
	else: #próxima instrução não está no MBR
		MAR=bin(PC)[2:]
		MBR=M[int(MAR,2)] #base 2
		IR=MBR[0:7]
		MAR=MBR[8:19]
		IBR=MBR[20:39]


	#Decodificar instrucao no IR

	if IR=="00001010":
		#LOAD MQ: transfere o conteúdo de MQ para AC
		AC=MQ

	elif IR=="00001001":
		#LOAD MQ,M(X): transfere o conteúdo do local de memória X para MQ
		MQ=M[int(MAR,2)]

	elif IR=="00100001":
		#STOR M(X): transfere o conteúdo de AC para o local de memória X
		M[int(MAR,2)]=AC.zfill(40)    #zfill é um método q eu descobri q serve para preencher a string à esquerda com zeros
						#isso pq o STOR M(X) substitui o conteúdo do AC para uma alocação de memória X (por assim dizer), fazendo com que o AC fique "zerado"

	elif IR=="00000001":
		#LOAD M(X): transfere M(X) para o AC
		AC=M[int(MAR,2)]

	elif IR=="00000010":
		#LOAD -M(X): transfere o -M(x) para o AC
		AC=-M[int(MAR,2)]

	elif IR=="00000011":
		#LOAD |M(X)|: transfere o valor absoluto de M(X) para o AC
		AC=abs(M[int(MAR,2)])

	elif IR=="00000100":
		#LOAD -|M(X)|: transfere -|M(X)| para o acumulador AC
		AC=-abs(M[int(MAR,2)])

	elif IR=="00001101":
		#JUMP M(X, 0:19): apanha a próxima instrução da metade esquerda de M(X)
		AUX=M[int(MAR,2)]
		IBR=AUX[0:19]

	elif IR=="00001110":
		#JUMP M(X, 20:39): apanha a próxima instrução da metade direita de M(X)
		AUX=M[int(MAR,2)]
		IBR=AUX[20:39]

	elif IR=="00001111":
		#JUMP + M(X, 0:19): se o número AC for não negativo,apanha a próxima instruçãoda metade esquerda de M(X)
		if AC>=0:
			AUX=M[int(MAR,2)]
			IBR=AUX[0:19]

	elif IR=="00010000":
		#JUMP + M(X, 20:39): se o número no AC for não negativo, apanha a próxima instrução da metade direita de M(X)
		if AC>=0:
			AUX=M[int(MAR,2)]
			IBR=AUX[20:39]

	elif IR=="00000101":
		#ADD M(X): soma M(X) a AC e coloca o resultado em AC
		AC=bin(int(AC,2)+int(M[int(MAR,2)],2))[2:]
	
	elif IR=="00000111":
		#ADD |M(X)|: soma o valor absoluto de M(X) a AC e coloca o resultado em AC
		AC=bin(int(AC,2)+abs(int(M[int(MAR,2)],2)))[2:]

	elif IR=="00000110":
		#SUB M(X): subtrai M(X) de AC e coloca o resultado em AC
		AC=bin(int(AC,2)-int(M[int(MAR,2)],2))[2:]

	elif IR=="00001000":
		#SUB |M(X)|: subtrai o valor absoluto de M(X)de AC e coloca o resultado em AC
		AC=bin(int(AC,2)-abs(int(M[int(MAR,2)],2)))[2:]

	elif IR=="00001011":
		#MUL M(X) eu nao sei como fazer bjs mas vou tentar bjs
		#MUL M(X): multiplica M(X) por MQ; coloca os bits mais significativos em AC, e os menos significativos em MQ
		resultado = bin(int(MQ,2)*int(M[int(MAR,2)],2))[2:]  #resultado vai ter tamanho de 80 bits, eu acho. se nao for, to fazendo errado msm bjs
		AC = bin(resultado[40:80])   #os últimos dígitos são os mais significativos, de acordo com minha lógica q pode estar falha bjs
		MQ = bin(resultado[0:39])

	elif IR=="00001100":
		#DIV M(X) eu tbm nao sei como fazer bjs mas vou tentar bjs se tiver errado melhor q nada ne nao mores
		#DIV M(X): divide AC por M(X), coloca o quociente em MQ e o resto em AC
		#tamanho nao altera com a divisao, so com a multiplicacao, entao vai continuar 40 bits
		quociente = bin(int(AC,2)/(int(M[int(MAR,2)],2)))[2:] 
		MQ = quociente
		AC = bin(int(AC,2)%(int(M[int(MAR,2)],2)))[2:]
    #AC = resto 

	elif IR=="00010100":
		#LSH: multiplica AC por 2, ou seja, desloca à esquerda uma posição de bit
		AC=bin(2*int(AC,2))[2:]

	elif IR=="00010101":
		#RSH:divide o AC por 2, ou seja, desloca uma posição à direita
		AC=bin(1/2*int(AC,2))[2:]

	elif IR=="00010010":
		# STOR M(X, 8:19): substitui campo de endereço da esquerda em M(X) por 12 bits mais à direita de AC
		#n sei mt bem como fazer???? kkkk bjs
		auxiliar = bin(int(M[int(MAR,2)],2))[2:]
		auxiliar = auxiliar[20:39]
		auxiliar2= bin(int(AC,2))[2:]
		auxiliar2 = auxiliar2[0:19]
		auxiliar = auxiliar2

	elif IR=="00010011":
		#STOR M(X, 28:29): substitui campo de endereço da direita em M(X) por 12 bits mais à direita de AC
		#esse aqui eh de alguma forma pior????? hmmm kkkk bjs
		auxiliar1 = bin(int(M[int(MAR,2)],2))[2:]
		auxiliar1 = auxiliar1[0:19]
		auxiliar2 = bin(int(AC,2))[2:]
		auxiliar2 = auxiliar2[0:19]
		auxiliar1 = auxiliar2

	
for key, value in M.items():
	print(key, value)
