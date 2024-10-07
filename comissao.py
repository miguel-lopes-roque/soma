#coding, utf8

def comissaoSalario():
    nome = input(" Entre com o nome do vendedor: ")
    SalarioFixo = float(input("informe o salario: "))
    Vendas = float(input("informe total de vendas: "))
    Comissao = 0.15*Vendas
    pagamentoEsperado=SalarioFixo+Comissao
    return nome, Comissao, pagamentoEsperado


if __name__=="__main__":
    nome, Comissao, Vendas, pagamentoEsperado = comissaoSalario()     
    strg = "{0} obteve R$ {1:.2f} de comissao e vai receber{2:.2f}".format(nome, Comissao, pagamentoEsperado)
    print(strg)