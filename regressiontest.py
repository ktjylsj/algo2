import csv
import pandas as pd
import datetime as dt
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
import matplotlib.pyplot as plt
from statsmodels.tsa.arima_model import ARIMA

train = ['1호선', '2호선', '3호선', '4호선', '5호선', '6호선', '7호선', '8호선', '9호선']

# 구 별
dobong = []
nowon = []
gangbuk = []
sungbuk = []
jungrang = []
dongdae = []
jongro = []
eunpung = []
seodae = []
junggu = []
sungdong = []
gwangjin = []
yongsan = []
mapo = []
gangseo = []
yangcheon = []
guro = []
yeongdeong = []
dongjak = []
gwanack = []
geumchun = []
seocho = []
gangnam = []
songpa = []
gangdong = []

# 구 모델용 데이터
ddm = []    # 01 동대문구
jg = []     # 02 중구
jr = []     # 03 종로구
gr = []     # 04 구로구
ydp = []    # 05 영등포구
sd = []     # 06 성동구
sp = []     # 07 송파구
sch = []    # 08 서초구
gj = []     # 09 광진구
ga = []     # 10 관악구
yc = []     # 11 양천구
dj = []     # 12 동작구
gn = []     # 13 강남구
mp = []     # 14 마포구
sdm = []    # 15 서대문구
ep = []     # 16 은평구
gb = []     # 17 강북구
ys = []     # 18 용산구
sb = []     # 19 성북구
nw = []     # 20 노원구
db = []     # 21 도봉구
gd = []     # 22 강동구
gs = []     # 23 강서구
jl = []     # 24 중랑구
gch = []    # 25 금천구

datelist = []

file_name = './data/gus.csv'
f = open(file_name)
data = csv.reader(f)
next(data)
gus = []
for row in data:
    if len(row) == 10:
        if row[9] == '':
            continue
        found = True
        for gu in gus:
            if gu == row[9]:
                found = False
                break
        if found:
            gus.append(row[9])

f = open(file_name)
data = csv.reader(f)
next(data)
for row in data:
    if row[9] == gus[0]:
        dongdae.append(row[3])
    elif row[9] == gus[1]:
        junggu.append(row[3])
    elif row[9] == gus[2]:
        jongro.append(row[3])
    elif row[9] == gus[3]:
        guro.append(row[3])
    elif row[9] == gus[4]:
        yeongdeong.append(row[3])
    elif row[9] == gus[5]:
        sungdong.append(row[3])
    elif row[9] == gus[6]:
        songpa.append(row[3])
    elif row[9] == gus[7]:
        seocho.append(row[3])
    elif row[9] == gus[8]:
        gwangjin.append(row[3])
    elif row[9] == gus[9]:
        gwanack.append(row[3])
    elif row[9] == gus[10]:
        yangcheon.append(row[3])
    elif row[9] == gus[11]:
        dongjak.append(row[3])
    elif row[9] == gus[12]:
        gangnam.append(row[3])
    elif row[9] == gus[13]:
        mapo.append(row[3])
    elif row[9] == gus[14]:
        seodae.append(row[3])
    elif row[9] == gus[15]:
        eunpung.append(row[3])
    elif row[9] == gus[16]:
        gangbuk.append(row[3])
    elif row[9] == gus[17]:
        yongsan.append(row[3])
    elif row[9] == gus[18]:
        sungbuk.append(row[3])
    elif row[9] == gus[19]:
        nowon.append(row[3])
    elif row[9] == gus[20]:
        dobong.append(row[3])
    elif row[9] == gus[21]:
        gangdong.append(row[3])
    elif row[9] == gus[22]:
        gangseo.append(row[3])
    elif row[9] == gus[23]:
        jungrang.append(row[3])
    elif row[9] == gus[24]:
        geumchun.append(row[3])


for i in range(4, 13):
    one = 0
    onecnt = 0
    two = 0
    twocnt = 0
    thr = 0
    thrcnt = 0
    fou = 0
    foucnt = 0
    fiv = 0
    fivcnt = 0
    six = 0
    sixcnt = 0
    sev = 0
    sevcnt = 0
    eig = 0
    eigcnt = 0
    nin = 0
    nincnt = 0
    ten = 0
    tencnt = 0
    ele = 0
    elecnt = 0
    twe = 0
    twecnt = 0
    tht = 0
    thtcnt = 0
    fot = 0
    fotcnt = 0
    fif = 0
    fifcnt = 0
    sit = 0
    sitcnt = 0
    set = 0
    setcnt = 0
    eit = 0
    eitcnt = 0
    nit = 0
    nitcnt = 0
    twn = 0
    twncnt = 0
    ton = 0
    toncnt = 0
    tto = 0
    ttocnt = 0
    tth = 0
    tthcnt = 0
    tfo = 0
    tfocnt = 0
    tfi = 0
    tficnt = 0
    date = "2015-"
    if i < 10:
        file_name = './data/2015_0' + str(i) + '.csv'
        date = date + "0" + str(i) + "-01"
    else:
        file_name = './data/2015_' + str(i) + '.csv'
        date = date + str(i) + "-01"
    f = open(file_name)
    data = csv.reader(f)
    convdate = dt.datetime.strptime(date, "%Y-%m-%d").date()
    datelist.append(convdate)
    for row in data:
        if row[3] in dongdae:
            one += float(int(row[6].replace(',', ''))/(int(row[4].replace(',', '')) + int(row[6].replace(',', ''))))
            onecnt += 1
        elif row[3] in junggu:
            two += float(int(row[6].replace(',', ''))/(int(row[4].replace(',', '')) + int(row[6].replace(',', ''))))
            twocnt += 1
        elif row[3] in jongro:
            thr += float(int(row[6].replace(',', ''))/(int(row[4].replace(',', '')) + int(row[6].replace(',', ''))))
            thrcnt += 1
        elif row[3] in guro:
            fou += float(int(row[6].replace(',', ''))/(int(row[4].replace(',', '')) + int(row[6].replace(',', ''))))
            foucnt += 1
        elif row[3] in yeongdeong:
            fiv += float(int(row[6].replace(',', ''))/(int(row[4].replace(',', '')) + int(row[6].replace(',', ''))))
            fivcnt += 1
        elif row[3] in sungdong:
            six += float(int(row[6].replace(',', ''))/(int(row[4].replace(',', '')) + int(row[6].replace(',', ''))))
            sixcnt += 1
        elif row[3] in songpa:
            sev += float(int(row[6].replace(',', ''))/(int(row[4].replace(',', '')) + int(row[6].replace(',', ''))))
            sevcnt += 1
        elif row[3] in seocho:
            eig += float(int(row[6].replace(',', ''))/(int(row[4].replace(',', '')) + int(row[6].replace(',', ''))))
            eigcnt += 1
        elif row[3] in gwangjin:
            nin += float(int(row[6].replace(',', ''))/(int(row[4].replace(',', '')) + int(row[6].replace(',', ''))))
            nincnt += 1
        elif row[3] in gwanack:
            ten += float(int(row[6].replace(',', ''))/(int(row[4].replace(',', '')) + int(row[6].replace(',', ''))))
            tencnt += 1
        elif row[3] in yangcheon:
            ele += float(int(row[6].replace(',', ''))/(int(row[4].replace(',', '')) + int(row[6].replace(',', ''))))
            elecnt += 1
        elif row[3] in dongjak:
            twe += float(int(row[6].replace(',', ''))/(int(row[4].replace(',', '')) + int(row[6].replace(',', ''))))
            twecnt += 1
        elif row[3] in gangnam:
            tht += float(int(row[6].replace(',', ''))/(int(row[4].replace(',', '')) + int(row[6].replace(',', ''))))
            thtcnt += 1
        elif row[3] in mapo:
            fot += float(int(row[6].replace(',', ''))/(int(row[4].replace(',', '')) + int(row[6].replace(',', ''))))
            fotcnt += 1
        elif row[3] in seodae:
            fif += float(int(row[6].replace(',', ''))/(int(row[4].replace(',', '')) + int(row[6].replace(',', ''))))
            fifcnt += 1
        elif row[3] in eunpung:
            sit += float(int(row[6].replace(',', ''))/(int(row[4].replace(',', '')) + int(row[6].replace(',', ''))))
            sitcnt += 1
        elif row[3] in gangbuk:
            set += float(int(row[6].replace(',', ''))/(int(row[4].replace(',', '')) + int(row[6].replace(',', ''))))
            setcnt += 1
        elif row[3] in yongsan:
            eit += float(int(row[6].replace(',', ''))/(int(row[4].replace(',', '')) + int(row[6].replace(',', ''))))
            eitcnt += 1
        elif row[3] in sungbuk:
            nit += float(int(row[6].replace(',', ''))/(int(row[4].replace(',', '')) + int(row[6].replace(',', ''))))
            nitcnt += 1
        elif row[3] in nowon:
            twn += float(int(row[6].replace(',', ''))/(int(row[4].replace(',', '')) + int(row[6].replace(',', ''))))
            twncnt += 1
        elif row[3] in dobong:
            ton += float(int(row[6].replace(',', ''))/(int(row[4].replace(',', '')) + int(row[6].replace(',', ''))))
            toncnt += 1
        elif row[3] in gangdong:
            tto += float(int(row[6].replace(',', ''))/(int(row[4].replace(',', '')) + int(row[6].replace(',', ''))))
            ttocnt += 1
        elif row[3] in gangseo:
            tth += float(int(row[6].replace(',', ''))/(int(row[4].replace(',', '')) + int(row[6].replace(',', ''))))
            tthcnt += 1
        elif row[3] in jungrang:
            tfo += float(int(row[6].replace(',', ''))/(int(row[4].replace(',', '')) + int(row[6].replace(',', ''))))
            tfocnt += 1
        elif row[3] in geumchun:
            tfi += float(int(row[6].replace(',', ''))/(int(row[4].replace(',', '')) + int(row[6].replace(',', ''))))
            tficnt += 1
    one = one/onecnt
    ddm.append(float(one))
    two = two/twocnt
    jg.append(float(two))
    thr = thr/thrcnt
    jr.append(float(thr))
    fou = fou/foucnt
    gr.append(float(fou))
    fiv = fiv/fivcnt
    ydp.append(float(fiv))
    six = six/sixcnt
    sd.append(float(six))
    sev = sev/sevcnt
    sp.append(float(sev))
    eig = eig/eigcnt
    sch.append(float(eig))
    nin = nin/nincnt
    gj.append(float(nin))
    ten = ten/tencnt
    ga.append(float(ten))
    ele = ele/elecnt
    yc.append(float(ele))
    twe = twe/twecnt
    dj.append(float(twe))
    tht = tht/thtcnt
    gn.append(float(tht))
    fot = fot/fotcnt
    mp.append(float(fot))
    fif = fif/fifcnt
    sd.append(float(fif))
    sit = sit/sitcnt
    ep.append(float(sit))
    set = set/setcnt
    gb.append(float(set))
    eit = eit/eitcnt
    ys.append(float(eig))
    nit = nit/nitcnt
    sb.append(float(nit))
    twn = twn/twncnt
    nw.append(float(twn))
    ton = ton/toncnt
    db.append(float(ton))
    tto = tto/ttocnt
    gd.append(float(tto))
    tth = tth/tthcnt
    gs.append(float(tth))
    tfo = tfo/tfocnt
    jl.append(float(tfo))
    tfi = tfi/tficnt
    gch.append(float(tfi))

for yr in range(2016, 2019):
    for i in range(1, 13):
        one = 0
        onecnt = 0
        two = 0
        twocnt = 0
        thr = 0
        thrcnt = 0
        fou = 0
        foucnt = 0
        fiv = 0
        fivcnt = 0
        six = 0
        sixcnt = 0
        sev = 0
        sevcnt = 0
        eig = 0
        eigcnt = 0
        nin = 0
        nincnt = 0
        ten = 0
        tencnt = 0
        ele = 0
        elecnt = 0
        twe = 0
        twecnt = 0
        tht = 0
        thtcnt = 0
        fot = 0
        fotcnt = 0
        fif = 0
        fifcnt = 0
        sit = 0
        sitcnt = 0
        set = 0
        setcnt = 0
        eit = 0
        eitcnt = 0
        nit = 0
        nitcnt = 0
        twn = 0
        twncnt = 0
        ton = 0
        toncnt = 0
        tto = 0
        ttocnt = 0
        tth = 0
        tthcnt = 0
        tfo = 0
        tfocnt = 0
        tfi = 0
        tficnt = 0
        date = str(yr) + '-'
        if i < 10:
            file_name = './data/' + str(yr) + '_0' + str(i) + '.csv'
            date = date + '0' + str(i) + '-01'
        else:
            file_name = './data/' + str(yr) + '_' + str(i) + '.csv'
            date = date + str(i) + '-01'
        f = open(file_name)
        data = csv.reader(f)
        convdate = dt.datetime.strptime(date, "%Y-%m-%d").date()
        datelist.append(convdate)
        for row in data:
            if row[3] in dongdae:
                one += float(int(row[6].replace(',', ''))/(int(row[4].replace(',', '')) + int(row[6].replace(',', ''))))
                onecnt += 1
            elif row[3] in junggu:
                two += float(int(row[6].replace(',', ''))/(int(row[4].replace(',', '')) + int(row[6].replace(',', ''))))
                twocnt += 1
            elif row[3] in jongro:
                thr += float(int(row[6].replace(',', ''))/(int(row[4].replace(',', '')) + int(row[6].replace(',', ''))))
                thrcnt += 1
            elif row[3] in guro:
                fou += float(int(row[6].replace(',', ''))/(int(row[4].replace(',', '')) + int(row[6].replace(',', ''))))
                foucnt += 1
            elif row[3] in yeongdeong:
                fiv += float(int(row[6].replace(',', ''))/(int(row[4].replace(',', '')) + int(row[6].replace(',', ''))))
                fivcnt += 1
            elif row[3] in sungdong:
                six += float(int(row[6].replace(',', ''))/(int(row[4].replace(',', '')) + int(row[6].replace(',', ''))))
                sixcnt += 1
            elif row[3] in songpa:
                sev += float(int(row[6].replace(',', ''))/(int(row[4].replace(',', '')) + int(row[6].replace(',', ''))))
                sevcnt += 1
            elif row[3] in seocho:
                eig += float(int(row[6].replace(',', ''))/(int(row[4].replace(',', '')) + int(row[6].replace(',', ''))))
                eigcnt += 1
            elif row[3] in gwangjin:
                nin += float(int(row[6].replace(',', ''))/(int(row[4].replace(',', '')) + int(row[6].replace(',', ''))))
                nincnt += 1
            elif row[3] in gwanack:
                ten += float(int(row[6].replace(',', ''))/(int(row[4].replace(',', '')) + int(row[6].replace(',', ''))))
                tencnt += 1
            elif row[3] in yangcheon:
                ele += float(int(row[6].replace(',', ''))/(int(row[4].replace(',', '')) + int(row[6].replace(',', ''))))
                elecnt += 1
            elif row[3] in dongjak:
                twe += float(int(row[6].replace(',', ''))/(int(row[4].replace(',', '')) + int(row[6].replace(',', ''))))
                twecnt += 1
            elif row[3] in gangnam:
                tht += float(int(row[6].replace(',', ''))/(int(row[4].replace(',', '')) + int(row[6].replace(',', ''))))
                thtcnt += 1
            elif row[3] in mapo:
                fot += float(int(row[6].replace(',', ''))/(int(row[4].replace(',', '')) + int(row[6].replace(',', ''))))
                fotcnt += 1
            elif row[3] in seodae:
                fif += float(int(row[6].replace(',', ''))/(int(row[4].replace(',', '')) + int(row[6].replace(',', ''))))
                fifcnt += 1
            elif row[3] in eunpung:
                sit += float(int(row[6].replace(',', ''))/(int(row[4].replace(',', '')) + int(row[6].replace(',', ''))))
                sitcnt += 1
            elif row[3] in gangbuk:
                set += float(int(row[6].replace(',', ''))/(int(row[4].replace(',', '')) + int(row[6].replace(',', ''))))
                setcnt += 1
            elif row[3] in yongsan:
                eit += float(int(row[6].replace(',', ''))/(int(row[4].replace(',', '')) + int(row[6].replace(',', ''))))
                eitcnt += 1
            elif row[3] in sungbuk:
                nit += float(int(row[6].replace(',', ''))/(int(row[4].replace(',', '')) + int(row[6].replace(',', ''))))
                nitcnt += 1
            elif row[3] in nowon:
                twn += float(int(row[6].replace(',', ''))/(int(row[4].replace(',', '')) + int(row[6].replace(',', ''))))
                twncnt += 1
            elif row[3] in dobong:
                ton += float(int(row[6].replace(',', ''))/(int(row[4].replace(',', '')) + int(row[6].replace(',', ''))))
                toncnt += 1
            elif row[3] in gangdong:
                tto += float(int(row[6].replace(',', ''))/(int(row[4].replace(',', '')) + int(row[6].replace(',', ''))))
                ttocnt += 1
            elif row[3] in gangseo:
                tth += float(int(row[6].replace(',', ''))/(int(row[4].replace(',', '')) + int(row[6].replace(',', ''))))
                tthcnt += 1
            elif row[3] in jungrang:
                tfo += float(int(row[6].replace(',', ''))/(int(row[4].replace(',', '')) + int(row[6].replace(',', ''))))
                tfocnt += 1
            elif row[3] in geumchun:
                tfi += float(int(row[6].replace(',', ''))/(int(row[4].replace(',', '')) + int(row[6].replace(',', ''))))
                tficnt += 1
        one = one/onecnt
        ddm.append(float(one))
        two = two/twocnt
        jg.append(float(two))
        thr = thr/thrcnt
        jr.append(float(thr))
        fou = fou/foucnt
        gr.append(float(fou))
        fiv = fiv/fivcnt
        ydp.append(float(fiv))
        six = six/sixcnt
        sd.append(float(six))
        sev = sev/sevcnt
        sp.append(float(sev))
        eig = eig/eigcnt
        sch.append(float(eig))
        nin = nin/nincnt
        gj.append(float(nin))
        ten = ten/tencnt
        ga.append(float(ten))
        ele = ele/elecnt
        yc.append(float(ele))
        twe = twe/twecnt
        dj.append(float(twe))
        tht = tht/thtcnt
        gn.append(float(tht))
        fot = fot/fotcnt
        mp.append(float(fot))
        fif = fif/fifcnt
        sd.append(float(fif))
        sit = sit/sitcnt
        ep.append(float(sit))
        set = set/setcnt
        gb.append(float(set))
        eit = eit/eitcnt
        ys.append(float(eig))
        nit = nit/nitcnt
        sb.append(float(nit))
        twn = twn/twncnt
        nw.append(float(twn))
        ton = ton/toncnt
        db.append(float(ton))
        tto = tto/ttocnt
        gd.append(float(tto))
        tth = tth/tthcnt
        gs.append(float(tth))
        tfo = tfo/tfocnt
        jl.append(float(tfo))
        tfi = tfi/tficnt
        gch.append(float(tfi))
            
for i in range(1, 10):
    one = 0
    onecnt = 0
    two = 0
    twocnt = 0
    thr = 0
    thrcnt = 0
    fou = 0
    foucnt = 0
    fiv = 0
    fivcnt = 0
    six = 0
    sixcnt = 0
    sev = 0
    sevcnt = 0
    eig = 0
    eigcnt = 0
    nin = 0
    nincnt = 0
    ten = 0
    tencnt = 0
    ele = 0
    elecnt = 0
    twe = 0
    twecnt = 0
    tht = 0
    thtcnt = 0
    fot = 0
    fotcnt = 0
    fif = 0
    fifcnt = 0
    sit = 0
    sitcnt = 0
    set = 0
    setcnt = 0
    eit = 0
    eitcnt = 0
    nit = 0
    nitcnt = 0
    twn = 0
    twncnt = 0
    ton = 0
    toncnt = 0
    tto = 0
    ttocnt = 0
    tth = 0
    tthcnt = 0
    tfo = 0
    tfocnt = 0
    tfi = 0
    tficnt = 0
    date = '2019-'
    file_name = './data/2019_0' + str(i) + '.csv'
    date = date + '0' + str(i) + '-01'
    f = open(file_name)
    data = csv.reader(f)
    convdate = dt.datetime.strptime(date, "%Y-%m-%d").date()
    datelist.append(convdate)
    for row in data:
        if row[3] in dongdae:
            one += float(int(row[6].replace(',', ''))/(int(row[4].replace(',', '')) + int(row[6].replace(',', ''))))
            onecnt += 1
        elif row[3] in junggu:
            two += float(int(row[6].replace(',', ''))/(int(row[4].replace(',', '')) + int(row[6].replace(',', ''))))
            twocnt += 1
        elif row[3] in jongro:
            thr += float(int(row[6].replace(',', ''))/(int(row[4].replace(',', '')) + int(row[6].replace(',', ''))))
            thrcnt += 1
        elif row[3] in guro:
            fou += float(int(row[6].replace(',', ''))/(int(row[4].replace(',', '')) + int(row[6].replace(',', ''))))
            foucnt += 1
        elif row[3] in yeongdeong:
            fiv += float(int(row[6].replace(',', ''))/(int(row[4].replace(',', '')) + int(row[6].replace(',', ''))))
            fivcnt += 1
        elif row[3] in sungdong:
            six += float(int(row[6].replace(',', ''))/(int(row[4].replace(',', '')) + int(row[6].replace(',', ''))))
            sixcnt += 1
        elif row[3] in songpa:
            sev += float(int(row[6].replace(',', ''))/(int(row[4].replace(',', '')) + int(row[6].replace(',', ''))))
            sevcnt += 1
        elif row[3] in seocho:
            eig += float(int(row[6].replace(',', ''))/(int(row[4].replace(',', '')) + int(row[6].replace(',', ''))))
            eigcnt += 1
        elif row[3] in gwangjin:
            nin += float(int(row[6].replace(',', ''))/(int(row[4].replace(',', '')) + int(row[6].replace(',', ''))))
            nincnt += 1
        elif row[3] in gwanack:
            ten += float(int(row[6].replace(',', ''))/(int(row[4].replace(',', '')) + int(row[6].replace(',', ''))))
            tencnt += 1
        elif row[3] in yangcheon:
            ele += float(int(row[6].replace(',', ''))/(int(row[4].replace(',', '')) + int(row[6].replace(',', ''))))
            elecnt += 1
        elif row[3] in dongjak:
            twe += float(int(row[6].replace(',', ''))/(int(row[4].replace(',', '')) + int(row[6].replace(',', ''))))
            twecnt += 1
        elif row[3] in gangnam:
            tht += float(int(row[6].replace(',', ''))/(int(row[4].replace(',', '')) + int(row[6].replace(',', ''))))
            thtcnt += 1
        elif row[3] in mapo:
            fot += float(int(row[6].replace(',', ''))/(int(row[4].replace(',', '')) + int(row[6].replace(',', ''))))
            fotcnt += 1
        elif row[3] in seodae:
            fif += float(int(row[6].replace(',', ''))/(int(row[4].replace(',', '')) + int(row[6].replace(',', ''))))
            fifcnt += 1
        elif row[3] in eunpung:
            sit += float(int(row[6].replace(',', ''))/(int(row[4].replace(',', '')) + int(row[6].replace(',', ''))))
            sitcnt += 1
        elif row[3] in gangbuk:
            set += float(int(row[6].replace(',', ''))/(int(row[4].replace(',', '')) + int(row[6].replace(',', ''))))
            setcnt += 1
        elif row[3] in yongsan:
            eit += float(int(row[6].replace(',', ''))/(int(row[4].replace(',', '')) + int(row[6].replace(',', ''))))
            eitcnt += 1
        elif row[3] in sungbuk:
            nit += float(int(row[6].replace(',', ''))/(int(row[4].replace(',', '')) + int(row[6].replace(',', ''))))
            nitcnt += 1
        elif row[3] in nowon:
            twn += float(int(row[6].replace(',', ''))/(int(row[4].replace(',', '')) + int(row[6].replace(',', ''))))
            twncnt += 1
        elif row[3] in dobong:
            ton += float(int(row[6].replace(',', ''))/(int(row[4].replace(',', '')) + int(row[6].replace(',', ''))))
            toncnt += 1
        elif row[3] in gangdong:
            tto += float(int(row[6].replace(',', ''))/(int(row[4].replace(',', '')) + int(row[6].replace(',', ''))))
            ttocnt += 1
        elif row[3] in gangseo:
            tth += float(int(row[6].replace(',', ''))/(int(row[4].replace(',', '')) + int(row[6].replace(',', ''))))
            tthcnt += 1
        elif row[3] in jungrang:
            tfo += float(int(row[6].replace(',', ''))/(int(row[4].replace(',', '')) + int(row[6].replace(',', ''))))
            tfocnt += 1
        elif row[3] in geumchun:
            tfi += float(int(row[6].replace(',', ''))/(int(row[4].replace(',', '')) + int(row[6].replace(',', ''))))
            tficnt += 1
    one = one/onecnt
    ddm.append(float(one))
    two = two/twocnt
    jg.append(float(two))
    thr = thr/thrcnt
    jr.append(float(thr))
    fou = fou/foucnt
    gr.append(float(fou))
    fiv = fiv/fivcnt
    ydp.append(float(fiv))
    six = six/sixcnt
    sd.append(float(six))
    sev = sev/sevcnt
    sp.append(float(sev))
    eig = eig/eigcnt
    sch.append(float(eig))
    nin = nin/nincnt
    gj.append(float(nin))
    ten = ten/tencnt
    ga.append(float(ten))
    ele = ele/elecnt
    yc.append(float(ele))
    twe = twe/twecnt
    dj.append(float(twe))
    tht = tht/thtcnt
    gn.append(float(tht))
    fot = fot/fotcnt
    mp.append(float(fot))
    fif = fif/fifcnt
    sd.append(float(fif))
    sit = sit/sitcnt
    ep.append(float(sit))
    set = set/setcnt
    gb.append(float(set))
    eit = eit/eitcnt
    ys.append(float(eig))
    nit = nit/nitcnt
    sb.append(float(nit))
    twn = twn/twncnt
    nw.append(float(twn))
    ton = ton/toncnt
    db.append(float(ton))
    tto = tto/ttocnt
    gd.append(float(tto))
    tth = tth/tthcnt
    gs.append(float(tth))
    tfo = tfo/tfocnt
    jl.append(float(tfo))
    tfi = tfi/tficnt
    gch.append(float(tfi))

df = pd.DataFrame(jr, index=datelist, columns=['무임승차'])
print(df)
plot_acf(df)
plot_pacf(df)
# plt.show()
model = ARIMA(df, order=(0, 1, 1))
model_fit = model.fit(trend='nc', full_output=True, disp=1)
print(model_fit.summary())

model_fit.plot_predict()
plt.rc('font', family='Malgun Gothic')
plt.show()
fore = model_fit.forecast(steps=1)
print(fore)