from lxml import html
import requests


def get_line_movements():

    all_games = []
    
    page = requests.get('https://www.thespread.com/mlb-baseball-public-betting-chart')
    tree = html.fromstring(page.content)

    for i in range(1, 30):

        date = tree.xpath('//*[@id="pb"]/div/div['+str(i)+']/div[1]/text()[1]')
        time = tree.xpath('//*[@id="pb"]/div/div['+str(i)+']/div[1]/text()[2]')
        open1 = tree.xpath('//*[@id="pb"]/div/div['+str(i)+']/div[4]/div[1]/text()[1]')
        open2 = tree.xpath('//*[@id="pb"]/div/div['+str(i)+']/div[4]/div[1]/text()[2]')
        current1 = tree.xpath('//*[@id="pb"]/div/div['+str(i)+']/div[4]/div[2]/text()[1]')
        current2 = tree.xpath('//*[@id="pb"]/div/div['+str(i)+']/div[4]/div[2]/text()[2]')
        away_id = tree.xpath('//*[@id="pb"]/div/div['+str(i)+']/div[2]/div[2]/text()[1]')
        home_id = tree.xpath('//*[@id="pb"]/div/div['+str(i)+']/div[2]/div[2]/text()[2]')
        away_pitcher = tree.xpath('//*[@id="pb"]/div/div['+str(i)+']/div[2]/div[2]/span/span[@id="v_pitcher"]/text()')
        away_team = tree.xpath('//*[@id="pb"]/div/div['+str(i)+']/div[2]/div[2]/span[@id="tmv"]/text()')
        home_pitcher = tree.xpath('//*[@id="pb"]/div/div['+str(i)+']/div[2]/div[2]/span/span[@id="h_pitcher"]/text()')
        home_team = tree.xpath('//*[@id="pb"]/div/div['+str(i)+']/div[2]/div[2]/span[@id="tmh"]/text()')

        game_object = (''.join(date), ''.join(time), ''.join(open1), ''.join(current1), ''.join(away_id)[:3].rstrip(), ''.join(away_pitcher), ''.join(away_team)[:3].rstrip(), ''.join(open2), ''.join(current2), ''.join(home_id)[:3].rstrip(), ''.join(home_pitcher), ''.join(home_team)[:3].rstrip())

        all_games.append(game_object)

    return all_games


def get_public():

    public_bets = []

    page = requests.get('https://www.thespread.com/mlb-baseball-public-betting-chart')
    tree = html.fromstring(page.content)

    for i in range(1, 11):
        
        team_id = tree.xpath('//*[@id="Mod11135"]/div/div/div[1]/div['+str(i)+']/span[2]/b/text()')
        team_name = tree.xpath('//*[@id="Mod11135"]/div/div/div[1]/div['+str(i)+']/span[3]/a/text()')
        public_percentage = tree.xpath('//*[@id="Mod11135"]/div/div/div[1]/div['+str(i)+']/span[4]/b/text()')

        public_object = (''.join(team_id).strip(), ''.join(team_name).encode('ascii', 'ignore'), ''.join(public_percentage).strip())

        public_bets.append(public_object)

    return public_bets
