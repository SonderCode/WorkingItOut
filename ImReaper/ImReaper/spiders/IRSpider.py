import scrapy
from ImReaper.items import ImreaperItem


class ImgurSpider(scrapy.Spider):
    name = "ImReaperSpider"
    allowed_domains = ["imgur.com"]
    start_urls = ["http://imgur.com/"]
    

    def parse(self, response):    	
        hxs = scrapy.selector.HtmlXPathSelector(response)
        ReaperItems = ImreaperItem()

        #Extract Image
        ArrayCollector = []
        _mainImage = hxs.xpath('//img[contains(@src, "imgur")]/@src').extract()

        for image in _mainImage:
        	if 'loaders' not in image:
        		image = image.replace("b.jpg", ".gif")
        		ArrayCollector.append(image)

        ReaperItems['IR_RealURL'] = ArrayCollector

        #Extract Title
        ArrayCollector = []
        _title = hxs.xpath("//div[@class='hover']/p/text()").extract()

        #heh.. tit
        for tit in _title:
        	ArrayCollector.append(tit)

        ReaperItems['IR_Title'] = ArrayCollector
        
        return ReaperItems