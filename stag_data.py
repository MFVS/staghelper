import pandas as pd


def get_data(zkratka):
    df = pd.read_csv(f'https://ws.ujep.cz/ws/services/rest2/predmety/getPredmetInfo?zkratka={zkratka}&lang=en&outputFormat=CSV&katedra=KI&rok=2022', sep=';', encoding='cp1250')
    return df
