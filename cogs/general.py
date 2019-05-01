ZATSUDAN_FORUM_ID = 515467348581416970

join_message = """
───────────────────────
{0}さん、
ようこそ{1}へ！:tada: :hugging:
雑談フォーラムは雑談に特化したDiscordサーバー。
しかし、現状はほとんどのチャンネルが
利用できないようになっています。
<#515467524960157716> をよく読み、
「アカウント登録」を
済ませてからご参加ください！


当サーバーに関する情報はこちらをご覧ください：
https://chat-forum-dcc.jimdo.com/
──────────────────────
"""


rolepanel_channel = 515467531176116224

agree_messages = [
    "{0}がサーバーに飛び込んだ！カンガルーだ！",
    "{0}の参上だ！",
    "{0}が来た。しばらくの間、話を聞くのじゃ。",
    "{0}の登場だ。刮目せよ！",
    "{0}だ！トラップカード発動！",
    "{0}、そんな装備で大丈夫か？",
    "{0}はいいぞ。",
    "{0}が参加したってそマ！？",
    "{0}が来た！ワンチャンあるぞ。",
    "{0}が参加したンゴ。優しくするやで～。",
    "{0}がきっとくる～",
    "{0}、入ってる。",
    "{0}のフレンズなんだね～！すっごーい！",
    "{0}はこのサーバーにいるのさ！",
    "{0}君、やぁ。ピザは持ってきたよね？",
    "{0}が来た。あいつチートだろ...弱体修正まだ？",
    "{0}、Come on baby Chat forum～！",
    "{0}(水属性)がとびだしてきた！",
    "{0}、みんなあなたを待っていた！",
    "{0}に任せて！",
    "{0}が来たぞ。お遊びは終わりだ。",
    "{0}さん、ようこそ。武器はドアのそばに置いていってね。",
    "{0}、ゆっくりしていってね！",
    "{0}、もっと！熱くなれよ！",
    "{0}と共にあらんことを。",
    "{0}が帰還した！お疲れ様！",
    "その、雑談フォーラムの中に、さらに、入ってきたのが{0}です。",
    "{0}にもっと注目するといいと、{1}も思います",
    "あれは、{0}、{0}マーン、{0}マーン"
]

voice_text = {
    515467645684809748: 515467627209031690,
    515467647341821963: 515467629176029197,
    515467649564672020: 515467631176974336,
    515467651691315220: 515467633282383882,
    515467653712707594: 515467635345981440,
    515467655378108417: 515467636994473985,
    515467658053943297: 515467639229775874,
    515467660067209227: 515467643285667840,
    531105433612451840: 531105503372378112,
    572773079680417802: 572772939112382474,
}

free_categories = [
    531634881860599818,
    515467876556210191,
    515467988535869440,
    515468108392169482
]

spam = [515467956113768483, 555687014872383488, 534340672300515328]


board_kwargs = {
    'guild_id': ZATSUDAN_FORUM_ID,
    'channel_id': [
        572772143729868806,
        572757718939729921,
    ],
    'category_id': [573129192879685652, 572771784408039424, 573121719460691988]
}

async def is_zatudanfolum(ctx):
    try:
        guild = ctx.guild
    except AttributeError:
        return False
    else:
        return guild is not None and guild.id == ZATSUDAN_FORUM_ID


async def is_staff(member):
    if await is_zatudanfolum(member):
        return any(r.id in (515467407381364738, 515467410174902272, 515467421323100160) for r in member.roles)
    else:
        return False
