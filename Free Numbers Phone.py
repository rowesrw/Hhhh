import time
import requests
from bs4 import BeautifulSoup
from rich.console import Console
from rich.table import Table
from rich import box
E = '\033[1;31m'
G = '\033[1;35m'
Z = '\033[1;31m'  # احمر
X = '\033[1;33m'  # اصفر
Z1 = '\033[2;31m'  # احمر ثاني
F = '\033[2;32m'  # اخضر
A = '\033[2;34m'  # ازرق
C = '\033[2;35m'  # وردي
B = '\x1b[38;5;208m'  # برتقالي
Y = '\033[1;34m'  # ازرق فاتح
M = '\x1b[1;37m'  # ابیض
S = '\033[1;33m'
U = '\x1b[1;37m'  # ابیض
BRed = '\x1b[1;31m'
BGreen = '\x1b[1;32m'
BYellow = '\x1b[1;33m'
R = '\x1b[1;34m'
BPurple = '\x1b[1;35m'
BCyan = '\x1b[1;36m'
BWhite = '\x1b[1;37m'

print(f'''{B}{E}=============================={B}
|{F}[+] YouTube    : {B}|أحمد الحراني 
|{F}[+] TeleGram  : {B} maho_s9    |
|{F}[+] Instagram  : {B}ahmedalharrani |
|{F}[+] Tool  : {B} Free Numbers|
{E}==============================''')

tlg = f"""
    1: {X}Canada: +13434535118,
    2: {F}United States: +13182697169,
    3: {A}Netherlands: +3197010518302,
    4: {B}France: +33644629866,
    5: {X}Sweden: +46726412705,
    6: {F}Sweden: +46726412713,
    7: {A}Sweden: +46726412760,
    8: {B}China: +8615486934106,
    9: {X}United Kingdom: +447700184823,
    10: {F}France: +33644628322,
    11: {A}United States: +15024653767,
    12: {B}France: +33757056592,
    13: {X}France: +33757056461,
    14: {F}China: +8613748154841,
    15: {A}United Kingdom: +447893984121,
    16: {B}United Kingdom: +447893984120,
    17: {X}United Kingdom: +447893984119,
    18: {F}United Kingdom: +447893984118,
    19: {A}France: +33644628325,
    20: {B}France: +33644628324,
    21: {X}China: +8613666696969,
    22: {F}United Kingdom: +447776728014,
    23: {A}Russia: +79991966144,
    24: {B}Hong Kong: +852256495852652,
    25: {X}China: +861824087849754,
    26: {F}United States: +1219923540657,
    27: {A}United States: +125883832111,
    28: {B}Hong Kong: +852725310451,
    29: {X}Hong Kong: +852302792408,
    30: {F}China: +861823675884622,
    31: {A}Hong Kong: +8527876214827,
    32: {B}China: +861397947212331,
    33: {X}Hong Kong: +8521482538124633,
    34: {F}Hong Kong: +8521371381152740,
    35: {A}Hong Kong: +852256495852647,
    36: {B}China: +861824087849749,
    37: {X}United States: +1219923540652,
    38: {F}United States: +1258838321156,
    39: {A}Hong Kong: +8527253104558,
    40: {B}Hong Kong: +852302792403,
    41: {X}China: +861823675884617,
    42: {F}Hong Kong: +8527876214822,
    43: {A}China: +861397947212326,
    44: {B}Hong Kong: +8521482538124628,
    45: {X}Hong Kong: +8521371381152735,
    46: {F}Hong Kong: +852256495852642,
    47: {A}China: +861824087849744,
    48: {B}United States: +1219923540647,
    49: {X}United States: +1258838321151,
    50: {F}Hong Kong: +8527253104553,
    51: {A}Hong Kong: +85222912297791,
    52: {B}China: +86182367588467,
    53: {X}Hong Kong: +8527876214812,
    54: {F}China: +861397947212316,
    55: {A}Hong Kong: +8521482538124618,
    56: {B}Hong Kong: +8521371381152725,
    57: {X}Hong Kong: +852256495852632,
    58: {F}China: +861824087849734,
    59: {A}United States: +1219923540637,
    60: {B}United States: +1258838321141,
    61: {X}Hong Kong: +8527253104543,
    62: {F}Hong Kong: +852229122977953,
    63: {A}China: +86182367588462,
    64: {B}Hong Kong: +852787621487,
    65: {X}Hong Kong: +8521482538124613,
    66: {F}Hong Kong: +8521371381152720,
    67: {A}Hong Kong: +852256495852627,
    68: {B}China: +861824087849729,
    69: {X}United States: +1219923540632,
    70: {F}United States: +1258838321136,
    71: {A}Hong Kong: +8527253104538,
    72: {B}Hong Kong: +852229122977948,
    73: {X}Hong Kong: +852151692081501,
    74: {F}Hong Kong: +852144678972531,
    75: {A}China: +8613578845916,
    76: {B}United States: +15053753974,
    77: {X}United States: +12083064581,
    78: {F}Hong Kong: +852145830144792,
    79: {A}United States: +12926554282,
    80: {B}China: +8615470874900,
    81: {X}United Kingdom: +447388549972,
    82: {F}United States: +12942129232,
    83: {A}United States: +12448719084,
    84: {B}China: +8613852699482,
    85: {X}United States: +12126803691,
    86: {F}China: +8613556847047,
    87: {A}Netherlands: +31657479598,
    88: {B}United Kingdom: +447404300533,
    89: {X}Latvia: +37126031755,
    90: {F}Hong Kong: +85218145671497
"""
print(tlg)

choose = {
    1: {'Canada': '+13434535118'},
    2: {'United States': '+13182697169'},
    3: {'Netherlands': '+3197010518302'},
    4: {'France': '+33644629866'},
    5: {'Sweden': '+46726412705'},
    6: {'Sweden': '+46726412713'},
    7: {'Sweden': '+46726412760'},
    8: {'China': '+8615486934106'},
    9: {'United Kingdom': '+447700184823'},
    10: {'France': '+33644628322'},
    11: {'United States': '+15024653767'},
    12: {'France': '+33757056592'},
    13: {'France': '+33757056461'},
    14: {'China': '+8613748154841'},
    15: {'United Kingdom': '+447893984121'},
    16: {'United Kingdom': '+447893984120'},
    17: {'United Kingdom': '+447893984119'},
    18: {'United Kingdom': '+447893984118'},
    19: {'France': '+33644628325'},
    20: {'France': '+33644628324'},
    21: {'China': '+8613666696969'},
    22: {'United Kingdom': '+447776728014'},
    23: {'Russia': '+79991966144'},
    24: {'Hong Kong': '+852256495852652'},
    25: {'China': '+861824087849754'},
    26: {'United States': '+1219923540657'},
    27: {'United States': '+125883832111'},
    28: {'Hong Kong': '+852725310451'},
    29: {'Hong Kong': '+852302792408'},
    30: {'China': '+861823675884622'},
    31: {'Hong Kong': '+8527876214827'},
    32: {'China': '+861397947212331'},
    33: {'Hong Kong': '+8521482538124633'},
    34: {'Hong Kong': '+8521371381152740'},
    35: {'Hong Kong': '+852256495852647'},
    36: {'China': '+861824087849749'},
    37: {'United States': '+1219923540652'},
    38: {'United States': '+1258838321156'},
    39: {'Hong Kong': '+8527253104558'},
    40: {'Hong Kong': '+852302792403'},
    41: {'China': '+861823675884617'},
    42: {'Hong Kong': '+8527876214822'},
    43: {'China': '+861397947212326'},
    44: {'Hong Kong': '+8521482538124628'},
    45: {'Hong Kong': '+8521371381152735'},
    46: {'Hong Kong': '+852256495852642'},
    47: {'China': '+861824087849744'},
    48: {'United States': '+1219923540647'},
    49: {'United States': '+1258838321151'},
    50: {'Hong Kong': '+8527253104553'},
    51: {'Hong Kong': '+85222912297791'},
    52: {'China': '+86182367588467'},
    53: {'Hong Kong': '+8527876214812'},
    54: {'China': '+861397947212316'},
    55: {'Hong Kong': '+8521482538124618'},
    56: {'Hong Kong': '+8521371381152725'},
    57: {'Hong Kong': '+852256495852632'},
    58: {'China': '+861824087849734'},
    59: {'United States': '+1219923540637'},
    60: {'United States': '+1258838321141'},
    61: {'Hong Kong': '+8527253104543'},
    62: {'Hong Kong': '+852229122977953'},
    63: {'China': '+86182367588462'},
    64: {'Hong Kong': '+852787621487'},
    65: {'Hong Kong': '+8521482538124613'},
    66: {'Hong Kong': '+8521371381152720'},
    67: {'Hong Kong': '+852256495852627'},
    68: {'China': '+861824087849729'},
    69: {'United States': '+1219923540632'},
    70: {'United States': '+1258838321136'},
    71: {'Hong Kong': '+8527253104538'},
    72: {'Hong Kong': '+852229122977948'},
    73: {'Hong Kong': '+852151692081501'},
    74: {'Hong Kong': '+852144678972531'},
    75: {'China': '+8613578845916'},
    76: {'United States': '+15053753974'},
    77: {'United States': '+12083064581'},
    78: {'Hong Kong': '+852145830144792'},
    79: {'United States': '+12926554282'},
    80: {'China': '+8615470874900'},
    81: {'United Kingdom': '+447388549972'},
    82: {'United States': '+12942129232'},
    83: {'United States': '+12448719084'},
    84: {'China': '+8613852699482'},
    85: {'United States': '+12126803691'},
    86: {'China': '+8613556847047'},
    87: {'Netherlands': '+31657479598'},
    88: {'United Kingdom': '+447404300533'},
    89: {'Latvia': '+37126031755'},
    90: {'Hong Kong': '+85218145671497'}
}

def ahmed(messages):
    console = Console()
    table = Table(show_header=False, box=box.SQUARE)
    table.add_column("", style="dim", width=2)
    table.add_column("Messages", justify="left", style="green")
    for index, message in enumerate(messages, start=1):
        table.add_row(f"{index}.", message)
    console.print(table)

def refresh_page(num):
    while True:
        time.sleep(3)
        url = f'https://sms24.me/en/numbers/{num}'
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        messages = []
        for span in soup.find_all('span', class_='placeholder text-break'):
            message = span.text.strip()
            messages.append(message)
        ahmed(messages)
        choice = input("هل تريد تحديث الصفحة؟ (y/n): ")
        if choice.lower() != 'y':
            break

def mahos():
    num = int(input("اختر رقم البلد: "))

    if num in choose:
        country = list(choose[num].keys())[0]
        number = choose[num][country]
        print(f"{E}البلد المختار:", country)
        print(f"{M}الرقم المرتبط به:", number)
    else:
        print("الرقم غير صحيح، يرجى اختيار رقم صحيح.")
        return

    number_splitted = number.split('+')
    num = number_splitted[1]

    url = f'https://sms24.me/en/numbers/{num}'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    messages = []
    for span in soup.find_all('span', class_='placeholder text-break'):
        message = span.text.strip()
        messages.append(message)

    ahmed(messages)

    choice = input("هل تريد تحديث الصفحة؟ (y/n): ")
    if choice.lower() == 'y':
        refresh_page(num)

if __name__ == "__main__":
    mahos()