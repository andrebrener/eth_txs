import os

from datetime import datetime

import requests
import pandas as pd

from bs4 import BeautifulSoup
from constants import DATA_DIR, MAX_PAGE_NUMBER


def get_page_data(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    row_dict = {}

    for tr in soup.find_all("tr")[1:]:
        vals = []
        for tag in tr.find_all("span", {"class": "address-tag"}):
            for t in tag.find_all("a"):
                link = t['href']
                first_val = link.index('0')
                vals.append(link[first_val:])

        dates = [
            tag['title'] for tag in tr.find_all("span", {
                "rel": "tooltip"
            })
        ]

        contract = [0]
        if len(tr.find_all("i", {"class": "fa fa-file-text-o"})):
            contract = [1]

        other_vals = []
        for n, t in enumerate(tr):
            if n < 5:
                continue
            other_vals.append(t.text)

        if not len(vals):
            continue

        if len(vals) == 2:
            vals.append('')

        row_dict[vals[0]] = [vals[1], vals[2]] + dates + other_vals + contract

    df = pd.DataFrame(row_dict).T.reset_index()

    if len(df.columns) != 8:
        return None

    df.columns = [
        'tx_hash', 'from_address', 'to_address', 'date', 'receiver', 'value',
        'tx_fee', 'contract'
    ]

    df['date'] = pd.to_datetime(df['date'])
    df['value'] = df['value'].apply(lambda x: x.split()[0])

    return df


def get_txs():
    dfs = []
    for i in range(MAX_PAGE_NUMBER):
        page_number = i + 1
        # print(page_number)
        url = 'https://etherscan.io/txs?p={}'.format(page_number)
        page_data = get_page_data(url)
        if page_data:
            dfs.append(page_data)

    final_df = pd.concat(dfs)

    return final_df


def main():
    start_time = datetime.today()
    df = get_txs()
    str_st = start_time.strftime('%Y_%m_%d_%H_%M')
    os.makedirs(DATA_DIR, exist_ok=True)
    file_name = '{}.csv'.format(str_st)
    full_path = os.path.join(DATA_DIR, file_name)
    df.to_csv(full_path, index=False)
    end_time = datetime.today()

    # print("The script was {} long".format(end_time - start_time))


if __name__ == '__main__':

    df = main()

    import pdb; pdb.set_trace()  # noqa # yapf: disable
