from datetime import date
from dateutil.relativedelta import relativedelta


def calcula_datas(data_primeira_parcela, qtd_parcelas):
    vetor_parcelas = []

    for i in range(qtd_parcelas):
        if i == 0:
            vetor_parcelas.append(data_primeira_parcela)
        else:
            vetor_parcelas.append(
                vetor_parcelas[i-1] + relativedelta(months=+1))

    return vetor_parcelas


def calcula_cet_anual(
    credito_concedido,
    data_liberacao_credito,
    lista_datas_pagamentos,
    valor_parcela
):
    VALOR_MAXIMO = 10000
    PRECISAO = 0.000001
    DIAS_NO_ANO = 365
    cet = 0

    while True:
        aproximacao_credito_concedido = 0
        for pagamento_atual in lista_datas_pagamentos:
            dias_entre_concessao_e_pagamento = pagamento_atual - data_liberacao_credito
            if dias_entre_concessao_e_pagamento.days < 0:
                print('Erro: Data de pagamento anterior a data de concessão do crédito.')
            aproximacao_credito_concedido += valor_parcela / \
                (1+cet)**(dias_entre_concessao_e_pagamento.days/DIAS_NO_ANO)

        cet += PRECISAO
        if cet >= VALOR_MAXIMO:
            print('Erro: CET ultrapassou limite máximo, impossível realizar cálculo.')
            return -1

        if aproximacao_credito_concedido-credito_concedido <= 0:
            break

        cet *= aproximacao_credito_concedido / credito_concedido

    return cet * 100


cet_anual = calcula_cet_anual(
    credito_concedido=200000,
    data_liberacao_credito=date.today(),
    # a periodicidade das parcelas é mensal
    lista_datas_pagamentos=calcula_datas(
        data_primeira_parcela=date(2022, 4, 20),
        qtd_parcelas=60
    ),
    valor_parcela=5750
)

print(cet_anual)
