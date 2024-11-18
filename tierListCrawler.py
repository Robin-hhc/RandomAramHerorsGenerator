import requests
from bs4 import BeautifulSoup


def fetch_opgg_aram_tier_list():
    url = "https://www.op.gg/modes/aram/"
    # Change the "zh-CN" to "en-US" or any language you want for getting result in different language.
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
        "Accept-Language": "zh-CN"
    }
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        print(f"Failed to fetch page, status code: {response.status_code}")
        return

    soup = BeautifulSoup(response.text, "html.parser")
    tier_list = []
    rows = soup.find("table", class_="css-1cwphh3 ez7snl10").find("tbody").find_all("tr") # find table
    for row in rows:
        hero_name = row.find_all("td")[1].find("a").find("strong").text.strip()
        tier_level = row.find_all("td")[2].text.strip()
        win_rate = row.find_all("td")[3].text.strip()
        tier_list.append([hero_name, tier_level, win_rate])
    return tier_list


if __name__ == "__main__":
    tier_list = fetch_opgg_aram_tier_list()
    filename = "heros.txt"
    with open(filename, 'w', encoding='utf-8') as file:
        for line in tier_list:
            file.write(line[0] + ", " + line[1] + ", " + line[2] + "\n")
