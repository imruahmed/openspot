import mechanicalsoup

browser = mechanicalsoup.Browser()

page = browser.get('http://www.adm.uwaterloo.ca/infocour/CIR/SA/under.html')

form = page.soup.find_all("form")[0]
form.find("option", {"value": "1165"})["selected"] = ""
form.find("option", {"value": "BIOL"})["selected"] = ""
form.find("input", {"name": "cournum"})["value"] = "120"

select_tags = page.soup.find_all("select")
for s in select_tags:
    vals = [option["value"] for option in s.find_all("option")]
    print(vals)
    
sched_response = browser.submit(form, page.url)