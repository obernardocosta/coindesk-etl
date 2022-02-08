import time
import json
import pandas as pd


CSV_PATH = 'coindesk-data-repository/transformed/{}/{}.csv'

def main(path=None):

    ret = {}

    if path is None:
        raise Exception('Parâmetro path não informado.')
     
    with open(path, 'r') as f:
        data = json.load(f)

    columns = ["time_updatedISO","bpi_code","bpi_symbol","bpi_rate","bpi_description","bpi_rate_float"]
    base_df = pd.json_normalize(data)

    columns_map = {
        "USD": {
            "time_updatedISO" : "time.updatedISO",
            "bpi_code": "bpi.USD.code",
            "bpi_symbol": "bpi.USD.symbol",
            "bpi_rate": "bpi.USD.rate",
            "bpi_description": "bpi.USD.description",
            "bpi_rate_float": "bpi.USD.rate_float"
        },
        "GBP": {
            "time_updatedISO" : "time.updatedISO",
            "bpi_code": "bpi.GBP.code",
            "bpi_symbol": "bpi.GBP.symbol",
            "bpi_rate": "bpi.GBP.rate",
            "bpi_description": "bpi.GBP.description",
            "bpi_rate_float": "bpi.GBP.rate_float"
        },
        "EUR": {
            "time_updatedISO" : "time.updatedISO",
            "bpi_code": "bpi.EUR.code",
            "bpi_symbol": "bpi.EUR.symbol",
            "bpi_rate": "bpi.EUR.rate",
            "bpi_description": "bpi.EUR.description",
            "bpi_rate_float": "bpi.EUR.rate_float"
        }
    }
    bpis_code = [{x: None} for x in columns_map.keys()]
    
    def fill_bpi(base_df, bpi_code, columns_map):
        df = pd.DataFrame()
        for k1 in columns_map.keys():
            for k2 in columns_map[k1].keys():
                if k1 == bpi_code:
                    try:
                        df[k2] = base_df[columns_map[k1][k2]]
                    except:
                        print('doest not exists{} '.format(columns_map[k1][k2]) )
                        df = None
                        break
        return df

    ts = int(time.time())
    for i, v in enumerate(bpis_code):
        bpi_code = next(iter(v))
        bpis_code[i][bpi_code] = fill_bpi(base_df, bpi_code, columns_map)
        file_path = CSV_PATH.format(bpi_code, ts)
        
        if bpis_code[i][bpi_code] is not None:
            bpis_code[i][bpi_code].to_csv(file_path, index=False)
            ret['{}_file_path'.format(bpi_code).lower()] = file_path
    
    if len(ret.keys()) != len(bpis_code):
        raise Exception('bpi and files are not the same.')
    return ret


if __name__ == '__main__':
    main()
