import scrapy
import time
import csv

class IPSpider(scrapy.Spider):
    name = "ip"
    start_urls =  [
        "https://ipinfo.io/countries/VN"
    ]

    def parse(self, response):
        nextUrls =  response.css("td.p-3 a::attr(href)").getall()

        with open('data.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Netblock", "Description", "Num IPs"])

        for url in nextUrls:
            if url not in scrawledASN:
                url = response.urljoin(url)
                yield scrapy.Request(url, callback=self.parseASN)
            

    def parseASN(self, response):
        if len(response.css("tbody")) > 0:
            netblocksList = response.css("tbody")[0].css("tr td a::text").getall()
            descriptionsList = response.css("tbody")[0].css("tr td span::text").getall()
            numIPsList = [int(numIP.strip().replace(',','')) for numIP in response.css("tbody")[0].css("tr td:nth-child(3)::text").getall()]

            if len(netblocksList) > 0:
                with open('data.csv', 'a', newline='') as file:
                    writer = csv.writer(file)
                    for idx in range(0, len(netblocksList)):
                        writer.writerow([netblocksList[idx], descriptionsList[idx], numIPsList[idx]])

# Use this variable to partially crawl data.
scrawledASN = [
    # "/AS131126",
    # "/AS131127",
    # "/AS131131",
    # "/AS131342",
    # "/AS131343",
    # "/AS131348",
    # "/AS131350",
    # "/AS131351",
    # "/AS131352",
    # "/AS131353",
    # "/AS131356",
    # "/AS131357",
    # "/AS131359",
    # "/AS131370",
    # "/AS131377",
    # "/AS131396",
    # "/AS131402",
    # "/AS131403",
    # "/AS131404",
    # "/AS131407",
    # "/AS131408",
    # "/AS131412",
    # "/AS131413",
    # "/AS131415",
    # "/AS131417",
    # "/AS131418",
    # "/AS131419",
    # "/AS131421",
    # "/AS131425",
    # "/AS131426",
    # "/AS131430",
    # "/AS131434",
    # "/AS131437",
    # "/AS131439",
    # "/AS135916",
    # "/AS135920",
    # "/AS135937",
    # "/AS135944",
    # "/AS135951",
    # "/AS213370",
    # "/AS24175",
    # "/AS38247",
    # "/AS38732",
    # "/AS38733",
    # "/AS38738",
    # "/AS45552",
    # "/AS45557",
    # "/AS45894",
    # "/AS45896",
    # "/AS45898",
    # "/AS45899",
    # "/AS55313",
    # "/AS55314",
    # "/AS55321",
    # "/AS56143",
    # "/AS56145",
    # "/AS56146",
    # "/AS56150",
    # "/AS56152",
    # "/AS56154",
    # "/AS56156",
    # "/AS63731",
    # "/AS63750"
    # "/AS7552",
    # "/AS38726",
    # "/AS38735",
    # "/AS24085",
    # "/AS131429",
    # "/AS38244",
    # "/AS38731",
    # "/AS135905",
    # "/AS24173",
    # "/AS45903",
    # "/AS7602",
    # "/AS45543",
    # "/AS24086",
    # "/AS18403",
    # "/AS63761",
    # "/AS56147",
    # "/AS45897",
    # "/AS45895",
    # "/AS131384",
    # "/AS45555",
    # "/AS45554",
    # "/AS45550",
    # "/AS45549",
    # "/AS45547",
    # "/AS131393",
    # "/AS45545",
    # "/AS131395",
    # "/AS131399",
    # "/AS131400",
    # "/AS38739",
    # "/AS131406",
    # "/AS63745",
    # "/AS63744",
    # "/AS131411",
    # "/AS131416",
    # "/AS131420",
    # "/AS38729",
    # "/AS131422",
    # "/AS131424",
    # "/AS38250",
    # "/AS131432",
    # "/AS38246",
    # "/AS131436",
    # "/AS38010",
    # "/AS24177",
    # "/AS24176",
    # "/AS131441",
    # "/AS24087",
    # "/AS135901",
    # "/AS135903",
    # "/AS24050",
    # "/AS135906",
    # "/AS23899",
    # "/AS23707",
    # "/AS135907",
    # "/AS201389",
    # "/AS140797",
    # "/AS140796",
    # "/AS140795",
    # "/AS140793",
    # "/AS140792",
    # "/AS140791",
    # "/AS140790",
    # "/AS140789",
    # "/AS140788",
    # "/AS140787",
    # "/AS140786",
    # "/AS140785",
    # "/AS140784",
    # "/AS131392",
    # "/AS63747",
    # "/AS45542",
    # "/AS140766",
    # "/AS135987",
    # "/AS135932",
    # "/AS131386",
    # "/AS131414",
    # "/AS55309",
    # "/AS55322",
    # "/AS135967",
    # "/AS38248",
    # "/AS135918",
    # "/AS45544",
    # "/AS45539",
    # "/AS45538",
    # "/AS135931",
    # "/AS135933",
    # "/AS140782",
    # "/AS140783",
    # "/AS140779",
    # "/AS140780",
    # "/AS140778",
    # "/AS140777",
    # "/AS140776",
    # "/AS140771",
    # "/AS140773",
    # "/AS140774",
    # "/AS140772",
    # "/AS140768",
    # "/AS140767",
    # "/AS140765",
    # "/AS140756",
    # "/AS140763",
    # "/AS140759",
    # "/AS140754",
    # "/AS140760",
    # "/AS140775",
    # "/AS140753",
    # "/AS140752",
    # "/AS140749",
    # "/AS140747",
    # "/AS140743",
    # "/AS140741",
    # "/AS140738",
    # "/AS140737",
    # "/AS135996",
    # "/AS135999",
    # "/AS135995",
    # "/AS135993",
    # "/AS135990",
    # "/AS135989",
    # "/AS135992",
    # "/AS135914",
    # "/AS135983",
    # "/AS135984",
    # "/AS135979",
    # "/AS135976",
    # "/AS135975",
    # "/AS135928",
    # "/AS135968",
    # "/AS135966",
    # "/AS63737",
    # "/AS135965",
    # "/AS135954",
    # "/AS131346",
    # "/AS135930",
    # "/AS56160",
    # "/AS135948",
    # "/AS131125",
    # "/AS135974",
    # "/AS63738",
    # "/AS135910",
    # "/AS135962",
    # "/AS63736",
    # "/AS131123",
    # "/AS131394",
    # "/AS56157",
    # "/AS56144",
    # "/AS131354",
    # "/AS131355",
    # "/AS131433",
    # "/AS56142",
    # "/AS55324",
    # "/AS55323",
    # "/AS55319",
    # "/AS55316",
    # "/AS131369",
    # "/AS55312",
    # "/AS55310",
    # "/AS55307",
    # "/AS131122",
    # "/AS45902",
    # "/AS45901",
    # "/AS24174",
    # "/AS45900",
    # "/AS131440",
    # "/AS45556",
    # "/AS131128",
    # "/AS24035"
    # "/AS7552",
    # "/AS63748",
    # "/AS131363",
    # "/AS131364",
    # "/AS131349",
    # "/AS131427",
    # "/AS131366",
    # "/AS131358",
    # "/AS131360",
    # "/AS131365",
    # "/AS38253",
    # "/AS56141",
    # "/AS56155",
    # "/AS63750",
    # "/AS63760",
    # "/AS45551",
    # "/AS131435",
    # "/AS131423",
    # "/AS131124",
    # "/AS131409",
    # "/AS131130",
    # "/AS135957",
    # "/AS135997",
    # "/AS140758",
    # "/AS63763",
    # "/AS131347",
    # "/AS38734",
    # "/AS63753",
    # "/AS140769",
    # "/AS135947",
    # "/AS140757",
    # "/AS140748",
    # "/AS131129",
    # "/AS131344",
    # "/AS63766",
    # "/AS135994",
    # "/AS135912",
    # "/AS38252",
    # "/AS38251",
    # "/AS135935",
    # "/AS140746",
    # "/AS131376",
    # "/AS131345",
    # "/AS45553",
    # "/AS140764",
    # "/AS38245",
    # "/AS135904",
    # "/AS140742",
    # "/AS140745",
    # "/AS131361",
    # "/AS131387",
    # "/AS45548",
    # "/AS140762",
    # "/AS131362",
    # "/AS55320",
    # "/AS131378",
    # "/AS55317",
    # "/AS55318",
    # "/AS135991",
    # "/AS55315",
    # "/AS140761",
    # "/AS135988",
    # "/AS135986",
    # "/AS135985",
    # "/AS140755",
    # "/AS135998",
    # "/AS135982",
    # "/AS135981",
    # "/AS131382",
    # "/AS135980",
    # "/AS135978",
    # "/AS140740",
    # "/AS135977",
    # "/AS140781",
    # "/AS135973",
    # "/AS135972",
    # "/AS135971",
    # "/AS135970",
    # "/AS140739",
    # "/AS140751",
    # "/AS55311",
    # "/AS140750",
    # "/AS135964",
    # "/AS135969",
    # "/AS140744",
    # "/AS63739",
    # "/AS140770",
    # "/AS63756",
    # "/AS56153",
    # "/AS131405",
    # "/AS63743",
    # "/AS23999",
    # "/AS63768",
    # "/AS63769",
    # "/AS63767",
    # "/AS63764",
    # "/AS63762",
    # "/AS63759",
    # "/AS63757",
    # "/AS63758"
]