from django.conf import settings


from linebot.models import TextSendMessage, ImageSendMessage, StickerSendMessage, LocationSendMessage, QuickReply, QuickReplyButton, MessageAction
from linebot.models import TemplateSendMessage,ConfirmTemplate, MessageTemplateAction, ButtonsTemplate, PostbackTemplateAction, URITemplateAction, CarouselTemplate, CarouselColumn, ImageCarouselTemplate, ImageCarouselColumn
from linebot.models import ImagemapSendMessage, BaseSize, MessageImagemapAction, URIImagemapAction, ImagemapArea, TemplateSendMessage, ButtonsTemplate, DatetimePickerTemplateAction
from linebot.models import TextSendMessage, AudioSendMessage, VideoSendMessage
from linebot.models import BubbleContainer, ImageComponent, BoxComponent, TextComponent, IconComponent, ButtonComponent, SeparatorComponent, FlexSendMessage, URIAction
from linebot.models import TextSendMessage, ImageSendMessage, LocationSendMessage, TemplateSendMessage,ButtonsTemplate, URITemplateAction, ConfirmTemplate, PostbackTemplateAction
from linebot import LineBotApi, WebhookParser
from hotelapi.models import booking
from hotelapi.models import users
from studentsapp.models import student
from flask import request
import datetime
line_bot_api = LineBotApi(settings.LINE_CHANNEL_ACCESS_TOKEN)
parser = WebhookParser(settings.LINE_CHANNEL_SECRET)
def sendText(event):  #傳送文字
    try:
        message = TextSendMessage(  
            text = "我是 Linebot，\n您好！"
        )
        line_bot_api.reply_message(event.reply_token,message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))

def sendImage(event):  #傳送圖片
    try:
        message = ImageSendMessage(
            original_content_url = "https://i.imgur.com/4QfKuz1.png",
            preview_image_url = "https://i.imgur.com/4QfKuz1.png"
        )
        line_bot_api.reply_message(event.reply_token,message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))

def sendStick(event):  #傳送貼圖
    try:
        message = StickerSendMessage(  #貼圖兩個id需查表
            package_id='1',  
            sticker_id='2'
        )
        line_bot_api.reply_message(event.reply_token, message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))

def sendMulti(event):  #多項傳送
    try:
        message = [  #串列
            StickerSendMessage(  #傳送貼圖
                package_id='1',  
                sticker_id='2'
            ),
            TextSendMessage(  #傳送y文字
                text = "這是 Pizza 圖片！"
            ),
            ImageSendMessage(  #傳送圖片
                original_content_url = "https://i.imgur.com/4QfKuz1.png",
                preview_image_url = "https://i.imgur.com/4QfKuz1.png"
            )
        ]
        line_bot_api.reply_message(event.reply_token,message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))

def sendPosition(event):  #傳送位置
    try:
        message = LocationSendMessage(
            title='101大樓',
            address='台北市信義路五段7號',
            latitude=25.034207,  #緯度
            longitude=121.564590  #經度
        )
        line_bot_api.reply_message(event.reply_token, message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))

                 
def sendQuickreply(event):  #快速選單
    try:
        message = TextSendMessage(
            text='請選擇下列資訊',
            quick_reply=QuickReply(
                items=[
                    QuickReplyButton(
                        action=MessageAction(label="旅遊數據分析", text="旅遊數據分析")
                    ),
                    QuickReplyButton(
                        action=MessageAction(label="景點查詢", text="景點查詢")
                    ),
                    QuickReplyButton(
                        action=MessageAction(label="交通", text="交通一點通")
                    ),
                    QuickReplyButton(
                        action=MessageAction(label="即時報", text="旅遊即時報")
                    ),
	            QuickReplyButton(
                        action=MessageAction(label="天氣", text="天氣小幫手")
                    ),
		   QuickReplyButton(
                        action=MessageAction(label="調查", text="2020旅遊調查")
                    ),
		   QuickReplyButton(
                        action=MessageAction(label="警廣", text="聯絡警廣")
                    ),
		    QuickReplyButton(
                        action=MessageAction(label="播報事故路況", text="播報警廣事故路況")
                    ),
			
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token,message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))
def sendButton(event):  #按鈕樣版
    try:
        message = TemplateSendMessage(
            alt_text='按鈕樣板',
            template=ButtonsTemplate(
                    thumbnail_image_url  ='https://i.imgur.com/ZGaXkKd.jpg' ,
                    title  =  'demo' ,
                    text  =  'pizza demo' ,
            actions=[
                    MessageTemplateAction(  #顯示文字計息
                        label='文字訊息',
                        text='@購買披薩'
                    ),
                    URITemplateAction(  #開啟網頁
                        label  =  'website mcu' ,
                        uri  =  'https://web.mcu.edu.tw/'
                    ),
                    PostbackTemplateAction(  #執行Postback功能,觸發Postback事件
                        label='回傳訊息',  #按鈕文字
                        #text='@購買披薩',  #顯示文字計息
                        data='action=buy'  #Postback資料
                    ),
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))

def sendConfirm(event):  #確認樣板
    try:
        message = TemplateSendMessage(
            alt_text='確認樣板',
            template=ConfirmTemplate(
                text='你確定要購買這項商品嗎？',
                actions=[
                    MessageTemplateAction(  #按鈕選項
                        label='是',
                        text='@yes'
                    ),
                    MessageTemplateAction(
                        label='否',
                        text='@no'
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))

def sendCarousel(event):  #轉盤樣板
    try:
        message = TemplateSendMessage(
            alt_text='轉盤樣板',
            template=CarouselTemplate(
                columns=[
                    CarouselColumn(
                        thumbnail_image_url='https://i.imgur.com/4QfKuz1.png',
                        title='這是樣板一',
                        text='第一個轉盤樣板',
                        actions=[
                            MessageTemplateAction(
                                label='文字訊息一',
                                text='賣披薩'
                            ),
                            URITemplateAction(
                                label='連結文淵閣網頁',
                                uri='http://www.e-happy.com.tw'
                            ),
                            PostbackTemplateAction(
                                label='回傳訊息一',
                                data='action=sell&item=披薩'
                            ),
                        ]
                    ),
                    CarouselColumn(
                        thumbnail_image_url='https://i.imgur.com/qaAdBkR.png',
                        title='這是樣板二',
                        text='第二個轉盤樣板',
                        actions=[
                            MessageTemplateAction(
                                label='文字訊息二',
                                text='賣飲料'
                            ),
                            URITemplateAction(
                                label='連結台大網頁',
                                uri='http://www.ntu.edu.tw'
                            ),
                            PostbackTemplateAction(
                                label='回傳訊息二',
                                data='action=sell&item=飲料'
                            ),
                        ]
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token,message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))

def sendImgCarousel(event):  #圖片轉盤
    try:
        message = TemplateSendMessage(
            alt_text='圖片轉盤樣板',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://i.imgur.com/4QfKuz1.png',
                        action=MessageTemplateAction(
                            label='文字訊息',
                            text='賣披薩'
                        )
                    ),
                    ImageCarouselColumn(
                        image_url='https://i.imgur.com/qaAdBkR.png',
                        action=PostbackTemplateAction(
                            label='回傳訊息',
                            data='action=sell&item=飲料'
                        )
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token,message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))

def sendPizza(event):
    try:
        message = TextSendMessage(
            text = '感謝您購買披薩，我們將盡快為您製作。'
        )
        line_bot_api.reply_message(event.reply_token, message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))

def sendYes(event):
    try:
        message = TextSendMessage(
            text='感謝您的購買，\n我們將盡快寄出商品。',
        )
        line_bot_api.reply_message(event.reply_token, message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))

def sendBack_buy(event, backdata):  #處理Postback
    try:
        text1 = '感謝您購買披薩，我們將盡快為您製作。\n(action 的值為 ' + backdata.get('action') + ')'
        text1 += '\n(可將處理程式寫在此處。)'
        message = TextSendMessage(  #傳送文字
            text = text1
        )
        line_bot_api.reply_message(event.reply_token, message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))

def sendBack_sell(event, backdata):  #處理Postback
    try:
        message = TextSendMessage(  #傳送文字
            text = '點選的是賣 ' + backdata.get('item')
        )
        line_bot_api.reply_message(event.reply_token, message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))


def sendImgmap(event):  #圖片地圖
    try:
        image_url = 'https://i.imgur.com/Yz2yzve.jpg'  #圖片位址
        imgwidth = 1040  #原始圖片寛度一定要1040
        imgheight = 300
        message = ImagemapSendMessage(
            base_url=image_url,
            alt_text="圖片地圖範例",
            base_size=BaseSize(height=imgheight, width=imgwidth),  #圖片寬及高
            actions=[
                MessageImagemapAction(  #顯示文字訊息
                    text='你點選了紅色區塊！',
                    area=ImagemapArea(  #設定圖片範圍:左方1/4區域
                        x=0, 
                        y=0, 
                        width=imgwidth*0.25, 
                        height=imgheight  
                    )
                ),
                URIImagemapAction(  #開啟網頁
                    link_uri='http://www.e-happy.com.tw',
                    area=ImagemapArea(  #右方1/4區域(藍色1)
                        x=imgwidth*0.75, 
                        y=0, 
                        width=imgwidth*0.25, 
                        height=imgheight  
                    )
                ),
            ]
        )
        line_bot_api.reply_message(event.reply_token, message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))

def sendDatetime(event):  #日期時間
    try:
        message = TemplateSendMessage(
            alt_text='日期時間範例',
            template=ButtonsTemplate(
                thumbnail_image_url='https://i.imgur.com/VxVB46z.jpg',
                title='日期時間示範',
                text='請選擇：',
                actions=[
                    DatetimePickerTemplateAction(
                        label="選取日期",
                        data="action=sell&mode=date",  #觸發postback事件
                        mode="date",  #選取日期
                        initial="2019-06-01",  #顯示初始日期
                        min="2019-01-01",  #最小日期
                        max="2020-12-31"  #最大日期
                    ),
                    DatetimePickerTemplateAction(
                        label="選取時間",
                        data="action=sell&mode=time",
                        mode="time",  #選取時間
                        initial="10:00",
                        min="00:00",
                        max="23:59"
                    ),
                    DatetimePickerTemplateAction(
                        label="選取日期時間",
                        data="action=sell&mode=datetime",
                        mode="datetime",  #選取日期時間
                        initial="2019-06-01T10:00",
                        min="2019-01-01T00:00",
                        max="2020-12-31T23:59"
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token,message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))

def sendData_sell(event, backdata):  #Postback,顯示日期時間
    try:
        if backdata.get('mode') == 'date':
            dt = '日期為：' + event.postback.params.get('date')  #讀取日期
        elif backdata.get('mode') == 'time':
            dt = '時間為：' + event.postback.params.get('time')  #讀取時間
        elif backdata.get('mode') == 'datetime':
            dt = datetime.datetime.strptime(event.postback.params.get('datetime'), '%Y-%m-%dT%H:%M')  #讀取日期時間
            dt = dt.strftime('{d}%Y-%m-%d, {t}%H:%M').format(d='日期為：', t='時間為：')  #轉為字串
        message = TextSendMessage(
            text=dt
        )
        line_bot_api.reply_message(event.reply_token,message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))


def sendButtonp(event):  #按鈕樣版
	    try:
	        message = TemplateSendMessage(
	            alt_text='按鈕樣板',
	            template=ButtonsTemplate(
	                thumbnail_image_url='https://img.onl/TtmP9C',  #顯示的圖片           
	                text='                旅遊小幫手',  #副標題
	                actions=[	                   
                        URITemplateAction(  #開啟網頁
	                        label='旅遊數據分析結果',
	                        uri='https://liff.line.me/1655387687-k6LB7JY4'
	                    ),	                    
	                ]
	            )
	        )
	        line_bot_api.reply_message(event.reply_token, message)
	    except:
	        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))
            
def sendButtonq(event):  #按鈕樣版
	    try:
	        message = TemplateSendMessage(
	            alt_text='按鈕樣板',
	            template=ButtonsTemplate(
	                thumbnail_image_url='https://i.imgur.com/uIcCV9Y.jpg',  #顯示的圖片           
	                text='              旅遊景點查詢',  #副標題
	                actions=[	                   
                        URITemplateAction(  #開啟網頁
	                        label='點擊查詢',
	                        uri='https://liff.line.me/1655387687-e6wpr36Y'
	                    ),	                    
	                ]
	            )
	        )
	        line_bot_api.reply_message(event.reply_token, message)
	    except:
	        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))
          
def sendButtonr(event):  #按鈕樣版
	    try:
	        message = TemplateSendMessage(
	            alt_text='按鈕樣板',
	            template=ButtonsTemplate(
	                thumbnail_image_url='https://img.onl/WsoLrl',  #顯示的圖片           
	                text='              交通查詢系統',  #副標題
	                actions=[	                   
                        URITemplateAction(  #開啟網頁
	                        label='查詢交通',
	                        uri='https://liff.line.me/1655387687-qvYLKnGM'
	                    ),
                        URITemplateAction(  #開啟網頁
	                        label='了解訂票資訊',
	                        uri='https://liff.line.me/1655387687-V6n5eP2y'
	                    ),	                    
                  ]
	            )
	        )
	        line_bot_api.reply_message(event.reply_token, message)
	    except:
	        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))

def sendButtons(event):  #按鈕樣版
	    try:
	        message = TemplateSendMessage(
	            alt_text='按鈕樣板',
	            template=ButtonsTemplate(
	                thumbnail_image_url='https://i.imgur.com/llADffI.jpg',  #顯示的圖片           
	                text='               旅遊即時報',  #副標題
	                actions=[	                   
                        URITemplateAction(  #開啟網頁
	                        label='疫情地圖',
	                        uri='https://liff.line.me/1655387687-pqOrQzNZ'
	                    ),
                        URITemplateAction(  #開啟網頁
	                        label='國道交通狀況',
	                        uri='https://liff.line.me/1655387687-W64Q2rmV'
	                    ),	                    
                  ]
	            )
	        )
                    
	        line_bot_api.reply_message(event.reply_token, message)
	    except:
	        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))
def sendButtont(event):  #按鈕樣版
	    try:
	        message = TemplateSendMessage(
	            alt_text='按鈕樣板',
	            template=ButtonsTemplate(
	                thumbnail_image_url='https://i.imgur.com/K1yjnxe.jpg',  #顯示的圖片           
	                text='                天氣小幫手',  #副標題
	                actions=[	                   
                        URITemplateAction(  #開啟網頁
	                        label='天氣查詢',
	                        uri='https://liff.line.me/1655387687-7qPelRNg'
	                    ),	                    
	                ]
	            )
	        )
	        line_bot_api.reply_message(event.reply_token, message)
	    except:
	        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))
		
		

def sendButtonu(event):  #按鈕樣版
	    try:
	        message = TemplateSendMessage(
	            alt_text='按鈕樣板',
	            template=ButtonsTemplate(
	                thumbnail_image_url='https://i.imgur.com/0lWM4Ic.jpg',  #顯示的圖片           
	                text='               2020旅遊調查',  #副標題
	                actions=[	                   
                        URITemplateAction(  #開啟網頁
	                        label='開始填寫',
	                        uri='https://liff.line.me/1655387687-N6V5Dx2b'
	                    ),	                    
	                ]
	            )
	        )
	        line_bot_api.reply_message(event.reply_token, message)
	    except:
	        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))	

def sendButtonv(event):  #按鈕樣版
	    try:
	        message = TemplateSendMessage(
	            alt_text='按鈕樣板',
	            template=ButtonsTemplate(
                        text='               警廣即時路況',  #副標題
	                actions=[	                   
                        URITemplateAction(  #開啟網頁
	                        label='即時路況',
	                        uri='https://liff.line.me/1655387687-86lXgYG3'
	                    ),
                    ]
	            )
	        )
	        line_bot_api.reply_message(event.reply_token, message)
	    except:
	        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))


def sendButtonx(event):  #按鈕樣版
	    try:
	        message = TemplateSendMessage(
	            alt_text='按鈕樣板',
	            template=ButtonsTemplate(
                        text='               警廣即時路況',  #副標題
	                actions=[	                   
                        URITemplateAction(  #開啟網頁
	                        label='即時路況1',
	                        uri='https://google-translate-proxy.herokuapp.com/api/tts?query=%27羅斯福路+基隆路口.汽車+機車事故-通知續%27&language=zh-tw'
	                    ),
                        URITemplateAction(  #開啟網頁
	                        label='即時路況2',
	                        uri='https://google-translate-proxy.herokuapp.com/api/tts?query=%27[台61線((西濱快速))] 北上157.7km   龍井交流道前 指示牌看起來有點搖晃(已排除) 後續排除%27&language=zh-tw'
	                    ),	                    
                    ]
	            )
	        )
	        line_bot_api.reply_message(event.reply_token, message)
	    except:
	        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))
		
		
def sendVoice(event):  #傳送聲音
            try:
                  message = AudioSendMessage(
	          original_content_url='https://google-translate-proxy.herokuapp.com/api/tts?query=%27[台61線((西濱快速))] 北上157.7km指示牌看起來有點搖晃(已排除)後續排除%27&language=zh-tw',  #聲音檔置於static資料夾
                  duration=20000  #聲音長度20秒
                  ),
                  line_bot_api.reply_message(event.reply_token, message)
            except:
                line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))
"""
def sendVedio(event):  #傳送影像
    try:
        message = VideoSendMessage(
            original_content_url=baseurl + 'robot.mp4',  #影片檔置於static資料夾
            preview_image_url=baseurl + 'robot.jpg'
        )
        line_bot_api.reply_message(event.reply_token, message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))
"""

def sendFlex(event):  #彈性配置
    try:
        bubble = BubbleContainer(
            direction='ltr',  #項目由左向右排列
            header=BoxComponent(  #標題
                layout='vertical',
                contents=[
                    TextComponent(text='冰火飲料', weight='bold', size='xxl'),
                ]
            ),
            hero=ImageComponent(  #主圖片
                url='https://i.imgur.com/3sBRh08.jpg',
                size='full',
                aspect_ratio='792:555',  #長寬比例
                aspect_mode='cover',
            ),
            body=BoxComponent(  #主要內容
                layout='vertical',
                contents=[
                    TextComponent(text='評價', size='md'),
                    BoxComponent(
                        layout='baseline',  #水平排列
                        margin='md',
                        contents=[
                            IconComponent(size='lg', url='https://i.imgur.com/GsWCrIx.png'),
                            TextComponent(text='25   ', size='sm', color='#999999', flex=0),
                            IconComponent(size='lg', url='https://i.imgur.com/sJPhtB3.png'),
                            TextComponent(text='14', size='sm', color='#999999', flex=0),
                        ]
                    ),
                    BoxComponent(
                        layout='vertical',
                        margin='lg',
                        contents=[
                            BoxComponent(
                                layout='baseline',
                                contents=[
                                    TextComponent(text='營業地址:', color='#aaaaaa', size='sm', flex=2),
                                    TextComponent(text='台北市信義路14號', color='#666666', size='sm', flex=5)
                                ],
                            ),
                            SeparatorComponent(color='#0000FF'),
                            BoxComponent(
                                layout='baseline',
                                contents=[
                                    TextComponent(text='營業時間:', color='#aaaaaa', size='sm', flex=2),
                                    TextComponent(text="10:00 - 23:00", color='#666666', size='sm', flex=5),
                                ],
                            ),
                        ],
                    ),
                    BoxComponent(  
                        layout='horizontal',
                        margin='xxl',
                        contents=[
                            ButtonComponent(
                                style='primary',
                                height='sm',
                                action=URIAction(label='電話聯絡', uri='tel:0987654321'),
                            ),
                            ButtonComponent(
                                style='secondary',
                                height='sm',
                                action=URIAction(label='查看網頁', uri="http://www.e-happy.com.tw")
                            )
                        ]
                    )
                ],
            ),
            footer=BoxComponent(  #底部版權宣告
                layout='vertical',
                contents=[
                    TextComponent(text='Copyright@ehappy studio 2019', color='#888888', size='sm', align='center'),
                ]
            ),
        )
        message = FlexSendMessage(alt_text="彈性配置範例", contents=bubble)
        line_bot_api.reply_message(event.reply_token,message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))

def manageForm2(event, mtext):
    try:
        flist = mtext[3:].split('/')
        text1 = '姓名：' + flist[0] + '\n'
        text1 += '日期：' + flist[1] + '\n'
        text1 += '包廂：' + flist[2]
        message = TextSendMessage(
            text = text1
        )
        line_bot_api.reply_message(event.reply_token,message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))
        


def sendUse(event):  #使用說明
    try:
        text1 ='''
1. 「房間預約」及「取消訂房」可預訂及取消訂房。每個 LINE 帳號只能進行一個預約記錄。
2. 「關於我們」對旅館做簡單介紹及旅館圖片。
3. 「位置資料」列出旅館地址，並會顯示地圖。
4. 「聯絡我們」可直接撥打電話與我們聯繫。
               '''
        message = TextSendMessage(
            text = text1
        )
        line_bot_api.reply_message(event.reply_token,message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))

def sendBooking(event, user_id):  #房間預約
    try:
       # if not (booking.objects.filter(bid=user_id).exists()):  #沒有訂房記錄
            message = TemplateSendMessage(
                alt_text = "房間預約",
                template = ButtonsTemplate(
                    thumbnail_image_url='https://i.imgur.com/1NSDAvo.jpg',
                    title='房間預約',
                    text='您目前沒有訂房記錄，可以開始預訂房間。',
                    actions=[
                        URITemplateAction(label='房間預約', uri='https://liff.line.me/1654180187-Y6rO6gmz')  #開啟LIFF讓使用者輸入訂房資料
                    ]
                )
            )
     #   else:  #已有訂房記錄
         #   message = TextSendMessage(
            #    text = '您目前已有訂房記錄，不能再訂房。'
          #  )
            line_bot_api.reply_message(event.reply_token,message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))

def sendCancel(event, user_id):  #取消訂房
    try:
        if booking.objects.filter(bid=user_id).exists():  #已有訂房記錄
            bookingdata = booking.objects.get(bid=user_id)  #讀取訂房資料
            roomtype = bookingdata.roomtype
            amount = bookingdata.roomamount
            in_date = bookingdata.datein
            out_date = bookingdata.dateout
            text1 = "您預訂的房間資料如下："
            text1 += "\n房間型式：" + roomtype
            text1 += "\n房間數量：" + amount
            text1 += "\n入住日期：" + in_date
            text1 += "\n退房日期：" + out_date
            message = [
                TextSendMessage(  #顯示訂房資料
                    text = text1
                ),
                TemplateSendMessage(  #顯示確認視窗
                    alt_text='取消訂房確認',
                    template=ConfirmTemplate(
                        text='你確定要取消訂房嗎？',
                        actions=[
                            PostbackTemplateAction(  #按鈕選項
                                label='是',
                                data='action=yes'
                            ),
                            PostbackTemplateAction(
                                label='否',
                                data='action=no'
                           )
                        ]
                    )
                )
            ]
        else:  #沒有訂房記錄
            message = TextSendMessage(
                text = '您目前沒有訂房記錄！'
            )
        line_bot_api.reply_message(event.reply_token,message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))

def sendAbout(event):  #關於我們
    try:
        text1 = "我們提供良好的環境及優質的住宿服務，使您有賓至如歸的感受，歡迎來體驗美好的經歷。"
        message = [
            TextSendMessage(  #旅館簡介
                text = text1
            ),
            ImageSendMessage(  #旅館圖片
                original_content_url = "https://i.imgur.com/1NSDAvo.jpg",
                preview_image_url = "https://i.imgur.com/1NSDAvo.jpg"
            ),
        ]
        line_bot_api.reply_message(event.reply_token,message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))

def sendPosition2(event):  #位置資訊
    try:
        text1 = "地址：南投縣埔里鎮信義路85號"
        message = [
            TextSendMessage(  #顯示地址
                text = text1
            ),
            LocationSendMessage(  #顯示地圖
                title = "宜居旅舍",
                address = text1,
                latitude = 23.97381,
                longitude = 120.977198
            ),
        ]
        line_bot_api.reply_message(event.reply_token,message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))

def sendContact(event):  #聯絡我們
    try:
        message = TemplateSendMessage(
            alt_text = "聯絡我們",
            template = ButtonsTemplate(
                thumbnail_image_url='https://i.imgur.com/tVjKzPH.jpg',
                title='聯絡我們',
                text='打電話給我們',
                actions=[
                    URITemplateAction(label='撥打電話', uri='tel:0123456789')  #開啟打電話功能
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token,message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))

def sendContactp(event):  #聯絡我們
    try:
        message = TemplateSendMessage(
            alt_text = "聯絡我們",
            template = ButtonsTemplate(
                thumbnail_image_url='https://i.imgur.com/tVjKzPH.jpg',
                text='警廣回報路況',
                actions=[
                    URITemplateAction(label='撥打電話0800000123', uri='tel:0800000123')  #開啟打電話功能
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token,message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))
	
def manageForm(event, mtext, user_id):  #處理LIFF傳回的FORM資料
    try:
        flist = mtext[3:].split('/')  #去除前三個「#」字元再分解字串
        roomtype = flist[0]  #取得輸入資料
            
        
        #unit = booking.objects.create(bid=user_id, roomtype=roomtype, roomamount=amount)  #寫入資料庫
        #unit.save()
        
        text1 = "您的查詢統一編號資料如下："
        text1 += "\n統一編號：" + roomtype
        message = TextSendMessage(  #顯示訂房資料
        text = text1
        )
        line_bot_api.reply_message(event.reply_token,message)
    
        students =student.objects.all().order_by('id')  #讀取資料表, 依 id 遞增排序 student2.objects.get(name="王俊德") #讀取一筆資料
        return render(request, "listall.html", locals())
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))

def sendYes2(event, user_id):  #處理取消訂房
    try:
        datadel = booking.objects.get(bid=user_id)  #從資料庫移除資料記錄
        datadel.delete()
        message = TextSendMessage(
            text = "您的房間預訂已成功刪除。\n期待您再次預訂房間，謝謝！"
        )
        line_bot_api.reply_message(event.reply_token,message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))

def pushMessage(event, mtext):  ##推播訊息給所有顧客
    try:
        msg = mtext[4:]  #取得訊息
        userall = users.objects.all()
        for user in userall:  #逐一推播
            message = TextSendMessage(
                text = msg
            )
            line_bot_api.push_message(to=user.uid, messages=[message])  #推播訊息
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))
