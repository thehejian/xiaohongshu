# -*- coding: utf-8 -*-
# topics 101-149 data
import sys as _sys, os as _os
_sys.path.insert(0, _os.path.dirname(__file__))

LQ = '\u201c'
RQ = '\u201d'

_HEAD = "Ink wash painting style, light rice paper texture, flowing ink strokes, subtle crimson and grey colors, sparse composition with negative space, misty atmosphere."

def _court(t, h=_HEAD):
    return h + " Han dynasty shenyi robe with crossed-collar right closure, traditional topknot with guan headpiece, palace with rammed-earth walls and tiled roof, low tables and floor mats. " + t

def _military(t, h=_HEAD):
    return h + " Han iron lamellar armor on soldiers, ring-pommel dao, Han crossbow, tense battlefield atmosphere with charging cavalry, dust and urgency. " + t

def _daily(t, h=_HEAD):
    return h + " Han dynasty period setting with appropriate clothing and architecture. " + t

T = {}
TOPICS = T

T[101] = {
    "folder": "zhao-di-huoguang",
    "article": """昭帝与霍光\u2014\u2014君臣绝配的昭宣前奏

公元前87年，汉武帝驾崩，遗诏命八岁的刘弗陵即位，大司马大将军霍光领尚书事辅政。一个小孩加一个秘书，开启了西汉最后的辉煌。

霍光跟着武帝做了三十年秘书，出入宫门每一步落点尺寸都不差。这份精准谨慎，让他成了武帝朝唯一零差错的幸存者。但武帝走后，天下人都不服\u2014\u2014你一个秘书，凭什么掌权？

不服的人很快跳了出来。燕王刘旦宣称长安\u201c玺封有异\u201d，起兵造反；左将军上官桀联合长公主、御史大夫桑弘羊密谋废掉霍光；就连霍光一手提拔的桑弘羊也觉得霍光挡了自己的路。三股势力同时发难，诏书写得煞有其事，要罢免霍光的兵权。

十四岁的昭帝把诏书往地上一扔：\u201c大将军是忠臣，先帝托他辅佐朕，谁敢再诋毁大将军，法办！\u201d霍光跪在地上，一句话没说。他不需要说话\u2014\u2014皇帝替他挡了。

昭帝十四岁就有这个判断力，加上霍光三十年练出来的治政手腕，这对君臣用了十三年时间，把武帝留下的烂摊子\u2014\u2014连年征战、民生凋敝、酷吏横行\u2014\u2014一样一样收拾干净。昭宣之治的根基，就是在这十三年里打下的。#汉昭帝 #霍光 #昭宣之治 #汉武帝后
""",
    "prompts": [
        _court("Young Emperor Zhao enthroned at 8, Huo Guang kneeling beside him receiving the edict. Chinese title '\u201c昭帝与霍光\u201d' in calligraphic brush style. No heavy outlines. Ample whitespace."),
        _court("Huo Guang walking into court, ministers bowing. Chinese title '\u201c君臣默契\u201d' in calligraphic brush style. No heavy outlines."),
        _court("Emperor Zhao at 14 rejecting false accusations against Huo Guang, throwing the edict to the ground. Chinese title '\u201c少帝护相\u201d' in calligraphic brush style. No heavy outlines."),
    ]
}

T[102] = {
    "folder": "salt-iron-debate",
    "article": """盐铁会议\u2014\u2014国家干预与自由市场的终极对决

公元前81年，长安未央宫里摆了一场大辩论。六十多个来自全国各地的\u201c贤良文学\u201d\u2014\u2014民间知识分子\u2014\u2014跟御史大夫桑弘羊面对面坐着，辩论盐铁专卖到底该不该废除。这可能是人类历史上最早的宏观经济政策大讨论。

武帝打了四十年仗，钱从哪来？盐铁官营、均输平准、酒类专卖。桑弘羊一手打造了这套国家资本主义体系，用行政手段把民间利润全收进国库。打仗是打赢了，但民间富户消失殆尽，小商贩活不下去，农民连买盐的钱都没有。

贤良文学们说：与民争利，国将不国。盐铁该放开给民间经营，让老百姓自己赚钱，国家才有真正的富足。

桑弘羊冷笑：盐铁放开了，豪强巨贾立马垄断，比国家更狠。国家手里没钱，匈奴再打过来怎么办？靠你们这些读书人去劝降？

辩论持续了整整一个月。最后霍光没有完全采纳贤良文学的主张\u2014\u2014盐铁官营留着，酒专卖废了。这是一个标准的政治妥协：改了武帝的极端政策，但没动摇国家财政的根基。

这场辩论的意义远超西汉一朝。此后两千年，只要国家缺钱，\u201c盐铁专卖\u201d就会自动回归。国家与市场的边界该画在哪\u2014\u2014这个问题直到今天也没有标准答案。#盐铁论 #桑弘羊 #霍光 #国家资本主义
""",
    "prompts": [
        _court("Debate scene at Weiyang Palace: Sang Hongyang facing dozens of scholars, intense discussion. Chinese title '\u201c盐铁之辩\u201d' in calligraphic brush style. No heavy outlines. Ample whitespace."),
        _court("Close up of Sang Hongyang counting coins on a desk, salt and iron ingots beside him. Chinese title '\u201c官营之利\u201d' in calligraphic brush style. No heavy outlines."),
        _daily("Han commoners queuing at a state-run salt shop, pottery jars. Chinese title '\u201c百姓买盐\u201d' in calligraphic brush style. No heavy outlines."),
    ]
}

T[103] = {
    "folder": "zhao-di-legacy",
    "article": """汉昭帝高评价\u2014\u2014十三岁即位，二十出头驾崩，在位十三年，硬是把武帝留下的烂摊子收拾出了方向。后世史学家对这位少年天子的评价出奇一致：如果多活二十年，他的历史排名不会低于汉文帝。

昭帝即位时才八岁。武帝末年全国户口减半，国库空虚，蜀地三万人造反，边境烽火不断。换了任何一个成年皇帝都未必撑得住\u2014\u2014何况一个八岁的孩子。

但昭帝做对了两件事。第一，他完全信任霍光。这不是盲从\u2014\u2014十四岁那年，上官桀等人写了封假诏书要罢霍光的兵权，昭帝一眼识破。第二，他自己不折腾。武帝什么都想干，昭帝什么都不想干\u2014\u2014把军队撤回来，把赋税降下来，把监狱里关的人放出去。

史书记载昭帝\u201c轻徭薄赋，与民休息\u201d。翻成白话：少收税，少打仗，让大家喘口气。武帝留下的几千万人口，在昭帝十三年里恢复到了五千多万。盐铁会议开了三十天，他坐在帘子后面从头听到尾，不表态不站队，让大臣们自己吵出结果。

一个二十出头就去世的年轻人，留下的评价不是\u201c可惜早逝\u201d，而是\u201c幸好有这十三年\u201d。对于一个帝王来说，能有这个评价，已经赢了。#汉昭帝 #与民休息 #昭宣之治
""",
    "prompts": [
        _court("Young Emperor Zhao reviewing memorials at his desk, Huo Guang standing respectfully to the side. Chinese title '\u201c少年天子\u201d' in calligraphic brush style. No heavy outlines. Ample whitespace."),
        _court("Emperor Zhao sitting behind a screen listening to the Salt and Iron Debate, scholars arguing before him. Chinese title '\u201c帘后听政\u201d' in calligraphic brush style. No heavy outlines."),
        _daily("Han commoners farming peacefully, children playing, sign of prosperous recovery. Chinese title '\u201c与民休息\u201d' in calligraphic brush style. No heavy outlines."),
    ]
}

T[104] = {
    "folder": "fu-jiezi-loulan",
    "article": """傅介子刺楼兰\u2014\u2014大汉朝最干脆的一次外交行动

公元前77年，西域楼兰国王安归倒向匈奴，屡次劫杀汉朝使节和商队。楼兰地处西域门户，扼守丝绸之路咽喉，是大汉通往西域的第一道关卡。霍光在长安看完情报，只说了一个字：换。

执行者叫傅介子，当时的身份是骏马监，管养马的。他从长安出发，只带了三十名勇士，一路走到楼兰。到了王宫门口，对楼兰王说：大汉天子赐你金币，请王出来领赏。

楼兰王安归犹豫了一下。汉使曾被匈奴威胁，安归不敢不见，又怕汉使设局。最后贪念占了上风\u2014\u2014他带着卫士出了宫。傅介子设宴招待，酒过三巡，他对安归说：天子有几句话要单独跟你说。

两人走到帐幕后面。傅介子使了个眼色，两名壮士从背后一刀刺入安归胸口，当场毙命。

楼兰王的卫士拔刀要冲。傅介子不慌不忙，举着大汉符节走出帐幕，大声宣布：\u201c安归负汉，天子派我诛之。你们的新王叫尉屠耆，是大汉亲自选定的。谁敢反抗，大汉的军队就在门外。\u201d

这一刀，把楼兰从此改名鄯善，彻底倒向汉朝。后世王昌龄写诗：\u201c黄沙百战穿金甲，不破楼兰终不还。\u201d那声呼喊穿透了八百年的边塞风沙。#傅介子 #楼兰 #霍光 #西域
""",
    "prompts": [
        _military("Fu Jiezi with 30 warriors at the gate of Loulan, desert backdrop. Chinese title '\u201c傅介子刺楼兰\u201d' in calligraphic brush style. No heavy outlines. Ample whitespace."),
        _court("Fu Jiezi feasting the Loulan king, assassins hidden behind curtain. Chinese title '\u201c宴席杀机\u201d' in calligraphic brush style. No heavy outlines."),
        _military("Han envoy holding imperial seal in front of Loulan palace, announcing the new king. Chinese title '\u201c斩首\u00b7易主\u201d' in calligraphic brush style. No heavy outlines."),
    ]
}

T[105] = {
    "folder": "zhao-di-rectification",
    "article": """昭帝拨乱反正\u2014\u2014五大领域清理武帝遗产

武帝轮台罪己诏虽然承认了错误，但遗留的问题一样没少\u2014\u2014连年战争拉空了国库，酷吏政治搞垮了官僚体系，告缗令摧毁了民间商业。昭帝和霍光用十三年时间，在五个方向上做减法。

第一，停战。武帝末年还准备打大宛，昭帝即位后全面收缩边疆驻军。匈奴来犯就打，打完了就撤，不追击不占领。士兵回家种地，军费开支砍了一半。

第二，减税。武帝时的算缗钱、车船税、口赋全部下调。昭帝在位的第四年，直接免除了当年所有田租。农民在地里干活，税吏不来，这就是最大的恩惠。

第三，废酷法。沈命法（地方官抓不够盗贼就要处死）、腹诽法（心里想什么都能定罪）全部废除。张汤种的酷吏之树，被连根拔起。

第四，缓刑。武帝末年关押的政治犯满为患。昭帝四次大赦天下，把监狱里关了几年的巫蛊案牵连者全放了。很多人在狱中关到头发白了，走出监狱大门时，外面已经换了一个皇帝。

第五，裁官。武帝朝膨胀的官僚队伍被大幅削减，尚书台的人事规模恢复了文景时期的水平。

五件事，没有一件是开创性的。全是\u201c不做\u201d\u2014\u2014不打仗，不收税，不抓人，不折腾。有时候，最好的治国就是少做事。#汉昭帝 #拨乱反正 #霍光 #轮台罪己
""",
    "prompts": [
        _court("Emperor Zhao signing edicts one by one, scrolls piled on desk. Chinese title '\u201c减负诏书\u201d' in calligraphic brush style. No heavy outlines. Ample whitespace."),
        _daily("Han farmers working in fields, no tax collectors in sight, peaceful countryside. Chinese title '\u201c免租之喜\u201d' in calligraphic brush style. No heavy outlines."),
        _court("Prison gates opening, prisoners being released, their families waiting outside. Chinese title '\u201c大赦天下\u201d' in calligraphic brush style. No heavy outlines."),
    ]
}

T[106] = {
    "folder": "zhao-di-harem",
    "article": """昭帝绝后\u2014\u2014一条穷裤与权力基因的垄断

公元前74年，二十一岁的汉昭帝病逝，没有留下一个子嗣。这个结果不是天意，是人算。

昭帝十二岁时，霍光把六岁的外孙女上官氏送入宫中，立为皇后。六岁的女孩嫁给了十二岁的男孩\u2014\u2014两人与其说是夫妻，不如说是玩伴。

霍光的算盘很简单：让上官家的女儿（也是霍家的外孙女）给昭帝生下太子，霍家的血统就能名正言顺地继承帝位。为了保证外孙女受宠，霍光做了两件事。

第一，他让太医告诉其他后宫嫔妃：皇上身体不好，不能频繁亲近女色。太医们全都是霍光的人，皇帝的身体状况由他说了算。

第二，他下令后宫女子全部穿\u201c穷裤\u201d\u2014\u2014一种前后系带多层的紧口内裤，穿脱极不方便。这几乎是物理层面的禁欲。

昭帝不是傻子，但十四岁识破假诏书的少年，面对权倾朝野的霍光，同样无力反抗。他的后宫形同虚设，上官皇后从未怀孕。

公元前74年，昭帝病逝于未央宫。霍光垄断皇权血脉的计划，因为皇帝死得太早而落空。但最讽刺的是，这个六岁入宫、十五岁就守寡的上官皇后，此后在宫中又活了四十年\u2014\u2014她的一生，从六岁那年起就已经被书写完毕。#汉昭帝 #霍光 #上官皇后 #穷裤
""",
    "prompts": [
        _court("Young Queen Shangguan at 6 years old entering the palace, Huo Guang watching from the side. Chinese title '\u201c六岁皇后\u201d' in calligraphic brush style. No heavy outlines. Ample whitespace."),
        _court("Palace scene with court ladies wearing restrictive qunku undergarments, imperial physician delivering Huo Guang's message. Chinese title '\u201c穷裤深宫\u201d' in calligraphic brush style. No heavy outlines."),
        _court("Emperor Zhao on his deathbed, Queen Shangguan young alone in mourning white. Chinese title '\u201c绝嗣而去\u201d' in calligraphic brush style. No heavy outlines."),
    ]
}

T[107] = {
    "folder": "liu-he-deposed",
    "article": """二十七日皇帝\u2014\u2014昌邑王刘贺的闪电废立

汉昭帝驾崩无子，霍光选中了昌邑王刘贺继承大统。刘贺接到诏书时正在喝酒打猎，听说自己要当皇帝，扔下酒杯就跑，一昼夜狂奔一百六十里进京。

但他只当了二十七天皇帝。

史书记载刘贺在这二十七天里犯了一千一百二十七件错事。平均每天四十多件。这个数字显然是夸张的\u2014\u2014撰写记录的霍光团队，把刘贺从昌邑带来的两百个随从全部定性为\u201c导引皇帝作恶的奸臣\u201d。

刘贺到底犯了什么不可饶恕的事？据史料还原，他做了三件让霍光忍不了的事：第一，把昌邑的旧部全部安插进要害部门，替换霍光的人；第二，在昭帝丧期喝酒看戏，违了礼法；第三，也是最重要的\u2014\u2014他问霍光：\u201c大将军，先帝时的盐铁专卖，是不是该考虑恢复了？\u201d

盐铁专卖是桑弘羊留给霍光的政治遗产之一\u2014\u2014减了量，但没废。刘贺这一问，触碰了霍光最敏感的神经：你想动我的政策，下一步是不是要动我的位置？

霍光联合大司农田延年、丞相杨敞率先发难。田延年在朝会上拔剑咆哮：\u201c先帝托孤于大将军，今皇帝昏乱，危及社稷，今日必须废立！谁敢反对，我这把剑不答应！\u201d

大臣们全吓傻了。杨敞（司马迁的女婿）吓得汗流浃背，连话都说不出来。刘贺被人从龙椅上拉下来，连滚带爬被送回昌邑。两百年后，他的墓在江西南昌被发现，出土的黄金比整个海昏侯国都重。#刘贺 #海昏侯 #霍光 #二十七日皇帝
""",
    "prompts": [
        _court("Liu He being crowned emperor, Huo Guang handing him the seal. Chinese title '\u201c登基大典\u201d' in calligraphic brush style. No heavy outlines. Ample whitespace."),
        _court("Liu He drinking wine during mourning period while Huo Guang watches angrily. Chinese title '\u201c丧期饮酒\u201d' in calligraphic brush style. No heavy outlines."),
        _court("Court scene: Tian Yannian holding a sword, shouting at Liu He to step down. Chinese title '\u201c剑指天颜\u201d' in calligraphic brush style. No heavy outlines."),
    ]
}

T[108] = {
    "folder": "haihunhou-tomb",
    "article": """海昏侯墓\u2014\u2014两千年后出土的西汉黄金屋

2015年，江西南昌一个叫墎墩山的地方，考古队挖开一座西汉大墓。墓门一开，所有人都愣住了。

十吨重的五铢钱堆成小山\u2014\u2014约两百万枚，相当于当时一个中等县的全年财政收入。金饼、马蹄金、麟趾金排列整齐，总重量超过一百二十公斤。这是中国汉代考古史上一次性出土黄金最多的一次。

墓主是刘贺\u2014\u2014那个当了二十七天皇帝就被霍光废掉的昌邑王，后来被贬为海昏侯。

刘贺的墓有多奢华？主椁室铺满漆器，全套编钟编磬，青铜雁鱼灯，孔子屏风\u2014\u2014屏风上还记载着孔子的生平和画像，比已知最早的孔子像还早了近百年。墓中出土了五千多枚竹简，包括了《论语》《易经》《礼记》等经典，其中失传了一千八百年的《齐论语》赫然在列。

刘贺被废后，霍光把他从长安赶回昌邑，削去王爵，软禁在昌邑城内，不许与外界往来。刘贺从此成了一个被历史遗忘的人。西汉史书给他的描述极其刻薄，说他\u201c行淫乱\u201d\u201c昏庸无道\u201d。

但考古学家对这座墓的评价是完全另一回事：墓中出土的《论语》抄本上有刘贺自己的批注，字迹工整认真。一个被史书定性为废物的人，在自己的墓里留下了完全不同的答案。历史是由胜利者书写的，但考古学家有权利不听。#海昏侯 #刘贺 #西汉考古 #齐论语
""",
    "prompts": [
        _court("Modern archaeologists opening the Haihunhou tomb, piles of gold coins visible inside. Chinese title '\u201c海昏侯墓\u201d' in calligraphic brush style. No heavy outlines. Ample whitespace."),
        _daily("Ten tons of Wuzhu coins stacked in a tomb chamber, gold ingots arranged in rows. Chinese title '\u201c两百万钱\u201d' in calligraphic brush style. No heavy outlines."),
        _daily("Confucius lacquer screen with portrait, bamboo slips scattered around. Chinese title '\u201c孔子屏风\u201d' in calligraphic brush style. No heavy outlines."),
    ]
}

T[109] = {
    "folder": "wei-prince-impostor",
    "article": """冒名卫太子案\u2014\u2014隽不疑的一场大考

公元前80年，长安城门口来了一个老人，自称是卫太子刘据。

刘据是汉武帝的嫡长子，三十八年的太子。公元前91年巫蛊之祸中，被江充诬陷，兵败逃亡，在湖县自缢。他的死是武帝晚年的最痛。

十一年过去了，突然有人自称卫太子还活着。消息传开，长安城的百姓蜂拥而至，街道堵得水泄不通。很多老臣心里打鼓\u2014\u2014当年刘据兵败，到底死没死透，谁也没亲眼看见尸体。

霍光和文武百官全都不敢说话。万一是真的卫太子，这地位比昭帝还高\u2014\u2014皇位按理该是他的。万一是假的，谁第一个开口说他是假、万一将来证明他是真的怎么办？

僵在那里的时候，京兆尹隽不疑从后排走上来。他不看那个老人，直接对霍光说：下令抓人。

霍光问：你凭什么？

隽不疑引用了《春秋》里的一个典故。春秋时期，卫国太子蒯聩得罪了父亲卫灵公，被赶出卫国。父亲死后，蒯聩的儿子即位当了国君。蒯聩跑回来要求复位，他的儿子拒绝了他\u2014\u2014\u201c出亡在外，即位的已是你的儿子，你回来就是逆命。\u201d卫国人把蒯聩抓了起来。

隽不疑说：卫太子当年起兵对抗武帝，已经是罪人。就算他还活着，他的儿子也没有即位，何况他本人？没有合法性的身份，就是冒名。抓。

霍光听了这话，马上拍板：抓。

后来一审，果然是假的\u2014\u2014是个跑江湖的算命先生，长得像卫太子，想来长安碰碰运气。

霍光后来说：隽不疑的《春秋》决狱，救了大汉一次。在法理和人情之间，一场大考被判得干干净净。#隽不疑 #卫太子 #巫蛊之祸 #春秋决狱
""",
    "prompts": [
        _court("Old man claiming to be Crown Prince Wei at Chang'an city gate, crowd gathering around. Chinese title '\u201c太子归来\u201d' in calligraphic brush style. No heavy outlines. Ample whitespace."),
        _court("Huo Guang and officials hesitating, Juan Buyi stepping forward from the back row. Chinese title '\u201c满朝不敢言\u201d' in calligraphic brush style. No heavy outlines."),
        _court("Juan Buyi quoting the Spring and Autumn Annals, officials listening in awe. Chinese title '\u201c春秋决狱\u201d' in calligraphic brush style. No heavy outlines."),
    ]
}

T[110] = {
    "folder": "xuan-di-childhood",
    "article": """汉宣帝童年\u2014\u2014从死囚婴儿到市井少年

公元前91年，长安监狱里关进来一个出生才几个月大的婴儿。这孩子是戾太子刘据的孙子，汉武帝的曾孙。巫蛊之祸中，他的爷爷死了，奶奶死了，父亲死了，母亲死了\u2014\u2014全家老小，只剩下他一个。

婴儿哪里知道什么谋反。但卫太子的血脉，就是原罪。武帝派郭穰去长安监狱：把卫太子家的所有人，全部处死。

负责监狱的官员丙吉关了门，不让郭穰进来。他对郭穰说：\u201c皇曾孙在此，无辜幼儿不得擅杀。\u201d在门口守了一夜。郭穰回去禀报武帝。武帝酒醒了，说了一句\u201c天使之也\u201d\u2014\u2014这是天意啊。于是大赦天下。

婴儿活了下来。丙吉给他取名刘病已\u2014\u2014病愈之意。刘病已在监狱里长到五岁，后来被送到祖母史良娣家寄养。再后来，他被接到了掖庭（后宫杂役区），由掖庭令张贺抚养。张贺是张汤的儿子，当年张汤的案子牵连了太多人，张贺也受够了政治迫害的苦。他看到刘病已，像是看到了曾经的自己。

刘病已在长安的市井街头长大。他跟斗鸡走狗的市井无赖混在一起，去上林苑看斗兽，去渭河边喝酒打架。他知道一个老百姓的米多少钱一斤，知道长安哪个市场的牛肉最新鲜，知道怎么从城东走到城西不被人查户籍。

后来，这个在街头混大的市井少年，成了大汉的第十位皇帝。#汉宣帝 #刘病已 #丙吉 #狱中太子
""",
    "prompts": [
        _court("Baby in prison, Bing Ji blocking the door with his body, refusing the execution order. Chinese title '\u201c狱中皇曾孙\u201d' in calligraphic brush style. No heavy outlines. Ample whitespace."),
        _daily("Young Liu Bingyi (Liu Xun) growing up in Chang'an streets, watching cockfights and dog races. Chinese title '\u201c市井少年\u201d' in calligraphic brush style. No heavy outlines."),
        _court("Bing Ji secretly teaching the young boy to read in a humble room. Chinese title '\u201c丙吉教读\u201d' in calligraphic brush style. No heavy outlines."),
    ]
}

T[111] = {
    "folder": "bing-ji-zhao-orphan",
    "article": """西汉版赵氏孤儿\u2014\u2014丙吉与汉宣帝

刘病已能活下来并最终登基，有一个最关键的人\u2014\u2014丙吉。他的名字在中国史上并不响亮，但他做的事，放在哪个时代都足以载入史册。

巫蛊之祸后，丙吉只是个管监狱的小官。他在长安监狱看到了那个被关押的皇曾孙，一个还在吃奶的婴儿。丙吉做了两件事：第一，给婴儿找奶妈\u2014\u2014他选了监狱里两个刚生完孩子的女囚犯胡组和郭徵卿，让她们轮流喂奶。第二，给婴儿换了个干净的单间\u2014\u2014用自己的俸禄买被子、买食物。

武帝下令杀绝卫太子血脉时，丙吉关上监狱大门，不顾自己可能被牵连。后来武帝大赦，丙吉一路护送孩子到祖母家。

刘病已长到十七岁那年，霍光废了刘贺，需要找一个新皇帝。丙吉\u2014\u2014已经升为大将军长史\u2014\u2014写了一封信给霍光：武帝的曾孙、戾太子的孙子刘病已，现在民间，通经术有才德，您可以看看。

霍光看了信，写了两个字：可立。

刘病已从市井一步踏入未央宫。当了皇帝后，他不知道自己小时候的事。丙吉从未主动提起。直到几年后，一个宫女上书说自己当年曾喂养过皇帝，丙吉才在朝会上说出了完整的真相。

宣帝当场泪流满面。他下令封丙吉为博阳侯、丞相。丙吉一生未曾炫耀过这件惊天之功。史书说他\u201c为人深厚，不伐善\u201d\u2014\u2014好事做了，从来不挂在嘴上。#丙吉 #汉宣帝 #巫蛊之祸 #恩人
""",
    "prompts": [
        _court("Bing Ji kneeling beside the prison bed, feeding a baby with a small spoon, two women prisoners nearby. Chinese title '\u201c狱中哺育\u201d' in calligraphic brush style. No heavy outlines. Ample whitespace."),
        _court("Bing Ji writing a letter to Huo Guang, recommending the young Liu Bingyi as emperor. Chinese title '\u201c荐帝之书\u201d' in calligraphic brush style. No heavy outlines."),
        _court("Emperor Xuan on the throne in tears, Bing Ji kneeling below. Chinese title '\u201c君臣相泣\u201d' in calligraphic brush style. No heavy outlines."),
    ]
}

T[112] = {
    "folder": "xuan-di-reign",
    "article": """孝宣之治\u2014\u2014西汉国力的巅峰

公元前74年，十七岁的刘病已从昌邑王府被接入未央宫，成为汉宣帝。这位从小在监狱和街头长大的皇帝，把汉朝推到了国力的最高峰。

宣帝的政治风格很简单：低调、务实、不折腾。他给自己起的年号很有意思\u2014\u2014本始、地节、元康、神爵\u2014\u2014全是\u201c开始\u201d\u201c节用\u201d\u201c安康\u201d之类的中性词，不像武帝那样雄心万丈。

但他做的事一点也不平庸。对内，他继续推行昭帝的休养生息政策，把田赋降到了三十税一\u2014\u2014这是中国历史上最低的农业税率。平准法和常平仓在全国推行，丰年国家平价收购粮食，灾年平价出售。粮价稳了，民心就稳了。

对外，他干成了武帝没干成的事\u2014\u2014让匈奴单于亲自来长安朝拜。公元前51年，呼韩邪单于带着全套匈奴仪仗队来到甘泉宫，向宣帝行藩臣之礼。从白登之围到孝宣之治，整整一百五十年，汉匈关系终于逆转。

宣帝最著名的治国理念只有八个字：\u201c霸道、王道，杂而用之。\u201d\u2014\u2014严刑峻法（霸道）和仁政教化（王道）两手都要硬。这八个字成了此后两千年中国王朝统治的基本公式，直到明清都没有变过。

在他治下，西汉的疆域达到极盛，人口恢复到武帝征伐之前的水平，国家监狱三年没有执行过一次死刑\u2014\u2014史称\u201c孝宣之治，侔德殷宗、周宣\u201d。一个街溜子出身的皇帝，做到了汉朝的最高境界。#汉宣帝 #孝宣之治 #常平仓 #王道霸道
""",
    "prompts": [
        _court("Emperor Xuan sitting on the throne, humble and alert, signing agricultural reform edicts. Chinese title '\u201c孝宣中兴\u201d' in calligraphic brush style. No heavy outlines. Ample whitespace."),
        _court("Huhanye Chanyu of the Xiongnu kneeling before Emperor Xuan at Ganquan Palace. Chinese title '\u201c单于朝汉\u201d' in calligraphic brush style. No heavy outlines."),
        _daily("Han farmers storing grain in a public granary, officials recording amounts. Chinese title '\u201c常平仓\u201d' in calligraphic brush style. No heavy outlines."),
    ]
}

T[113] = {
    "folder": "sword-oath-huozhi-massacre",
    "article": """古剑情深\u2014\u2014许平君之死与霍氏灭门

宣帝即位后，霍光提出要把女儿嫁给宣帝做皇后。宣帝不想，但他不敢直接拒绝。他下了一道诏书：朕贫贱时有一把古剑，现在找不到了，各位爱卿替朕找找。

大臣们立刻明白了\u2014\u2014故剑情深。宣帝在民间娶的妻子叫许平君，他当了皇帝，想立她做皇后。霍光的女儿只能做妃子。霍光气得发抖，但诏书已经下了，他不能公开反对。

许平君被立为皇后后，霍光老婆霍显买通了女医，在许平君分娩后下毒。许皇后喝了掺了附子的药膳汤，浑身抽搐，很快毒发身亡。死时年仅十九岁。

宣帝知道妻子死得蹊跷，但他什么都没说。他立霍光的女儿为后，封霍家的子弟为将军、列侯。霍光废过一任皇帝，杀一个皇后对他来说不算什么。宣帝继续笑，继续忍。

公元前68年，霍光去世。宣帝以帝王之礼厚葬霍光，规格堪比皇帝。霍家人以为安全了。

两年后，宣帝废了霍皇后，下令彻查许皇后之死。霍家子弟谋反\u2014\u2014宣帝早有准备。兵围霍府，霍显母子被腰斩。霍光的儿子霍禹被处以极刑。整个霍氏家族，包括与霍家联姻的无数世家，被连根拔起，灭门者数千家。

故剑仍在，持剑之人已不在。宣帝杀光霍家满门后，再也没有立过皇后。#故剑情深 #许平君 #霍光 #霍氏灭门
""",
    "prompts": [
        _court("Young Emperor Xuan telling his officials about the old sword, his beloved Xu Pingjun beside him. Chinese title '\u201c故剑情深\u201d' in calligraphic brush style. No heavy outlines. Ample whitespace."),
        _daily("Empress Xu on her sickbed, a female physician preparing poisoned soup. Chinese title '\u201c毒后之祸\u201d' in calligraphic brush style. No heavy outlines."),
        _court("Huo family mansion surrounded by imperial guards, arrest scene. Chinese title '\u201c霍府覆灭\u201d' in calligraphic brush style. No heavy outlines."),
    ]
}

T[114] = {
    "folder": "huo-marriage-web",
    "article": """霍家联姻网\u2014\u2014权力婚姻的大网如何笼罩西汉

霍光辅政二十年，他的权力不仅来自大司马大将军的头衔，更来自一张密不透风的联姻网。这张网编织得有多密？

霍光的外孙女是上官皇后（昭帝的皇后）。霍光的女儿霍成君是宣帝的第二任皇后。霍光的儿子霍禹娶了公主。霍光的侄孙女嫁给了宣帝的太子刘奭（后来的元帝）。霍光的女婿们遍布朝廷，度辽将军范明友是霍光的女婿，给事中任宫也是霍光的女婿。丞相府的属官、尚书台的郎官、殿中的禁卫将领\u2014\u2014到处都是霍家的人或霍家的亲戚。

宣帝每次上朝，感觉满朝文武跟他说话都要先看看霍光的脸色。他坐的那个龙椅，似乎只是暂借给他的。

这种局面有一个专业名词叫\u201c内外朝合流\u201d\u2014\u2014霍光把皇帝的决策层和行政层全部占了。宣帝名义上是皇帝，实际上跟提线木偶没什么两样。

霍光死后，宣帝花了三年才把这张网撕开。方法也很直接\u2014\u2014查贪污。霍家没有一个人经得起查。霍光在世时生活简朴，但他的儿子霍禹光在长安就养了三十多匹纯种西域马，每匹价值上百万钱。

这张联姻网的崩塌，带走了两千多颗人头。那些曾经因为姓霍或者娶了霍家女儿而飞黄腾达的人，一夜之间回到了起点。权力的赌桌上，没有人能光靠姻亲赢到最后。#霍光 #联姻 #外戚 #霍氏灭门
""",
    "prompts": [
        _court("Diagram of Huo Guang's marriage network, lines connecting royal and Huo family names. Chinese title '\u201c霍家联姻网\u201d' in calligraphic brush style. No heavy outlines. Ample whitespace."),
        _court("Emperor Xuan on the throne, Huo Guang's relatives all around in court positions. Chinese title '\u201c满朝霍氏\u201d' in calligraphic brush style. No heavy outlines."),
        _court("Huo family compound with luxury horses and carriages, indicating wealth. Chinese title '\u201c权倾朝野\u201d' in calligraphic brush style. No heavy outlines."),
    ]
}

T[115] = {
    "folder": "li-prince-posthumous",
    "article": """戾太子之谜\u2014\u2014汉宣帝为何给爷爷上恶谥

汉宣帝登基后，追尊自己的祖父刘据为\u201c戾太子\u201d。戾这个字在谥法中是什么意思？\u201c不悔前过曰戾\u201d，也就是不知悔改。

一个被冤杀的太子，他的孙子当了皇帝，为什么不翻案平反，反而给爷爷上一个\u201c不知悔改\u201d的恶谥？

这要从武帝晚年说起。巫蛊之祸中，刘据确实起兵了\u2014\u2014他调用了长乐宫的卫队，跟丞相刘屈氂的军队在长安城内打了五天。史书上说刘据\u201c矫节发兵\u201d，也就是假传圣旨调兵。不管他有什么理由，起兵对抗皇帝就是不忠不孝。武帝虽然后来后悔了，杀了江充全家，建了思子宫，但官方定性从未更改\u2014\u2014刘据就是反了。

宣帝如果要给爷爷平反，就必须否定武帝的判断。而否定武帝，就等于否定汉朝皇权的合法性\u2014\u2014武帝是汉朝功业最盛的一个皇帝，否定他意味着整个大汉帝国的根基动摇。

宣帝在政治上极其务实。他选择了一个折中的方案：追尊祖父为\u201c戾太子\u201d，承认祖父起兵是错误的，但用太子的礼仪重新安葬。后来又追尊为\u201c戾皇\u201d，但没有给他正式的皇帝庙号。

史学家分析这个谥号还有另一层含义：宣帝在告诉天下人\u2014\u2014我不会因为个人感情而推翻先帝的结论。我是武帝的合法继承人，不是来翻旧案的。

戾太子的故事在数千年后仍让人唏嘘。一个从未犯错的太子，因为一场莫须有的巫蛊之祸，被父亲逼死，被孙子定谳。历史的残酷不在于刀剑，而在于不得不做的选择题。#戾太子 #汉宣帝 #巫蛊之祸 #谥号
""",
    "prompts": [
        _court("Crown Prince Wei leading soldiers through Chang'an streets during the Witchcraft Crisis. Chinese title '\u201c太子起兵\u201d' in calligraphic brush style. No heavy outlines. Ample whitespace."),
        _court("Emperor Xuan signing the edict granting the posthumous title 'Li', a conflicted expression on his face. Chinese title '\u201c定谥之难\u201d' in calligraphic brush style. No heavy outlines."),
        _court("Tomb of Crown Prince Wei being rebuilt with proper ceremony, Emperor Xuan attending. Chinese title '\u201c追尊戾园\u201d' in calligraphic brush style. No heavy outlines."),
    ]
}

T[116] = {
    "folder": "xuan-di-military",
    "article": """宣帝武功\u2014\u2014西域都护与匈奴称臣

公元前59年，汉朝在乌垒城（今新疆轮台）设立了西域都护府。这是中国历史上中央政府第一次在西域设立常驻行政机构。标志着天山南北三十六国正式纳入汉朝版图。

第一任西域都护叫郑吉。这个人的履历很有意思\u2014\u2014他是宣帝从基层一步步提拔上来的实干派。郑吉没有霍去病那样的骑兵天才，也不会写诗，但他把三十六国的使节、商队、驻军和驿站串联成了一张行政网络。

西域都护的权力有多大？他可以调动各国军队，裁决各国内部纠纷，管理丝绸之路上的商旅和税收。汉朝在西域的驻军人数并不多\u2014\u2014大约两千人\u2014\u2014但靠着这些小股精锐部队和灵活的外交手腕，郑吉维持了西域三十年的和平。

更让宣帝载入史册的是公元前51年呼韩邪单于的朝拜。当年的匈奴分裂为南北两部\u2014\u2014南匈奴呼韩邪被北匈奴打败，选择了臣服汉朝。宣帝在甘泉宫接见他时，赏赐了黄金二十斤、丝绸上万匹。呼韩邪的臣服具有象征意义：从白登之围到漠北决战，再到单于亲自朝拜，汉匈战争终于画上了句号。

宣帝为此改元\u201c甘露\u201d\u2014\u2014上天降下的甘甜雨露。没有武力的炫耀，没有封禅的排场，只是一个务实的皇帝和一个务实的单于，在甘泉宫里达成了和平。

武帝用五十年没完成的事，宣帝在二十年间做完了。#西域都护 #呼韩邪 #汉宣帝 #郑吉
""",
    "prompts": [
        _military("Zheng Ji accepting the Western Regions protectorate seal at Wulei City, 36 kingdom envoys present. Chinese title '\u201c西域都护\u201d' in calligraphic brush style. No heavy outlines. Ample whitespace."),
        _military("Huhanye Chanyu kneeling before Emperor Xuan at Ganquan Palace, gifts of gold and silk. Chinese title '\u201c单于朝拜甘露年\u201d' in calligraphic brush style. No heavy outlines."),
        _daily("Silk Road caravan passing through a Han garrison post in the Western Regions. Chinese title '\u201c丝路安宁\u201d' in calligraphic brush style. No heavy outlines."),
    ]
}

T[117] = {
    "folder": "xuan-di-domestic",
    "article": """宣帝仁政\u2014\u2014廷尉平、常平仓与天下殷富

宣帝对内政的治理，有一套很实在的逻辑：法律要公道，粮食要便宜，官员要廉洁。

他刚即位就发现了一个严重问题：地方官判案太随意。同样一个案子，在这个县判死罪，在邻县判无罪。宣帝下令设立\u201c廷尉平\u201d\u2014\u2014相当于最高法院巡回法官，每年到各地复核死刑案件。冤假错案被纠正了一大批。史载宣帝在位的二十五年中，廷尉平一共复核了两万多件案子，其中改判无罪的超过四千件。

粮食政策是宣帝的另一项创举。他采纳了耿寿昌的建议，在边郡设立\u201c常平仓\u201d。丰年粮价低，国家高于市场价收购；荒年粮价飞涨，国家低于市场价抛售。这不是慈善\u2014\u2014国家通过差价赚了钱，老百姓也吃得起饭。

常平仓制度一直沿用了两千年。直到清朝，各省的粮仓运转逻辑都还是宣帝那套。

经济数据最能说明问题。宣帝末年，西汉在籍人口突破五千万，比武帝时期整整多了一千五百万。谷价跌到了历史最低\u2014\u2014宣帝中期长安一石谷仅五钱，连武帝时期的十分之一都不到。

一个从监狱里活下来的孩子，一个在街头混大的少年，成了西汉最会管家的皇帝。他不追求功盖万世，他只追求一件事：让治下的百姓吃得起饭、喊得了冤、活得下去。#汉宣帝 #廷尉平 #常平仓 #孝宣之治
""",
    "prompts": [
        _court("Imperial judge reviewing death penalty cases at a local court, prison gates open behind. Chinese title '\u201c廷尉平冤\u201d' in calligraphic brush style. No heavy outlines. Ample whitespace."),
        _daily("Commoners buying grain at a Changping Granary, prices posted on a board. Chinese title '\u201c常平仓籴\u201d' in calligraphic brush style. No heavy outlines."),
        _daily("Han marketplace scene, abundant food displays, cheerful merchants. Chinese title '\u201c天下殷富\u201d' in calligraphic brush style. No heavy outlines."),
    ]
}

T[118] = {
    "folder": "two-grassroots-emperors",
    "article": """两位草根皇帝\u2014\u2014汉宣帝与唐宣宗

中国历史上有一个很有趣的巧合：两个被称为\u201c宣\u201d的皇帝，都是从底层爬上来的。

汉宣帝刘询（初名刘病已），襁褓中入狱，五岁寄人篱下，十几岁在长安街头混日子。唐宣宗李忱，因为母亲是宫女，从小被皇室和太监瞧不起，装傻装了三十六年，直到四十岁才被推上皇位。

两个人上位后的施政方向惊人地相似。

第一，都重法度。汉宣帝从小就见过监狱里的黑暗，所以他特别重视法律公正。唐宣宗在宫里见惯了太监弄权，所以他登基后第一件事就是整顿司法，所有案件必须走正规程序，不许太监插手。

第二，都轻徭薄赋。汉宣帝把田赋降到三十税一，唐宣宗把盐税减了一半。两个人都明白底层百姓的命门在哪\u2014\u2014太重的税是要出人命的。

第三，都善用人才。汉宣帝有丙吉、郑吉、张敞、韩延寿。唐宣宗有令狐绹、白敏中\u2014\u2014都是实干派。宣宗很讨厌\u201c虚名之士\u201d，谁的名声太大他反而不信任。这一点跟汉宣帝的\u201c霸王道杂之\u201d如出一辙。

最让历史学家感慨的是：两个王朝都在他们的治下出现了\u201c中兴\u201d，但也都只是回光返照。汉宣帝死后，元帝即位，西汉开始走下坡路。唐宣宗死后，懿宗即位，二十年后唐朝就灭亡了。

草根皇帝最大的困境，不是自己不会当皇帝\u2014\u2014而是自己的儿子不会继承这份来自泥土的智慧。#汉宣帝 #唐宣宗 #草根皇帝 #大中之治
""",
    "prompts": [
        _court("Han Xuan Di young in street clothes among commoners in Chang'an marketplace. Chinese title '\u201c汉宣帝微时\u201d' in calligraphic brush style. No heavy outlines. Ample whitespace."),
        _court("Tang Xuanzong (Li Chen) pretending to be foolish in the palace as a young man. Chinese title '\u201c唐宣宗装傻\u201d' in calligraphic brush style. No heavy outlines."),
        _court("Two emperor portraits side by side in ink wash style. Chinese title '\u201c双宣并立\u201d' in calligraphic brush style. No heavy outlines."),
    ]
}

T[119] = {
    "folder": "wang-zhengjun-entry",
    "article": """王政君入宫\u2014\u2014随手一指改变西汉国运

公元前53年，一个叫王政君的十八岁女子被送入太子宫。她的命运转折点，来自一个极其偶然的动作。

太子刘奭（后来的汉元帝）当时正为宠妃司马良娣的死伤心，拒绝亲近任何女人。他爹宣帝和刘皇后急了\u2014\u2014太子无子，这是大事。皇后选了五个宫女，让太子从中挑一个。

太子心不在焉，随手一指：\u201c这个可以。\u201d

他指的是坐在最边上的一个，穿着朴素的绛色衣服，低着头不敢看人。她叫王政君。

这一指，改变了西汉的历史。王政君当晚就怀孕了，生下了一个儿子\u2014\u2014后来的汉成帝刘骜。王政君因此被立为太子妃。元帝即位后她成了皇后。成帝即位后她成了皇太后。

王政君的家族从此飞黄腾达。她的兄弟王凤当了大将军，王家子弟布满朝廷。她有一个侄子，叫王莽\u2014\u2014后来篡了汉朝。

司马光在《资治通鉴》里写下了一段意味深长的评论：王政君入宫，完全是一个偶然。如果不是太子随手一指，如果没有那个夜晚，如果生的是女儿\u2014\u2014西汉的历史可能就是另一个走向。

一个女人的命运改变了一个王朝的命运。而改变她命运的，只是太子无心的一指。#王政君 #汉元帝 #王莽 #西汉灭亡
""",
    "prompts": [
        _court("Five palace women sitting in a row, young Prince Shi looking away and pointing casually. Chinese title '\u201c随手一指\u201d' in calligraphic brush style. No heavy outlines. Ample whitespace."),
        _court("Wang Zhengjun holding her newborn son in the palace, Empress Dowager visiting. Chinese title '\u201c得子立妃\u201d' in calligraphic brush style. No heavy outlines."),
        _court("A mature Wang Zhengjun as Grand Empress Dowager, surrounded by Wang family officials including young Wang Mang. Chinese title '\u201c王氏专权\u201d' in calligraphic brush style. No heavy outlines."),
    ]
}

T[120] = {
    "folder": "yuan-di-decline",
    "article": """乱我家者太子也\u2014\u2014汉元帝如何败光家底

汉元帝刘奭是宣帝的儿子，从小在深宫长大。他跟他爹完全是两个物种\u2014\u2014宣帝务实、精明、懂民间疾苦；元帝柔情、好儒、满脑子理想主义。

宣帝活着时就说过一句著名的话：\u201c乱我家者，太子也！\u201d\u2014\u2014搞乱我刘家天下的，就是这太子。他几次想换太子，但因为刘奭是许平君的儿子\u2014\u2014宣帝最爱的女人生的\u2014\u2014下不了手。

元帝即位后，把宣帝那一套全推翻了。宣帝是\u201c霸王道杂之\u201d，元帝是\u201c纯任德教\u201d\u2014\u2014全用儒家道德治国。听起来很好，做起来一团糟。

他把权力从尚书台拿出来分给宦官。为什么？因为宦官没家族背景，不会变成霍光第二。但他忘了：宦官虽然没有家族，但宦官有帮派。中书令石显、仆射牢梁、少府五鹿充宗三人结成了\u201c中书帮\u201d，把持朝政二十年。石显权势之大，连丞相都要看他的脸色。

元帝在位的十六年中，西汉国力急转直下。常平仓没人管了，廷尉平取消了，西域都护府的后勤支持被砍了一大半。北方的匈奴虽然没打过来，但西羌叛乱了。汉朝跟西羌打了两仗，耗费军费四十亿钱\u2014\u2014一个宣帝时代积累下来的家底，被元帝十六年花掉了大半。

元帝死后，成帝即位。王政君成了太后，王氏外戚正式登台。西汉的结局，从宣帝说\u201c乱我家者太子也\u201d那一刻就已经写好了。#汉元帝 #石显 #宣帝 #西汉衰落
""",
    "prompts": [
        _court("Emperor Yuan reading Confucian classics, ignoring administrative scrolls piled up on his desk. Chinese title '\u201c纯任德教\u201d' in calligraphic brush style. No heavy outlines. Ample whitespace."),
        _court("Eunuch Shi Xian receiving memorials at the palace gate, officials bowing to him. Chinese title '\u201c中书弄权\u201d' in calligraphic brush style. No heavy outlines."),
        _military("Han soldiers fighting the Western Qiang rebellion, a general tallying war expenses. Chinese title '\u201c西羌糜饷\u201d' in calligraphic brush style. No heavy outlines."),
    ]
}

T[121] = {
    "folder": "zhaojun-heqin",
    "article": """昭君出塞\u2014\u2014冷宫惊艳与塞外六十年和平

公元前33年，匈奴呼韩邪单于第三次来长安朝拜。这一次，他提出了一个请求：愿做大汉女婿，迎娶汉朝公主。

元帝不想派真公主去\u2014\u2014以前的细君公主嫁到乌孙，在草原上过了一辈子。他让内侍去后宫传话：愿意嫁到匈奴的，朕把她当公主嫁出去。

后宫佳丽三千，没人想去。只有一个人站出来：王昭君。

王昭君入宫五年了，从未见过皇帝一面\u2014\u2014后宫的宫女太多，皇帝只有翻到画像才会召见。昭君没钱贿赂画师毛延寿，毛延寿在她的画像上点了一颗\u201c克夫痣\u201d。元帝看到画像就把她的名字划掉了。

五年了，她连皇帝长什么样都不知道。去匈奴，至少比老死在冷宫里强。

临行那天，元帝设宴送别。王昭君盛装出殿\u2014\u2014这是她第一次以妃子的身份站在皇帝面前。元帝看得呆住了：眼前这个女人是他见过最美的女子，端庄大方、明眸皓齿。他的目光扫向那幅画像\u2014\u2014毛延寿当场被拖出去砍了。

但一切已经无法挽回。王昭君嫁给了呼韩邪，生下了两个儿子。呼韩邪死后，按照匈奴的收继婚习俗，她又嫁给了呼韩邪的长子复株累单于，又生了两个女儿。

昭君出塞换来了汉匈之间六十年的和平。长安和草原之间，再也没有流过血。她在漠北草原生活了三十三年，死后葬在今天的呼和浩特。据说每到秋天，塞外草原上的草都枯黄了，只有她的坟头上始终长着青草。人们管它叫\u201c青冢\u201d。#王昭君 #昭君出塞 #呼韩邪 #汉匈和平
""",
    "prompts": [
        _daily("Wang Zhaojun in plain palace dress, looking at a portrait being painted by Mao Yanshou. Chinese title '\u201c画师点痣\u201d' in calligraphic brush style. No heavy outlines. Ample whitespace."),
        _court("Wang Zhaojun in full ceremonial dress walking before Emperor Yuan, everyone stunned by her beauty. Chinese title '\u201c惊艳临辞\u201d' in calligraphic brush style. No heavy outlines."),
        _daily("Wang Zhaojun on horseback on the grassland, wearing Xiongnu clothing, Huhanye beside her. Chinese title '\u201c青冢千秋\u201d' in calligraphic brush style. No heavy outlines."),
    ]
}

T[122] = {
    "folder": "xuandi-xiongnu",
    "article": """宣帝平匈奴\u2014\u2014为何完成武帝没实现的伟业

汉武帝打了五十年，把匈奴打得远遁漠北，但始终没能让匈奴单于低头称臣。宣帝没打什么大仗，匈奴单于却自己跑来长安朝拜了。为什么？

答案很简单：内部瓦解比外部征伐更致命。

公元前60年，匈奴虚闾权渠单于死后，内部为了争单于位发生了长达数年的内乱。五单于争立\u2014\u2014五个自称单于的人互相砍杀。最后剩下的两个：呼韩邪单于和他的哥哥郅支单于。

郅支打败了呼韩邪。呼韩邪往南跑，一直跑到汉朝的边境线上。他派儿子到长安做人质，请求汉朝庇护。

宣帝没有派大军出塞，而是做了三件事：第一，在边境囤积粮草，表明汉朝随时可以支援呼韩邪；第二，送呼韩邪一个大印，承认他是南匈奴的合法单于；第三，让郑吉在西域牵制郅支的后方。

这三件事没有一件是战争行为，但每一件都是对呼韩邪的政治背书。公元前51年，呼韩邪带着全套匈奴仪仗走进了甘泉宫，向宣帝行了藩臣之礼。

武帝用刀剑没做到的事，宣帝用粮仓和大印做到了。没有一兵一卒出塞，但匈奴问题彻底解决了。#汉宣帝 #匈奴 #呼韩邪 #不战而屈人之兵
""",
    "prompts": [
        _military("Five Xiongnu chanyu fighting each other on the steppe, divided tribal banners. Chinese title '\u201c五单于争立\u201d' in calligraphic brush style. No heavy outlines. Ample whitespace."),
        _court("Huhanye Chanyu arriving at the Han border with his family, requesting sanctuary. Chinese title '\u201c呼韩邪投汉\u201d' in calligraphic brush style. No heavy outlines."),
        _court("Emperor Xuan granting Huhanye the seal and official recognition at Ganquan Palace. Chinese title '\u201c甘露受封\u201d' in calligraphic brush style. No heavy outlines."),
    ]
}

T[123] = {
    "folder": "chengdi-liuao",
    "article": """成帝刘骜\u2014\u2014死在温柔乡的亡国之君

成帝刘骜是西汉第九位皇帝。他接手时，西汉还算强盛；他死的时候，西汉已经开始崩塌。他在位的二十六年只做了一件事\u2014\u2014溺死在赵飞燕和赵合德的温柔里。

赵飞燕是个舞女，身材极轻，据说能在人手掌上跳舞\u2014\u2014这就是\u201c掌上飞燕\u201d的由来。她的妹妹赵合德比她更美，肌肤如雪，体态丰腴。成帝把姐妹俩一起接进了宫，从此再也没出来。

两个赵氏姐妹把成帝牢牢控制在手心里。她们自己生不出孩子，也不让别的嫔妃生。许美人怀孕了，成帝知道后不敢声张，偷偷让太医去看，把生下的男婴送了人\u2014\u2014后来还是被赵氏姐妹逼死了。后宫若有女子怀孕，赵合德直接派人去处理，成帝除了哭，什么都不敢做。

成帝平时不上朝，不批奏折。他把国事全交给了王家的外戚\u2014\u2014王凤、王商、王根、王立\u2014\u2014王政君的兄弟们。王家子弟遍布朝野，成了比霍光还大的势力。

公元前7年，四十五岁的成帝在赵合德的床上暴毙。史书记载他\u201c精尽而亡\u201d\u2014\u2014不是夸张，是真的死在了女人的身体上。

赵合德被大臣们逼问致死，赵飞燕被废为庶人后自杀。但成帝的死改变不了已经铸成的局面\u2014\u2014王氏外戚已经彻底把持了朝政。他爹元帝花了十六年败光家底，他花了二十六年把剩下的全烧了。#汉成帝 #赵飞燕 #赵合德 #王氏外戚
""",
    "prompts": [
        _court("Zhao Feiyan dancing on a bronze tray, Emperor Cheng watching mesmerized. Chinese title '\u201c掌上飞燕\u201d' in calligraphic brush style. No heavy outlines. Ample whitespace."),
        _court("Zhao Hede with exquisite beauty, Emperor Cheng kneeling before her, pleading. Chinese title '\u201c温柔困龙\u201d' in calligraphic brush style. No heavy outlines."),
        _court("Emperor Cheng dead on the bed, Zhao Hede in panic, officials breaking into the chamber. Chinese title '\u201c精尽人亡\u201d' in calligraphic brush style. No heavy outlines."),
    ]
}

T[124] = {
    "folder": "chengdi-absurd",
    "article": """成帝离谱事\u2014\u2014微服私访到荒诞无度

成帝不只在后宫荒唐，他在宫外也留下了大量离谱的故事。

他跟富平侯张放关系暧昧。两人经常穿着平民的衣服，从皇宫侧门溜出去，到长安城的各个角落夜游。张放给成帝介绍各种奇人：斗鸡的、耍蛇的、变戏法的。成帝觉得新鲜，每次都玩到深夜，然后让张放背着他从侧门翻墙回宫。

有一次，成帝微服到渭河边喝酒，跟一群市井无赖打了一架。堂堂大汉天子鼻青脸肿地回了宫，对太监说：\u201c别告诉太后。\u201d

张放仗着皇帝的宠信，在长安城里无法无天。他不但欺男霸女，还跟人争风吃醋杀了人。御史大夫弹劾张放，成帝舍不得杀他，只把他赶出了京城。张放一走，成帝天天哭，给他写信，又把他的官职升了。

还有一回，成帝在宫里闷得发慌，让太监扮成强盗在御花园里抢劫，然后他亲自带人\u201c追捕\u201d，玩官兵抓强盗的游戏。大臣们面面相觑，但又不敢说。

最离谱的事跟赵氏姐妹相关。赵合德洗澡时满室生香，成帝偷偷挖了个洞偷看。赵合德喷水溅到他脸上，他开心得不得了。赵飞燕送他一种春药叫\u201c慎恤胶\u201d，成帝一次吃七粒，最后暴毙在床上。

一个皇帝荒唐到这个地步，西汉怎么可能不亡？#汉成帝 #张放 #赵飞燕 #赵合德
""",
    "prompts": [
        _court("Emperor Cheng in commoner clothes sneaking through a palace side door with Zhang Fang. Chinese title '\u201c微服夜游\u201d' in calligraphic brush style. No heavy outlines. Ample whitespace."),
        _daily("Emperor Cheng in tavern on Wei River, getting into a fight with commoners. Chinese title '\u201c天子斗殴\u201d' in calligraphic brush style. No heavy outlines."),
        _court("Zhao Hede bathing in a fragrant bath, Emperor Cheng peeking through a hole in the wall. Chinese title '\u201c偷窥香汤\u201d' in calligraphic brush style. No heavy outlines."),
    ]
}

T[125] = {
    "folder": "aidi-liuxin",
    "article": """哀帝刘欣\u2014\u2014断袖之癖与七年折腾

成帝死后无子，皇位传给了他的侄子刘欣，史称汉哀帝。哀帝在位七年，最出名的一件事是\u201c断袖之癖\u201d，但他留给西汉的遗产远不止这个八卦。

哀帝即位时才十八岁，年轻气盛，想做一番大事业。他干的第一件事就是\u201c限田限奴\u201d\u2014\u2014他认为土地兼并太严重，应该限制所有人占有的土地和奴隶数量。贵族们炸了锅。诏书还没实施，就被以王政君为首的外戚集团联手压了下去。

哀帝又试图削夺王氏外戚的权力。他把王莽赶出了首都，让王莽回封地养老。王家的子弟被一个个调离要害部门。但哀帝自己的外戚\u2014\u2014丁家和傅家\u2014\u2014迅速顶上，成了新一代权贵。刚从王氏的锅里捞出来，又掉进了丁傅的油锅。

哀帝也很怕死，天天让方士炼丹求仙。结果其中一个方士说他\u201c不宜久居宫中\u201d，他就真的搬出皇宫住到了上林苑。一个皇帝被方士忽悠得不敢回自己的宫殿。

他的断袖故事更广为人知\u2014\u2014宠臣董贤跟他同寝，有一次哀帝先醒了，发现衣袖被董贤压住。为了不惊醒董贤，哀帝用剑割断了自己的衣袖。从此有了\u201c断袖之癖\u201d这个成语。

哀帝把董贤从一个十几岁的美少年提拔为大司马，位列三公之首。满朝文武跪在一个比自己儿子还小的漂亮男孩面前。

公元前1年，二十五岁的哀帝病逝，没有子嗣。他折腾了七年，限田限奴没搞成，王氏外戚没打倒，只留下了一段断袖的传说和一个彻底空了的国库。#汉哀帝 #断袖之癖 #董贤 #限田令
""",
    "prompts": [
        _court("Young Emperor Ai signing an edict to restrict land ownership, noble palace opposition. Chinese title '\u201c限田令\u201d' in calligraphic brush style. No heavy outlines. Ample whitespace."),
        _court("Emperor Ai cutting his sleeve to avoid waking Dong Xian, tender scene. Chinese title '\u201c断袖\u201d' in calligraphic brush style. No heavy outlines."),
        _court("Dong Xian at 20 years old receiving the Grand Marshal seal, older officials kneeling. Chinese title '\u201c少年大司马\u201d' in calligraphic brush style. No heavy outlines."),
    ]
}

T[126] = {
    "folder": "dongxian-rise-fall",
    "article": """董贤\u2014\u2014断袖男友的暴富与惨死

董贤是中国历史上最传奇的\u201c宠臣\u201d之一。从一个十几岁的美少年到三公之首只用了三年，从三公之首到自杀也只用了三年。

董贤是哀帝的太子舍人，负责在殿上传报时间。哀帝第一次见到他时，被他的容貌惊住了\u2014\u2014史书记载董贤\u201c性柔和\u201d\u201c美姿仪\u201d，长得比女人还好看。哀帝把他叫到面前，当天就封为驸马都尉侍中，跟他同吃同住。

董贤的升官速度极其夸张：二十二岁封为大司马、卫将军，位在三公之上。哀帝把国库里的钱大量赏给他\u2014\u2014董家的宅子跟皇宫一样大，董贤自己的俸禄是年两千万钱，相当于大国丞相的二十倍。董贤的父亲董恭被封为少府，岳父被封为将作大匠，连董家的仆人都有官职。

有一次哀帝在宴会上笑着说：\u201c朕要在自己万年之后，把皇位禅让给董贤。\u201d\u2014\u2014这可能是中国历史上第一次有皇帝想把皇位传给自己的男朋友。

哀帝死后，王政君以太皇太后的身份召见王莽入宫主政。王莽做的第一件事就是弹劾董贤\u2014\u2014\u201c无功德而居大位，天下不服。\u201d董贤在朝会上被当场解除大司马印绶，被赶回自己的宅子。

当天晚上，董贤和妻子抱头痛哭，一同自杀了。王莽让人验尸确认后，将董贤的尸体以平民之礼草草掩埋。为了防止董贤的坟被盗，连墓碑都没立。

从极盛到极惨，前后不到六年。权力不来源于自身能力时，从来都是借来的\u2014\u2014终归要还。#董贤 #汉哀帝 #王莽 #宠臣
""",
    "prompts": [
        _court("Young Dong Xian in palace uniform, Emperor Ai staring at him. Chinese title '\u201c惊为天人\u201d' in calligraphic brush style. No heavy outlines. Ample whitespace."),
        _court("Dong Xian receiving the Grand Marshal seal at age 22, ministers' jealous gazes. Chinese title '\u201c二十二岁大司马\u201d' in calligraphic brush style. No heavy outlines."),
        _court("Dong Xian and his wife weeping before suicide, the grand mansion deserted behind them. Chinese title '\u201c草席葬身\u201d' in calligraphic brush style. No heavy outlines."),
    ]
}

T[127] = {
    "folder": "wangmang-humble",
    "article": """王莽谦恭未篡时\u2014\u2014道德圣人的伪装

白居易有一句诗：\u201c王莽谦恭未篡时。\u201d\u2014\u2014王莽在没篡位之前，谦恭得像个圣人。

王莽的出身并不差\u2014\u2014他是王政君的侄子，王家是当时最显赫的外戚家族。但王家的子弟们全都在长安斗富比阔，只有王莽一个人过着苦行僧般的生活。他穿着粗布衣服，骑着劣马，住着破房子。他把俸禄全拿出来分给门客和穷人。

他的长子王获杀了一个奴婢，王莽逼着王获自杀偿命。这件事传遍了长安\u2014\u2014连王家的子弟都对自己的奴婢这么好，王莽真是个\u201c大善人\u201d。

公元前8年，王莽被任命为大司马。他上任后第一件事就是把自己的俸禄拿出来救济灾民。遇到蝗灾，他带头吃素，还上书太后请求减薪。全国百姓都被感动了，联名上书要求给王莽加薪。

但这一切都是完美的表演。王莽的目标很明确：按照霍光的剧本，一步不差地走向权力巅峰。

他做了四件事来塑造自己的圣人形象：第一，生活简朴到极致，穿得像个教书先生；第二，礼贤下士，对所有人彬彬有礼；第三，严于律己，儿子杀了人他让儿子偿命；第四，打击政敌毫不手软。

王莽的谦恭不是品德，是策略。当所有人都觉得你是圣人的时候，皇帝的位置就不那么遥不可及了。#王莽 #霍光 #权力游戏 #西汉末年
""",
    "prompts": [
        _daily("Wang Mang in coarse cloth eating plain food while his cousin feasts in silk behind him. Chinese title '\u201c粗衣粝食\u201d' in calligraphic brush style. No heavy outlines. Ample whitespace."),
        _court("Wang Mang forcing his son to commit suicide for killing a servant, dramatic scene. Chinese title '\u201c杀子偿命\u201d' in calligraphic brush style. No heavy outlines."),
        _daily("People kneeling to Wang Mang, begging him to accept a higher salary. Chinese title '\u201c万民请愿\u201d' in calligraphic brush style. No heavy outlines."),
    ]
}

T[128] = {
    "folder": "pingdi-liukan",
    "article": """平帝刘衎\u2014\u2014九岁傀儡与王莽的最后一步

公元前1年，九岁的刘衎被立为皇帝，史称汉平帝。他是中国历史上最小的皇帝之一\u2014\u2014一个连自己的名字都不会写的孩子，被推上了龙椅。

王莽此时已经从大司马升为了\u201c安汉公\u201d\u2014\u2014一个专门为他创造的爵位，高于所有诸侯王。平帝即位后，王莽独揽朝政，皇帝不过是个盖章的工具人。

公元元年，王莽更进一步，被封为\u201c宰衡\u201d\u2014\u2014\u201c宰\u201d是丞相，\u201c衡\u201d是太傅。两个最高官职合到他一个人身上。

平帝慢慢长大了。十四岁时，他开始表现出不满\u2014\u2014王莽专权，他连自己的老师都见不到。有人告诉王莽：皇帝最近在私下抱怨，说安汉公太专横了。

公元5年冬天，平帝生病了。王莽亲自去探病，端上一碗药。平帝喝了药，第二天就死了。史书上说平帝是\u201c病逝\u201d，但《资治通鉴》白纸黑字地记录：平帝是被王莽毒死的。

平帝死后，王莽从刘氏宗族中选了一个两岁的婴儿做皇帝，史称孺子婴。两岁的孩子当皇帝干什么？王莽替他干。

一年后，王莽把\u201c摄皇帝\u201d改成了\u201c假皇帝\u201d。再过一年，\u201c假皇帝\u201d变成了\u201c真皇帝\u201d。

西汉从高祖刘邦建国（公元前202年）到平帝之死（公元5年），共历十二帝，延续了两百零七年。一个九岁登基的傀儡皇帝，成了西汉的最后一位真皇帝。#汉平帝 #王莽 #安汉公 #孺子婴
""",
    "prompts": [
        _court("Nine-year-old Emperor Ping being crowned, Wang Mang standing behind the throne. Chinese title '\u201c九岁登基\u201d' in calligraphic brush style. No heavy outlines. Ample whitespace."),
        _court("Wang Mang visiting the sick Emperor Ping, handing him a bowl of medicine. Chinese title '\u201c药中藏机\u201d' in calligraphic brush style. No heavy outlines."),
        _court("Wang Mang kneeling before a 2-year-old Ruzi Ying, but actually holding all power. Chinese title '\u201c摄皇帝\u201d' in calligraphic brush style. No heavy outlines."),
    ]
}

T[129] = {
    "folder": "wangmang-usurp-five",
    "article": """王莽篡汉五步走\u2014\u2014温水煮青蛙式夺权

王莽从大司马到皇帝，走了五步。每一步都有名义，每一步都没遇到有组织的反抗。他完美复刻了霍光的路线，然后走得更远。

第一步：安汉公（公元1年）。平帝即位，王莽被封为\u201c安汉公\u201d\u2014\u2014名义上是辅政大臣，实际上掌握了所有朝政。老百姓只知有王莽，不知有皇帝。

第二步：宰衡（公元3年）。王莽兼任丞相和太傅，百官之首。他的女儿嫁给了平帝做皇后，王莽成了国丈。此时他的声望达到了巅峰\u2014\u2014全国近五十万人上书请求给他加九锡。

第三步：摄皇帝（公元6年）。平帝被毒死后，王莽立两岁的刘婴为帝，自己以\u201c摄皇帝\u201d的身份理政。他穿天子的衣服，住天子的宫殿，批天子的奏折，唯一不同就是不叫皇帝。

第四步：假皇帝（公元8年）。王莽把\u201c摄\u201d字去掉，直接自称\u201c假皇帝\u201d\u2014\u2014代理皇帝。刘家的宗室终于有人反应过来了，起兵反抗。刘崇（安众侯）、翟义（丞相）先后起兵，但都被迅速镇压。民间对王莽的支持度太高了\u2014\u2014百姓宁可相信一个圣人，也不相信那些姓刘的。

第五步：真皇帝（公元9年）。王莽逼迫孺子婴禅让。他让人造了一个\u201c天命\u201d\u2014\u2014在挖井时发现一块石头，上面刻着\u201c告安汉公莽为皇帝\u201d。王莽在未央宫举行了禅让大典，从刘婴手中接过了传国玉玺。

西汉亡了。王莽坐在龙椅上，准备开始他的理想国建设。他不知道自己已经站在了中国历史上最大一场社会实验的起点\u2014\u2014这场实验的名字叫新政，结局叫全面崩溃。#王莽 #禅让 #摄皇帝 #新朝
""",
    "prompts": [
        _court("Wang Mang receiving the Nine Bestowments, ceremonial scene with officials. Chinese title '\u201c加九锡\u201d' in calligraphic brush style. No heavy outlines. Ample whitespace."),
        _court("Wang Mang in emperor's clothes but titled 'Acting Emperor', the boy emperor nearby. Chinese title '\u201c假皇帝\u201d' in calligraphic brush style. No heavy outlines."),
        _court("Wang Mang receiving the imperial seal from young Liu Ying in the abdication ceremony. Chinese title '\u201c禅让大典\u201d' in calligraphic brush style. No heavy outlines."),
    ]
}

T[130] = {
    "folder": "wangmang-reforms",
    "article": """王莽魔幻改革\u2014\u2014书呆子如何毁了一个帝国

公元9年，王莽建立了新朝。他坐在龙椅上，翻开《周礼》，开始了中国历史上最疯狂的社会改革实验。

他改革的第一项叫\u201c王田制\u201d\u2014\u2014土地全部收归国有，按一夫一妇百亩的标准重新分配给农民。禁止土地买卖。听起来很美好，但他没考虑到全国的土地测量、人口登记需要多少行政力量。命令发下去，三年了，连长安城外的地都没量清楚。

第二项叫\u201c五均六筦\u201d\u2014\u2014国家控制物价、贷款、盐铁酒专卖、铸币权、征税、山林川泽。这是桑弘羊国家资本主义的激进升级版。执行这些政策的官员全是王莽的亲戚和亲信，他们一边替国家收钱，一边往自己兜里揣。

第三项叫货币改革。王莽在短短十年里改了五次货币\u2014\u2014从五铢钱改成大泉五十，又改成契刀五百，又改成宝货制，把二十多种贝壳、龟甲、布帛全变成了法定货币。老百姓刚习惯了一种钱，王莽又推翻了重来。每一次改钱都是在洗劫民间的财富。

第四项叫\u201c改官制地名\u201d。王莽把全国的地名全改了\u2014\u2014郡名、县名、官名、爵位名全部照搬《周礼》。官员们连自己的印信上都搞不清楚写的是什么职务。地名一改再改，公文快递都送不到正确的地方。

短短十几年，全国民不聊生。公元17年，绿林军起义。公元22年，赤眉军起义。公元23年，王莽被杀于未央宫，他的头被割下来传遍天下。

一个书呆子试图用《周礼》建造乌托邦，结果造了一个地狱。#王莽 #王田制 #五均六筦 #货币改革 #新朝
""",
    "prompts": [
        _daily("Wang Mang reading Zhouli in the palace while outside farmers struggle with land reform. Chinese title '\u201c王田令\u201d' in calligraphic brush style. No heavy outlines. Ample whitespace."),
        _daily("Five different types of Wang Mang's coins on a table, confused merchants arguing. Chinese title '\u201c五改货币\u201d' in calligraphic brush style. No heavy outlines."),
        _military("Green Woods Army rebels storming Chang'an, Wang Mang fleeing in the palace. Chinese title '\u201c未央终局\u201d' in calligraphic brush style. No heavy outlines."),
    ]
}

T[131] = {
    "folder": "wangmang-no-usurp",
    "article": """王莽若不篡汉\u2014\u2014中国为何走不出日本幕府路线

历史爱好者常问一个问题：为什么中国历史上权臣遍地，但没有一个建立了日本幕府那种长期稳定的武家政权？霍光比德川家康的权力还大，为什么霍家只传了二代就被连根拔起？

根源在于中国有一个日本没有的制度\u2014\u2014嫡长子继承制。日本天皇的继承权经常模糊不清，给了幕府将军\u201c代天皇执政\u201d的空间。中国从周朝开始就确立了嫡长子继承制，谁是合法的继承人，所有人都知道。你权臣再大，名义上你只是\u201c辅佐\u201d，不能\u201c取代\u201d。

王莽能篡汉成功，不是因为他权力大，而是因为汉朝的嫡系血脉\u2014\u2014从元帝开始\u2014\u2014已经连续三代绝嗣。昭帝无子、成帝无子、哀帝无子、平帝有子被毒死。连续四代皇帝没有留下合法的成年继承人，这在任何王朝都是致命的。

假设王莽没有篡汉，而是像霍光一样\u201c辅政\u201d而终，孺子婴长大后再还政\u2014\u2014汉朝的血脉会继续延续，但后世的权臣们仍然会走同样的路。只要皇权专制的框架不变，权臣政治就会周期性出现。

王莽给了后世一个冷酷的启示：当旧制度的漏洞大到一定程度时，一定会有人去捅破它。与其怪王莽是伪君子，不如怪西汉后期的皇帝们自己把江山拱手让人。#王莽 #幕府 #嫡长子继承 #禅让
""",
    "prompts": [
        _court("Diagram comparing Chinese imperial succession (clear lines) vs Japanese imperial succession (dotted lines) in ink style. Chinese title '\u201c继承之异\u201d' in calligraphic brush style. No heavy outlines. Ample whitespace."),
        _court("Huo Guang in Han court vs Tokugawa Ieyasu in Edo castle, side by side comparison. Chinese title '\u201c权臣双雄\u201d' in calligraphic brush style. No heavy outlines."),
        _daily("Broken jade seal on a throne, four child emperor portraits fading away. Chinese title '\u201c四代绝嗣\u201d' in calligraphic brush style. No heavy outlines."),
    ]
}

T[132] = {
    "folder": "xuandi-kpi",
    "article": """宣帝大年初一KPI\u2014\u2014史上最卷年终考核

汉宣帝把\u201c年终考核\u201d玩到了极致。每年正月初一，全国各郡国的上计吏（相当于今天的CFO+COO）带着一整年的数据到长安汇报工作。宣帝亲自坐在未央宫里听汇报。

汇报不是走过场。宣帝会从早上听到晚上，问每一个郡的详细数据：今年本地人口增长了多少？开垦了多少荒地？逮捕了多少盗贼？收了多少粮食？粮价多少？

如果数据不好看，宣帝会当场追问原因。地方官说\u201c今年蝗灾\u201d，宣帝就问：蝗灾范围多少亩？朝廷拨的救济粮到了吗？赈灾款够不够？问得越细，地方官越紧张。

《汉书》里记载了一个典型案例：陈万年做地方官时，每年考核都是全国前三。宣帝把他调到了丞相府当属官。上任后第一年，丞相府的考核数据就\u2014\u2014跟往年一样，因为陈万年走后他那个郡的数据还是第一名。

宣帝最离谱的考核指标是\u201c狱空率\u201d\u2014\u2014监狱里没有在押犯人的天数。如果一个郡连续几个月监狱是空的，说明这个郡治理得当，官员可以升迁。地方官们为了刷数据，甚至把犯人提前放回家过年，等考核结束了再抓回来。

大年初一，别人家团聚过年。宣帝在未央宫里一条一条地算数据。他信不过任何人的口头汇报，他只看数字。#汉宣帝 #KPI #年终考核 #上计
""",
    "prompts": [
        _court("Emperor Xuan sitting in Weiyang Palace on New Year's Day, officials reporting with bamboo scrolls. Chinese title '\u201c正旦考绩\u201d' in calligraphic brush style. No heavy outlines. Ample whitespace."),
        _daily("Han official nervously sweating while reporting statistics, Emperor Xuan pointing at a number. Chinese title '\u201c数据追责\u201d' in calligraphic brush style. No heavy outlines."),
        _daily("Prison gate with a wooden sign reading 'Cells Empty', local officials celebrating. Chinese title '\u201c狱空率\u201d' in calligraphic brush style. No heavy outlines."),
    ]
}

T[133] = {
    "folder": "han-official-leave",
    "article": """汉代公务员福利\u2014\u2014休沐丧假与带薪探亲

很多人以为\u201c公务员周末双休\u201d是现代才有的制度。实际上，汉朝的公务员福利比不少现代企业还完善。

第一，休沐。汉朝规定官员每五天休息一天，叫\u201c休沐\u201d\u2014\u2014意思是让你回家洗头洗澡。不要笑，在那个没有热水器的年代，洗一次头是件大工程。官员们在官署里合署办公，五天才回家一次。

第二，丧假。父母去世，官员可以\u201c丁忧\u201d守孝三年。这三年是带薪的，官位保留。如果这位官员实在离不开岗位\u2014\u2014比如霍光\u2014\u2014皇帝可以\u201c夺情\u201d，强制你回来上班，但这是极少数。

第三，探亲假。官员在外地工作，每三年可以请一次\u201c归宁\u201d假，回家看望父母。往返路费由官府报销。

第四，看病假。官员生病，公家的医生免费诊治。药费也是公家的。如果病得太重，皇帝还会专门派人送药慰问。

第五，住房。京官住在官署分配的房子里，水电煤（其实就是柴火和蜡烛）都是公家出。地方官住在郡国的官舍里，不用自己租房。

宣帝时期还有一项人性化措施：夫妻双方都在官府工作的，可以\u201c并休\u201d\u2014\u2014把两个人的休沐日凑一起过个长周末。

两千年前的打工人，福利比今天还好。#汉代 #公务员 #休沐 #丁忧
""",
    "prompts": [
        _daily("Han official going home for his bath day, carrying a bundle of clean clothes. Chinese title '\u201c休沐洗头\u201d' in calligraphic brush style. No heavy outlines. Ample whitespace."),
        _daily("Han official visiting parents in another town, government courier horse. Chinese title '\u201c归宁省亲\u201d' in calligraphic brush style. No heavy outlines."),
        _court("Imperial physician diagnosing a sick official, palace medicine gifts beside them. Chinese title '\u201c公费医疗\u201d' in calligraphic brush style. No heavy outlines."),
    ]
}

T[134] = {
    "folder": "han-women-rights",
    "article": """汉代女性地位\u2014\u2014休夫改嫁与财产权

汉朝女性的社会地位，在中国古代史中是一个罕见的亮点。她们可以休夫、可以改嫁、可以继承财产、甚至可以进太学读书。

朱买臣的妻子因为丈夫穷得揭不开锅，主动提出离婚，改嫁了一个当地的小商人。这在汉代是合法的\u2014\u2014妇女有\u201c七出\u201d（丈夫可以休妻的条件），但也有\u201c三不去\u201d（妻子可以拒绝离婚的条件）。最重要的是，汉朝女性有\u201c主动提出离婚\u201d的权利，这在后世的宋明清是不可能想象的。

平阳公主先嫁曹寿，后嫁卫青。一个公主改嫁了两次，没有人觉得不妥。卓文君跟司马相如私奔\u2014\u2014对，私奔是错的，但同居后没人逼她回家。她的父亲卓王孙后来还给了她一大笔财产，因为汉朝法律规定：女性有权继承家产。

汉朝女性还有受教育权。皇后和公主们从小跟着太傅读书，不少能写诗作文。汉成帝的皇后赵飞燕虽然出身舞女，但入宫后也通过了后宫的文化考试。

最能说明问题的是财产权。汉朝法律明确规定：妻子的嫁妆全部属于妻子个人财产，丈夫无权动用。如果离婚了，妻子可以把自己的嫁妆全部带走，岳父家的遗产也由女儿继承。

从什么时候开始，女性的这些权利都消失了？从儒家礼教逐渐僵化的唐宋明清。汉朝的妇女，比她们的后代幸运得多。#汉代女性 #婚姻 #财产权 #卓文君
""",
    "prompts": [
        _daily("Han woman writing a divorce contract at a desk, her husband looking shocked. Chinese title '\u201c妻休夫\u201d' in calligraphic brush style. No heavy outlines. Ample whitespace."),
        _daily("Woman receiving property from her father, carrying a bundle of valuables. Chinese title '\u201c女承家产\u201d' in calligraphic brush style. No heavy outlines."),
        _daily("Girl studying with a teacher in a home classroom, scrolls on the table. Chinese title '\u201c女子读书\u201d' in calligraphic brush style. No heavy outlines."),
    ]
}

T[135] = {
    "folder": "xuandi-street-life",
    "article": """宣帝街溜子岁月\u2014\u2014斗鸡走马上位的平民皇帝

刘病已（后来的汉宣帝）在长安当街溜子的那几年，可能是中国皇帝里最接地气的青春。

他寄住在掖庭令张贺家，口袋里没什么钱。长安的市井生活就是他的学堂。他每天跟一群\u201c不良少年\u201d混在一起\u2014\u2014这些人中有人是斗鸡的高手，有人是跑马的好手，有人是专门帮人讨债的\u201c职业经理人\u201d。

刘病已最拿手的是斗鸡。他养了一只叫\u201c金距\u201d的斗鸡，毛色金黄，凶猛异常，据说从未输过。他用这只鸡在长安的斗鸡场上赢了不少钱。赢了钱就请大家喝酒，输了就跟人打架。

他还精通马匹鉴赏。长安西市的马贩子没有一个不认识他\u2014\u2014不是因为他有皇族身份，而是因为他挑马的眼力奇准。他能看出来哪匹马有病、哪匹马能跑长途、哪匹马是偷来的。

他跟着一群游侠学会了打架。长安的每条巷子怎么钻、哪家的狗最凶、哪个坊最晚宵禁\u2014\u2014他都一清二楚。

这段市井生活塑造了他后来的统治风格。他知道五铢钱能买多少米，知道普通老百姓过日子的难处。当上皇帝后，他废除了一项让老百姓苦不堪言的制度\u2014\u2014\u201c告缗令\u201d\u2014\u2014这是他亲身体会过的东西。

他的故事证明了一件事：在街头混过的人，当起皇帝来反而更踏实。#汉宣帝 #市井 #斗鸡 #刘病已
""",
    "prompts": [
        _daily("Young Liu Bingyi in the Chang'an marketplace, watching a cockfight with street friends. Chinese title '\u201c斗鸡少年\u201d' in calligraphic brush style. No heavy outlines. Ample whitespace."),
        _daily("Liu Bingyi examining a horse at the West Market horse fair, merchants gathered around. Chinese title '\u201c市井伯乐\u201d' in calligraphic brush style. No heavy outlines."),
        _court("Emperor Xuan on the throne remembering his street days, smiling at the contrast. Chinese title '\u201c天子忆少年\u201d' in calligraphic brush style. No heavy outlines."),
    ]
}

T[136] = {
    "folder": "han-burial-craze",
    "article": """西汉丧葬狂热\u2014\u2014厚葬到盗墓产业化

西汉是一个对\u201c死后世界\u201d极度痴迷的时代。皇帝从登基的第一天就开始修陵墓\u2014\u2014武帝的茂陵修了五十三年，每年花掉全国赋税的三分之一。

汉朝人坚信\u201c事死如事生\u201d\u2014\u2014死后要过跟生前一样的生活。所以陵墓里什么都要有：房子要仿照皇宫，家具要全套红木漆器，衣服要金缕玉衣，食物要装满几百个陶罐。

最夸张的是金缕玉衣。用上千片玉石和金丝编成一件衣服，一片玉片打磨到厚度不超过一毫米。中山靖王刘胜的金缕玉衣用了2498片玉片、1100克金丝。做一件这样的衣服，一个熟练玉匠要做整整十年。

厚葬的直接后果就是疯狂的盗墓。西汉末年，盗墓已经形成了一个完整的产业链\u2014\u2014有专门勘探的技术团队，有专门掘土的施工队，有专门销赃的地下渠道。赤眉军入长安后，第一件事就是挖了茂陵。他们光从茂陵里搬出来的金银财宝就拉了三个月的车。

东汉末年，曹操专门设立了\u201c发丘中郎将\u201d和\u201c摸金校尉\u201d\u2014\u2014官方盗墓机构，用陵墓里的陪葬品充当军饷。

汉朝人用金丝玉衣保护尸体不被侵犯，但他们没想到\u2014\u2014最吸引盗墓贼的，恰恰就是那件金丝玉衣。#厚葬 #金缕玉衣 #茂陵 #盗墓
""",
    "prompts": [
        _daily("Han craftsman assembling gold-thread jade burial suit, thousands of jade pieces laid out. Chinese title '\u201c金缕玉衣\u201d' in calligraphic brush style. No heavy outlines. Ample whitespace."),
        _daily("Tomb interior filled with pottery, bronze vessels, and lacquerware, lavish furnishings. Chinese title '\u201c事死如生\u201d' in calligraphic brush style. No heavy outlines."),
        _daily("Tomb raiders at night breaking into a Han dynasty burial mound. Chinese title '\u201c盗墓夜行\u201d' in calligraphic brush style. No heavy outlines."),
    ]
}

T[137] = {
    "folder": "han-tianren-ganying",
    "article": """天人感应\u2014\u2014蝗灾要写检讨跟老鼠打官司

董仲舒给汉武帝提了一个理论叫\u201c天人感应\u201d\u2014\u2014皇帝是天子，如果皇帝做错了事，老天爷就会降下灾异来警告你。这个理论的本意是约束皇权，但发展到了西汉中后期，变成了一整套荒诞但认真的\u201c灾害问责制\u201d。

比如蝗灾。蝗虫铺天盖地飞来吃庄稼，地方官立刻上报朝廷。皇帝的第一反应不是派兵灭蝗\u2014\u2014而是写\u201c罪己诏\u201d：检讨自己哪里做错了。宣帝写过、元帝写过、成帝写过，每一份罪己诏都写得真情实感，好像蝗虫真的是被皇帝的品德招来的。

更离谱的是跟老鼠打官司。元帝时期长安发生鼠患，太常寺（管祭祀的部门）专门成立了一个\u201c治鼠\u201d委员会\u2014\u2014不是去灭鼠，而是去\u201c审鼠\u201d。他们把抓住的老鼠送到公堂上，让法官宣读老鼠的\u201c罪状\u201d：\u201c汝等啮坏官仓，罪当死。\u201d然后判决老鼠死刑\u2014\u2014杀老鼠的行为被定性为\u201c执行判决\u201d，而不是灭鼠。

还发生过一起\u201c陨石问罪\u201d事件。成帝时期，一颗陨石砸进了皇宫。太史令立即上书弹劾丞相\u2014\u2014\u201c天降陨石于宫，丞相失德所致。\u201d丞相真的因此被免了职。

这些在今天看来非常荒谬的事，在西汉是严肃的国家制度。这套制度的积极意义是：它给了大臣们一个用\u201c天意\u201d对抗皇帝暴政的理论武器。汉武帝那么强势的人，也不敢对着\u201c蝗灾\u201d说自己没错。#天人感应 #董仲舒 #罪己诏 #灾害
""",
    "prompts": [
        _daily("Han emperor writing self-criticism edict at his desk, locust plague visible through window. Chinese title '\u201c罪己诏蝗\u201d' in calligraphic brush style. No heavy outlines. Ample whitespace."),
        _daily("Han magistrate judging a rat in court, rat on a table, officials recording. Chinese title '\u201c公堂审鼠\u201d' in calligraphic brush style. No heavy outlines."),
        _daily("Meteorite in palace courtyard, officials pointing at the chancellor accusing him. Chinese title '\u201c陨石劾相\u201d' in calligraphic brush style. No heavy outlines."),
    ]
}

T[138] = {
    "folder": "han-aesthetics",
    "article": """西汉审美\u2014\u2014野性浪漫的大国气象

西汉的美学风格，用一个词概括就是：\u201c野性浪漫\u201d。它不像宋明那样精致内敛，也不像唐代那样雍容华贵。西汉的审美有一种原始的、野蛮的、生命力爆发的冲击力。

最能代表这种风格的是霍去病墓前的石雕。马踏匈奴石雕\u2014\u2014一匹战马四蹄稳健，脚下踩着一个挣扎的匈奴士兵。马的线条粗犷豪放，没有精细的雕刻，但那股力量感扑面而来。这就是西汉审美的精髓：不求形似，只求神似。

汉代的漆器是另一绝。黑底红纹，线条流畅奔放，画的是云气纹、神兽纹、狩猎纹。长沙马王堆出土的漆器，两千多年后颜色依然鲜艳如新。

汉隶书法风格刚健有力，跟后世的楷书大不相同。汉隶的线条有波磔\u2014\u2014每一笔都带着一种向前冲的劲。传世的《张迁碑》《曹全碑》记录的不仅是文字，更是一个时代的精神气质。

汉代人喜欢大东西。未央宫周长接近十公里，长乐宫同样宏伟。上林苑方圆三万多平方米，养了来自西域的各种珍禽异兽。武帝在上林苑里打猎，一次就能猎杀上千头野兽。

这种大气的背后是自信。一个刚刚战胜了匈奴的帝国，不需要用精致来证明自己。粗犷、豪放、野性\u2014\u2014这是胜利者的审美。#西汉审美 #霍去病墓 #汉隶 #马踏匈奴
""",
    "prompts": [
        _daily("Huo Qubing tomb stone carving: a war horse trampling a Xiongnu soldier, bold rough lines. Chinese title '\u201c马踏匈奴\u201d' in calligraphic brush style. No heavy outlines. Ample whitespace."),
        _daily("Black-and-red Han lacquer ware with cloud patterns and mythical beasts, vibrant colors. Chinese title '\u201c漆器云纹\u201d' in calligraphic brush style. No heavy outlines."),
        _daily("Han dynasty official script calligraphy on a stone stele, bold brushstrokes. Chinese title '\u201c汉隶风骨\u201d' in calligraphic brush style. No heavy outlines."),
    ]
}

T[139] = {
    "folder": "han-debt-law",
    "article": """汉代老赖治理\u2014\u2014借钱不还全家抵债

现代社会人人痛恨老赖。汉朝人更痛恨\u2014\u2014他们用了最原始也最有效的手段：全家抵债。

汉朝法律对债务违约的处理非常严厉。《二年律令》规定：借了钱到期不还，债权人可以到官府起诉。官府判决后，老赖必须在三十天内还清。还不上？债权人有权把老赖的\u201c家属、奴婢、财产\u201d全部拿去抵债。

家属包括：老婆、孩子、父母。三十天一到，官府就来你家查封了。

有个著名的例子。刘邦当皇帝后，他父亲刘太公还在老家种地。刘太公年轻时有个朋友叫纪信，因为借了人钱还不上，全家被债权人拉去当了奴仆。刘太公虽然心疼纪信，但法律就是这么规定的，他也无能为力。后来纪信在荥阳之战中替刘邦去死，成了汉朝的大忠臣。但他的家人，早就因为债务成了别人的奴隶。

汉朝还有一种更极端的催债方式：让欠债人用劳动抵债。你还不钱？那就来我家干活。干一天活抵多少钱，事先谈好。很多大地主就是用这种方式，白捡了一大批\u201c自愿\u201d的劳动力。

汉武帝时期还出现了一种\u201c专业催债人\u201d\u2014\u2014游侠。游侠中有一部分专门替人讨债，他们比官府更可怕。官府还要按程序起诉，游侠直接上门\u201c讲理\u201d\u2014\u2014讲不通就动手。

汉朝人的逻辑很简单：欠债还钱，天经地义。还不上，就从你的命里还。#汉代 #债务 #老赖 #游侠催债
""",
    "prompts": [
        _daily("Han debt collector at a debtor's door, family belongings being confiscated. Chinese title '\u201c举家抵债\u201d' in calligraphic brush style. No heavy outlines. Ample whitespace."),
        _daily("Debtor working in a creditor's field, counting labor days on a tally stick. Chinese title '\u201c劳役偿债\u201d' in calligraphic brush style. No heavy outlines."),
        _daily("Han youxia (knight-errant) confronting a debtor in the marketplace, crowd watching. Chinese title '\u201c游侠催债\u201d' in calligraphic brush style. No heavy outlines."),
    ]
}

T[140] = {
    "folder": "han-traffic-law",
    "article": """长安路怒症\u2014\u2014汉代飙车党超速罚款

两千年前的长安城，已经跟今天的超级都市一样堵车了。

长安城有八街九陌一百六十个闾里，人口超过五十万。城里的主干道叫\u201c驰道\u201d，宽约五十米\u2014\u2014这比今天北京长安街还宽。但再宽的路也架不住人多。

汉朝对交通违法有详细的规定。

第一，超速。《二年律令》规定：在城内骑马或乘车超速，罚金四两。在驰道上超速，罚金加倍。如果你撞伤了人，不仅要赔医药费，还要\u201c完为城旦\u201d\u2014\u2014剃掉头发去修城墙。

第二，逆行。长安的驰道有严格的方向规定\u2014\u2014左入右出，不能逆行。逆行者同样罚金。

第三，酒驾。汉朝对酒后驾车处罚更严厉。酒驾造成事故的，直接判\u201c弃市\u201d\u2014\u2014在市场当众处死。

第四，违规使用车道。长安驰道最中间的路叫\u201c御道\u201d，只有皇帝和他的使者可以走。如果有人走错了路上了御道，罚金四两。如果是骑马上了御道\u2014\u2014罚金八两。

张敞当京兆尹（相当于长安市长）时，下大力气整治过交通。他在十字路口设置了\u201c木桩\u201d（相当于今天的人行道护栏），让人车分离。还在路口安排\u201c亭长\u201d（交警），专门疏导交通。

但张敞也犯了愁\u2014\u2014因为最难罚的人是外戚。王家子弟在长安街上纵马狂奔，谁敢拦？张敞的办法是：不拦人，拦马。他把王家的马扣了，让王家人自己来取。来人必须出示身份证件和出行许可\u2014\u2014再牛的人也得老老实实排队办手续。#汉代 #交通 #长安 #张敞
""",
    "prompts": [
        _daily("Busy Chang'an street with horse carriages, pedestrians and official chariots, ordered lanes. Chinese title '\u201c长安车马\u201d' in calligraphic brush style. No heavy outlines. Ample whitespace."),
        _daily("Han traffic warden at an intersection directing horse carriages with a wooden sign. Chinese title '\u201c亭长疏堵\u201d' in calligraphic brush style. No heavy outlines."),
        _daily("A speeding rider being stopped by officials, paying a fine at roadside. Chinese title '\u201c驰道超速罚金\u201d' in calligraphic brush style. No heavy outlines."),
    ]
}

T[141] = {
    "folder": "han-wine-policy",
    "article": """汉代酒政\u2014\u2014从禁酒令到官营酒厂到宁可醉死

汉朝对酒的态度反复横跳，堪称史上最矛盾。

开国时刘邦搞酎金律，对祭祀用酒规定了严格的标准\u2014\u2014必须是每年八月酿造的\u201c酎酒\u201d，发酵时间、原料比例都有法定标准。诸侯进贡的酎酒如果质量不合格，直接削爵。

文帝时期开始搞禁酒令。文帝的理由很淳朴：酒是用粮食酿的，太浪费了。大灾之年禁酒的诏书发了一道又一道\u2014\u2014但禁不住。长安城里偷偷卖酒的小作坊越禁越多。

武帝时期彻底放弃禁酒，改成官营垄断。公元前98年，武帝推行\u201c榷酒酤\u201d\u2014\u2014酒由官府统一生产、统一销售、统一定价，私人不许酿酒卖酒。这是中国历史上第一次\u201c国家专卖酒\u201d。

官营酒的质量极差，价格还贵。老百姓买不着好酒，就开始走私\u2014\u2014私酿酒的黑市比官营之前还热闹。

昭帝时期废除了榷酒酤，改成\u201c征税制\u201d\u2014\u2014私人可以自由酿酒卖酒，但每卖一升酒都要交税。汉书里的数据显示，仅酒税一项，全国一年能收两亿多钱。

宣帝时期更进一步，允许在特定节日\u201c大酺五日\u201d\u2014\u2014全城狂欢五天，酒随便喝。这是民间最快乐的五天\u2014\u2014你可以看到一个京兆尹和一个小贩坐在一个酒桌上划拳。

到了东汉末年，酒政完全崩溃。天下的粮食全被拿去酿酒了\u2014\u2014不是因为粮食多，而是因为人们要用酒精麻痹乱世中的恐惧。曹操后来不得不再次祭出铁腕禁酒令：酿酒者罚金，卖酒者罚金，买酒者罚金。但谁也禁不住了。#汉代 #酒政 #榷酒酤 #禁酒令
""",
    "prompts": [
        _daily("Han official distillery, workers brewing in large vats, government stamp on jars. Chinese title '\u201c官营酿酒\u201d' in calligraphic brush style. No heavy outlines. Ample whitespace."),
        _daily("Han marketplace, people openly drinking during the five-day festival. Chinese title '\u201c大酺五日\u201d' in calligraphic brush style. No heavy outlines."),
        _daily("Black market wine cellar hidden beneath a house, secret brewing equipment. Chinese title '\u201c私酒黑市\u201d' in calligraphic brush style. No heavy outlines."),
    ]
}

T[142] = {
    "folder": "xuandi-huo-shi",
    "article": """宣帝与霍氏\u2014\u2014隐忍两年到一夜灭门

宣帝的皇位是霍光给的。但\u201c给出来的皇位\u201d有一个致命的代价：你永远欠着别人的债。

宣帝即位后，霍光坐在朝堂上，把持了所有军国大事。宣帝每次上朝，霍光就坐在他旁边\u2014\u2014不是作为臣子坐在下面，而是跟天子并肩坐在一起。宣帝\u201c如芒在背\u201d，坐立不安。

宣帝怎么办？答：忍。他忍了两年。

这两年里，霍光提出什么，宣帝就同意什么。霍光要封自己的子弟做官，宣帝立刻批。霍光要把女儿霍成君嫁给宣帝做皇后，宣帝也答应了。霍家子弟遍布朝廷要职\u2014\u2014霍光的儿子霍禹当了大司马，霍光的侄孙霍云当了中郎将，霍光的女婿们把禁卫军牢牢攥在手里。

宣帝表面上对霍光言听计从，但有一件事露了底。他要立许平君为皇后\u2014\u2014那个在民间嫁给他、给他生了儿子的原配。霍光想让自己的女儿做皇后。宣帝下了一道诏书：\u201c朕微贱时用过一把宝剑，现在颇为思念。众卿能否帮朕找回来？\u201d

大臣们都明白了\u2014\u2014这是\u201c故剑情深\u201d。皇帝忘不掉的是那把剑，也是那个人。最后宣帝硬顶着霍光的压力，立了许平君。

但许平君很快就死了\u2014\u2014生孩子时被霍光的妻子霍显买通太医毒死了。宣帝什么也没说。他替许皇后办了隆重的葬礼，然后同意了立霍成君为后。

公元68年，霍光去世。宣帝以皇帝的规格为他举行了葬礼。霍家以为万事大吉了。

两年后，宣帝突然出手。他解除了霍家子弟的所有兵权，把霍家的姻亲一个个调离要害部门。霍家密谋造反，消息走漏。宣帝下令逮捕霍氏全族\u2014\u2014灭门。

忍了五年，一夜之间全还了。#汉宣帝 #霍光 #故剑情深 #许平君
""",
    "prompts": [
        _court("Young Emperor Xuan sitting sideways on the throne, Huo Guang beside him, tension visible. Chinese title '\u201c如芒在背\u201d' in calligraphic brush style. No heavy outlines. Ample whitespace."),
        _court("Emperor Xuan issuing the 'old sword' edict, ministers understanding his meaning. Chinese title '\u201c故剑情深\u201d' in calligraphic brush style. No heavy outlines."),
        _court("Huo family mansion at night, soldiers surrounding it, arrest underway. Chinese title '\u201c一夜灭门\u201d' in calligraphic brush style. No heavy outlines."),
    ]
}

T[143] = {
    "folder": "han-currency-war",
    "article": """西汉货币战争\u2014\u2014铸币权才是真正的命门

汉朝七十年\u201c吴楚七国之乱\u201d，表面上是诸侯造反，根子上是\u2014\u2014铸币权之争。

刘邦建国时，铜矿在各郡县手上，诸侯国可以自己铸钱。吴王刘濞占据了豫章郡的大铜山，招募亡命之徒日夜铸钱。吴国铸的钱质量好、分量足，整个长江流域都在用吴钱。吴国用铸币权换来了三样东西：军费、民心、粮食。

文帝时期进一步放开了铸币权\u2014\u2014任何人只要向官府交钱买\u201c铸币许可证\u201d，就可以合法铸钱。这一下可就炸锅了。家家户户都在铸钱，钱的质量越来越差。有的大户把铜钱磨薄了，磨下来的铜屑再铸新钱。市面上流通的铜钱越来越轻、越来越薄。到景帝时期，一斤铜的理论价值已经跌了一半。

晁错上书景帝要求收回铸币权。他算了一笔账：吴国每年铸钱收入相当于全国税收的三分之一。一个国家三分之一的经济命脉掌握在一个诸侯王手里，这个国家迟早要出事。

景帝采纳了晁错的建议。他下令禁止私人铸钱，把铜山全部收归国有。这就是\u201c削藩策\u201d的根本动机\u2014\u2014不是针对诸侯的权力，而是针对诸侯的钱。

这就是吴楚七国之乱的导火索。刘濞起兵时，最响亮的口号不是\u201c清君侧\u201d，而是\u201c钱不够用了\u201d。他给部下的承诺是\u201c打到长安，遍地黄金\u201d。

吴楚七国之乱被平定后，武帝彻底收回了铸币权。全国只有上林三官可以铸钱\u2014\u2014这就是\u201c上林三官五铢钱\u201d。从此以后，谁控制了铸币权，谁就控制了天下。

文帝放开铸币权是\u201c对\u201d还是\u201c错\u201d？从短期看，文帝是对的\u2014\u2014经济活了。从长期看，景帝和武帝也是对的\u2014\u2014国家对货币的控制权不能丢。这不是对错的问题，是阶段的问题。#铸币权 #吴楚七国之乱 #刘濞 #五铢钱
""",
    "prompts": [
        _daily("Wu state copper mine with workers casting coins, King Liu Bi inspecting. Chinese title '\u201c吴王铸钱\u201d' in calligraphic brush style. No heavy outlines. Ample whitespace."),
        _daily("Different Han coins of varying sizes and thicknesses, merchants arguing. Chinese title '\u201c钱法之乱\u201d' in calligraphic brush style. No heavy outlines."),
        _court("Emperor Jing and Chao Cuo discussing coinage reform, map of vassal states. Chinese title '\u201c削藩收钱\u201d' in calligraphic brush style. No heavy outlines."),
    ]
}

T[144] = {
    "folder": "xuandi-justice",
    "article": """宣帝与于定国\u2014\u2014不杀一人治天下的法官

西汉司法制度的巅峰，在宣帝时期的廷尉于定国身上。

于定国当廷尉（相当于最高法院院长）十八年。他在任期间，京城的死刑判决数量\u2014\u2014零。对，你没有看错\u2014\u2014十八年里，于定国没有判过一个人死刑。

他是怎么做到的？第一，慎刑原则。于定国对所有刑事案件的基本原则是\u201c疑罪从无\u201d\u2014\u2014证据不足的一律不判，有争议的一律从轻。他的名言是：\u201c宁失不辜，不杀无辜。\u201d

第二，和解优先。于定国在审判中极力推动民事和解。他判案前先让双方坐下来谈，谈成了撤案，谈不成再判。他审的案子，八成以上以和解结案。

第三，亲自查案。于定国不坐在办公室里看卷宗。他亲自到监狱里跟犯人谈话，到乡间调查取证。他有一双出了名的\u201c老鼠耳朵\u201d\u2014\u2014因为他总能在别人忽略的细节里发现真相。

宣帝如此信任于定国，有一个深层原因：宣帝小时候的悲惨遭遇（祖父戾太子被冤杀，全家被灭族）让他对司法公正有着近乎偏执的重视。他在位期间，大幅减轻了刑罚，废除了多项肉刑。

宣帝和于定国的组合，创造了整个中国古代史上最低的死刑率。连司马迁的外孙杨恽犯了\u201c大逆不道\u201d的罪，宣帝也没杀他，只判了免职。

有汉一代，最能体现\u201c仁政\u201d的，不是武帝的雄才大略，而是宣帝和于定国的不杀一人。#于定国 #廷尉 #汉宣帝 #慎刑
""",
    "prompts": [
        _court("Yu Dingguo in the courtroom, listening carefully to a defendant, scrolls piled high. Chinese title '\u201c廷尉听讼\u201d' in calligraphic brush style. No heavy outlines. Ample whitespace."),
        _daily("Yu Dingguo visiting a prison, talking with inmates personally. Chinese title '\u201c亲临狱中\u201d' in calligraphic brush style. No heavy outlines."),
        _court("Emperor Xuan and Yu Dingguo walking together in the palace garden. Chinese title '\u201c君臣仁政\u201d' in calligraphic brush style. No heavy outlines."),
    ]
}

T[145] = {
    "folder": "han-hunting-giant",
    "article": """两汉三代巨兽猎手\u2014\u2014飞将军力士与李广

汉朝人崇尚勇武，跟野兽搏斗在汉朝是一项受尊敬的技能。

李广被称为\u201c飞将军\u201d，但他在战场上最出名的事迹不是射杀匈奴人，而是射猛虎。他当右北平太守时，管辖的地区老虎很多。李广每次出猎都要找老虎比划。有一次他射中了一只老虎，但老虎没死，扑过来咬住了他的马腿。李广从马背上摔下来，顺手抽出短刀捅死了老虎。虎口夺命这件事，在匈奴人中传成了神话。

更猛的是他孙子李禹。史书记载李禹徒手杀死过一头成年公熊。这可比射老虎难多了\u2014\u2014弓箭还能保持距离，徒手搏熊意味着你要跟一头半吨重的猛兽贴身肉搏。

西汉还有一个叫申屠嘉的力士。他在街上遇到三头疯牛，赤手空拳把三头牛全打趴下了。老百姓看呆了，申屠嘉拍拍手上的灰走了。后来他当上了丞相\u2014\u2014汉朝\u201c力士当丞相\u201d的奇葩传统，从周勃杀猪开始，到申屠嘉打牛还在继续。

到了东汉，还有一个叫李广的\u2014\u2014同名同姓，是东汉末年人，号称\u201c勇过孙吴\u201d。他单骑追杀一头犀牛，用长矛刺穿了犀牛的额头。犀牛皮厚到什么程度？箭头射不透，但他用长矛扎透了。

汉代人对勇武的崇拜，本质是一种\u201c贵族精神\u201d。在汉朝，一个男人要是没跟野兽打过架，都不好意思说自己是个男人。#李广 #搏虎 #申屠嘉 #汉代勇武
""",
    "prompts": [
        _daily("Li Guang on horseback shooting a tiger with bow and arrow, dramatic forest scene. Chinese title '\u201c飞将军射虎\u201d' in calligraphic brush style. No heavy outlines. Ample whitespace."),
        _daily("Shen Tujia fighting three bulls in the street with bare hands, crowd amazed. Chinese title '\u201c力士搏牛\u201d' in calligraphic brush style. No heavy outlines."),
        _daily("Li Yu (Han dynasty) wrestling a bear, heroic outdoor scene. Chinese title '\u201c徒手搏熊\u201d' in calligraphic brush style. No heavy outlines."),
    ]
}

T[146] = {
    "folder": "han-slave-market",
    "article": """汉代人口贩卖\u2014\u2014一个奴婢只值一头猪

汉朝的奴隶贸易完全合法。长安西市有一个专门的\u201c奴市\u201d，规模比牲口市还大。每天清晨，奴隶贩子把奴隶赶到市场上，男女老少一排排站着，像挑牲口一样被买主翻来覆去看。

奴婢的价格在不同时期差异很大。武帝时期物价稳定，一个成年男奴的价格大约在2万到3万钱之间。5万钱就能买一个识字的、会算账的\u201c高级奴\u201d。到了末年，天下大乱，一个奴婢的价格跌到了2千到5千钱\u2014\u2014跟一头猪差不多。

汉朝最大的奴隶主是谁？不是商人，不是地主，而是皇族。武帝的赏赐动不动就\u201c赐奴婢百人\u201d。霍光家里有超过五百个奴婢。张安世家里有七百多个奴婢，他在家里搞了\u201c内部分工体系\u201d\u2014\u2014有人纺织、有人酿酒、有人贩货、有人记账。张家的\u201c企业内部市场\u201d比长安城外的市场经济还发达。

奴隶的来源主要有三种：战俘、债务抵押、人口拐卖。战俘构成了汉朝奴隶的大头\u2014\u2014汉朝对匈奴的每一次军事行动都会带回大批俘虏。这些匈奴人被卖为奴，大多数终生无法恢复自由。

汉朝法律对奴隶的保护几乎为零。主人打死自己的奴婢，只要向官府报备一下就行，不需要承担任何法律责任。如果奴婢告发主人，判刑的是奴婢。张安世家里有奴婢不堪虐待逃走，抓回来后直接被砍断了腿\u2014\u2014合法。

西汉废除奴隶制了吗？没有。直到王莽的\u201c王田制\u201d才提出了废除奴隶制的主张\u2014\u2014但王莽自己家里就有上千个奴婢，他的主张纯属自欺欺人。#汉代 #奴隶制 #奴婢 #人口贩卖
""",
    "prompts": [
        _daily("Han slave market in Chang'an, people lined up like livestock, buyers inspecting. Chinese title '\u201c长安奴市\u201d' in calligraphic brush style. No heavy outlines. Ample whitespace."),
        _daily("Zhang Anshi's mansion workshop, hundreds of slaves weaving and accounting. Chinese title '\u201c豪奴成市\u201d' in calligraphic brush style. No heavy outlines."),
        _daily("Xiongnu war captives being marched into Chang'an, chained, becoming slaves. Chinese title '\u201c匈奴为奴\u201d' in calligraphic brush style. No heavy outlines."),
    ]
}

T[147] = {
    "folder": "han-food",
    "article": """西汉吃什么\u2014\u2014烤肉配蜂蜜与没有辣椒的时代

穿越到西汉，你最想念的食物不是手机，是辣椒。西汉人完全不知道辣椒、西红柿、土豆、玉米、花生是什么\u2014\u2014这些全是几百年后从美洲传来的。

那西汉人吃什么？主食是粟（小米）和麦（面粉）。西汉人吃面食的方式非常原始\u2014\u2014把麦子炒熟了碾碎，加点水拌成糊糊吃，叫\u201c麦饭\u201d。这玩意儿又干又硬，难以下咽。

肉食方面，最常见的是猪肉和狗肉。你没看错\u2014\u2014狗肉。刘邦年轻时最爱吃狗肉，他的连襟樊哙就是杀狗卖肉的。汉朝人吃狗肉的风气很盛，长安城里遍地都是\u201c狗屠\u201d。狗肉最流行的吃法是烤着吃\u2014\u2014把狗肉串在竹签上，撒上盐和花椒烤。对，汉朝人已经开始吃花椒了，但只当调料用，不是当麻味的香料。

牛肉？牛在汉朝是不准随便杀的。汉朝法律规定：无故杀牛者\u201c罪至死\u201d。不是罚款，是杀头。所以汉朝人吃牛肉的机会极少\u2014\u2014只有在皇帝祭祀或特定节日时才能吃到。

调味品方面，西汉人已经用上了酱油的雏形\u2014\u2014\u201c酱\u201d。酱是用豆子发酵做的，类似今天的黄豆酱。但最让汉朝人欲罢不能的调料是蜂蜜。他们用蜂蜜涂在烤肉上，做成\u201c蜜炙肉\u201d。长沙马王堆汉墓出土的菜单上，就有\u201c蜜炙鹿肉\u201d\u2014\u2014两千年前的蜜汁烧烤。

喝酒必用酒樽，喝酒前要\u201c温酒\u201d\u2014\u2014放在铜樽里加热。汉朝人不喝凉酒，所有酒都要热过再喝。

口味方面，西汉人偏爱\u201c甜\u201d和\u201c咸\u201d的组合。糖的来源很有限\u2014\u2014主要是蜂蜜和饴糖。想吃甜食不容易。#西汉饮食 #狗肉 #蜜炙 #辣椒
""",
    "prompts": [
        _daily("Han kitchen: a cook grilling dog meat skewers over a fire, honey jar nearby. Chinese title '\u201c蜜炙肉\u201d' in calligraphic brush style. No heavy outlines. Ample whitespace."),
        _daily("Han commoner eating millet porridge (mai fan) at a wooden table with simple bowls. Chinese title '\u201c麦饭糊糊\u201d' in calligraphic brush style. No heavy outlines."),
        _daily("Han feast: dog meat stew, honey-grilled venison, warm wine in bronze vessels. Chinese title '\u201c汉家宴席\u201d' in calligraphic brush style. No heavy outlines."),
    ]
}

T[148] = {
    "folder": "han-game-sports",
    "article": """西汉人的业余生活\u2014\u2014六博蹴鞠与马球

汉朝人不只会打仗和斗殴，他们的业余生活相当丰富。

最流行的娱乐项目是\u201c六博\u201d\u2014\u2014一种棋类游戏，比今天的大富翁还复杂。六博使用六根箸（相当于骰子）和十二枚棋子，棋盘上有\u201c道\u201d和\u201c方\u201d，棋子沿着棋盘走，先到者胜。汉朝人玩六博玩得如痴如醉\u2014\u2014吴王刘濞的太子在长安跟皇太子玩六博，因为争棋路被皇太子用棋盘砸死了\u2014\u2014没错，这就是吴楚七国之乱的最初导火索。

更普及的运动是\u201c蹴鞠\u201d\u2014\u2014踢足球。汉朝的蹴鞠跟现代足球最大的区别是：汉朝人用毛皮缝制鞠球，填充毛发和碎布。比赛规则已经相当成熟：有球门、有裁判、有犯规处罚。汉武帝这个超级体育迷，让军队把蹴鞠列入了正式训练科目\u2014\u2014理由是：\u201c蹴鞠能练体力、练反应、练团队配合。\u201d他的将军们把战车围成一圈当球场，士兵们就在里面踢。

马球（击鞠）从西域传入后，迅速在长安贵族中流行。霍光家的公子们最爱打马球，每人一匹千里马，手里拿着长柄球杖。据说霍禹（霍光的儿子）打马球时能从马上倒立下来接球\u2014\u2014这个动作放在今天的马球场上也是顶级难度。

老百姓玩不起马，就玩\u201c角抵\u201d（摔跤）和\u201c投壶\u201d（往壶里投箭）。投壶在宴会上特别受欢迎\u2014\u2014喝多了酒的人投不准，姿势东倒西歪，逗得满堂大笑。

最奢侈的娱乐是\u201c斗兽\u201d。上林苑里养着老虎、熊、豹子。勇猛的汉朝人策马持矛跟野兽搏斗，围观的人声震天。这不是表演，这是真打。#蹴鞠 #六博 #马球 #汉代娱乐
""",
    "prompts": [
        _daily("Han soldiers playing cuju (football) inside a chariot circle, competitive scene. Chinese title '\u201c军旅蹴鞠\u201d' in calligraphic brush style. No heavy outlines. Ample whitespace."),
        _daily("Han noblemen playing polo on horseback with long-handled mallets. Chinese title '\u201c击鞠争锋\u201d' in calligraphic brush style. No heavy outlines."),
        _daily("Han banquet: guests playing pitch-pot (touhu), one drunk person missing the pot. Chinese title '\u201c投壶醉态\u201d' in calligraphic brush style. No heavy outlines."),
    ]
}

T[149] = {
    "folder": "han-yangzhou-boy",
    "article": """汉初扬州小男孩\u2014\u2014子胥托梦的政治寓言

这个故事的开始跟刘濞有关。刘濞造反前，扬州有个八岁的小男孩做了一个梦：

他梦见吴王夫差的相国伍子胥从江里走上岸来。伍子胥浑身湿透，头发散乱，冲到男孩面前说：\u201c孩子，帮我转告当今吴王\u2014\u2014我的尸骨还在江底泡了两百年。我求他替我在江边修一座庙，不然吴国要出大事。\u201d

男孩醒了，告诉了父亲。父亲觉得不对劲，去见了吴王刘濞。刘濞听了大怒：\u201c一个八岁小儿的梦话，也敢来见我！\u201d把父子俩赶走了。

半年后，刘濞起兵造反。汉军攻入吴国后，把刘濞的尸首扔进了长江里\u2014\u2014跟伍子胥同一个地方。

这个故事在汉代流传极广。背后的政治逻辑值得细品：伍子胥是春秋时期吴国的忠臣，被夫差冤杀后投尸江中。刘濞也是吴王\u2014\u2014同一片封地、同样的王号、同样的结局。老百姓用这个寓言来表达一个朴素的道理：不听劝的人，下场都是一样的。

《汉书》把这个记录在\u201c五行志\u201d里，归类为\u201c妖言\u201d。但史官写下这个故事的时候，也许在想\u2014\u2014如果刘濞真的听了那个八岁男孩的话，吴国还会灭亡吗？#刘濞 #伍子胥 #扬州 #预言
""",
    "prompts": [
        _daily("Eight-year-old boy in bed, ghostly vision of Wu Zixu rising from the river. Chinese title '\u201c子胥托梦\u201d' in calligraphic brush style. No heavy outlines. Ample whitespace."),
        _court("Boy and his father being turned away by King Liu Bi. Chinese title '\u201c吴王拒谏\u201d' in calligraphic brush style. No heavy outlines."),
        _daily("Liu Bi's body thrown into the same river as Wu Zixu, moonlight on water. Chinese title '\u201c一江同葬\u201d' in calligraphic brush style. No heavy outlines."),
    ]
}
