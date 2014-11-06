import scrapy


class ImreaperItem(scrapy.Item):
    # define the fields for your item here like:
	IR_Title = scrapy.Field()
	#IR_TopComment = scrapy.Field()
	IR_RealURL = scrapy.Field()
