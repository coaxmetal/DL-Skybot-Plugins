from util import hook, http

@hook.command('beer')
@hook.command
def beeradvocate(inp):
    """ search beeradvocate.com """

    search_url = 'http://beeradvocate.com/search'
    base_url = 'http://beeradvocate.com/'

    results = http.get_html(search_url, q=http.quote_plus(inp))
    result = results.xpath("//td[@id='mainContent']/div[2]/ul/li[1]")

    if not result:
        return 'No Results'
    else:
        page_url = base_url + results[0].get('href')
        page = http.get_html(page)
        community_score = page.xpath("//td[@id='mainContent']/table[1]/tbody/tr[1]/td[1]/table/tbody/tr/td[1]/span[@class='BAscore_big']")
        bros_score = page.xpath("//td[@id='mainContent']/table[1]/tbody/tr[1]/td[1]/table/tbody/tr/td[2]/span[@class='BAscore_big']")
        return results[0].text_content() + ' || ' + 'Community Score: %s, ' % community_score.text_content() + 'Bros score: %s' % bros_score + ' | ' + page_url