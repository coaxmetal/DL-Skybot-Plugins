from util import hook, http

@hook.command('beer')
@hook.command
def beeradvocate(inp):
    """ search beeradvocate.com """

    search_url = 'http://beeradvocate.com/search'
    base_url = 'http://beeradvocate.com'

    results = http.get_html(search_url, q=http.quote_plus(inp))
    result = results.xpath("//td[@id='mainContent']/div[2]/ul/li[1]")

    if not result:
        return 'No Results'
    else:
        page_url = base_url + result[0].xpath('a')[0].get('href')
        page = http.get_html(page_url)
        scores = page.cssselect('.BAscore_big')
        return result[0].text_content() + ' || ' + 'Community Score: %s, ' % scores[0].text_content() + 'Bros score: %s' % scores[1].text_content()+ ' | ' + page_url