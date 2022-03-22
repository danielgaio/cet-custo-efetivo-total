from datetime import datetime, date
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
    lista_datas_pagamentos
):
    # constantes
    VALOR_MAXIMO = 10000
    PRECISAO = 0.000001
    DIAS_NO_ANO = 365

    cet = 0

    while True:
        aproximacao_credito_concedido = 0
        for pagamento_atual in lista_datas_pagamentos:
            dias_entre_concessao_e_pagamento = pagamento_atual - data_liberacao_credito
            print(dias_entre_concessao_e_pagamento)


calcula_cet_anual(
    credito_concedido=1000,
    data_liberacao_credito=date.today(),
    # a periodicidade das parcelas é mensal
    lista_datas_pagamentos=calcula_datas(
        data_primeira_parcela=date(2022, 4, 20),
        qtd_parcelas=5
    )
)
