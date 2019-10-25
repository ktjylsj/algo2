import csv
import pandas as pd
import datetime as dt
import matplotlib.pyplot as plt
from statsmodels.tsa.arima_model import ARIMA
import numpy as np

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
    one2 = 0
    onecnt = 0
    two = 0
    two2 = 0
    twocnt = 0
    thr = 0
    thr2 = 0
    thrcnt = 0
    fou = 0
    fou2 = 0
    foucnt = 0
    fiv = 0
    fiv2 = 0
    fivcnt = 0
    six = 0
    six2 = 0
    sixcnt = 0
    sev = 0
    sev2 = 0
    sevcnt = 0
    eig = 0
    eig2 = 0
    eigcnt = 0
    nin = 0
    nin2 = 0
    nincnt = 0
    ten = 0
    ten2 = 0
    tencnt = 0
    ele = 0
    ele2 = 0
    elecnt = 0
    twe = 0
    twe2 = 0
    twecnt = 0
    tht = 0
    tht2 = 0
    thtcnt = 0
    fot = 0
    fot2 = 0
    fotcnt = 0
    fif = 0
    fif2 = 0
    fifcnt = 0
    sit = 0
    sit2 = 0
    sitcnt = 0
    set = 0
    set2 = 0
    setcnt = 0
    eit = 0
    eit2 = 0
    eitcnt = 0
    nit = 0
    nit2 = 0
    nitcnt = 0
    twn = 0
    twn2 = 0
    twncnt = 0
    ton = 0
    ton2 = 0
    toncnt = 0
    tto = 0
    tto2 = 0
    ttocnt = 0
    tth = 0
    tth2 = 0
    tthcnt = 0
    tfo = 0
    tfo2 = 0
    tfocnt = 0
    tfi = 0
    tfi2 = 0
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
        # 1 무임
        # 2 유임
        if row[3] in dongdae:
            one += int(row[6].replace(',', ''))
            one2 += int(row[4].replace(',', ''))
            onecnt += 1
        elif row[3] in junggu:
            two += int(row[6].replace(',', ''))
            two2 += int(row[4].replace(',', ''))
            twocnt += 1
        elif row[3] in jongro:
            thr += int(row[6].replace(',', ''))
            thr2 += int(row[4].replace(',', ''))
            thrcnt += 1
        elif row[3] in guro:
            fou += int(row[6].replace(',', ''))
            fou2 += int(row[4].replace(',', ''))
            foucnt += 1
        elif row[3] in yeongdeong:
            fiv += int(row[6].replace(',', ''))
            fiv2 += int(row[4].replace(',', ''))
            fivcnt += 1
        elif row[3] in sungdong:
            six += int(row[6].replace(',', ''))
            six2 += int(row[4].replace(',', ''))
            sixcnt += 1
        elif row[3] in songpa:
            sev += int(row[6].replace(',', ''))
            sev2 += int(row[4].replace(',', ''))
            sevcnt += 1
        elif row[3] in seocho:
            eig += int(row[6].replace(',', ''))
            eig2 += int(row[4].replace(',', ''))
            eigcnt += 1
        elif row[3] in gwangjin:
            nin += int(row[6].replace(',', ''))
            nin2 += int(row[4].replace(',', ''))
            nincnt += 1
        elif row[3] in gwanack:
            ten += int(row[6].replace(',', ''))
            ten2 += int(row[4].replace(',', ''))
            tencnt += 1
        elif row[3] in yangcheon:
            ele += int(row[6].replace(',', ''))
            ele2 += int(row[4].replace(',', ''))
            elecnt += 1
        elif row[3] in dongjak:
            twe += int(row[6].replace(',', ''))
            twe2 += int(row[4].replace(',', ''))
            twecnt += 1
        elif row[3] in gangnam:
            tht += int(row[6].replace(',', ''))
            tht2 += int(row[4].replace(',', ''))
            thtcnt += 1
        elif row[3] in mapo:
            fot += int(row[6].replace(',', ''))
            fot2 += int(row[4].replace(',', ''))
            fotcnt += 1
        elif row[3] in seodae:
            fif += int(row[6].replace(',', ''))
            fif2 += int(row[4].replace(',', ''))
            fifcnt += 1
        elif row[3] in eunpung:
            sit += int(row[6].replace(',', ''))
            sit2 += int(row[4].replace(',', ''))
            sitcnt += 1
        elif row[3] in gangbuk:
            set += int(row[6].replace(',', ''))
            set2 += int(row[4].replace(',', ''))
            setcnt += 1
        elif row[3] in yongsan:
            eit += int(row[6].replace(',', ''))
            eit2 += int(row[4].replace(',', ''))
            eitcnt += 1
        elif row[3] in sungbuk:
            nit += int(row[6].replace(',', ''))
            nit2 += int(row[4].replace(',', ''))
            nitcnt += 1
        elif row[3] in nowon:
            twn += int(row[6].replace(',', ''))
            twn2 += int(row[4].replace(',', ''))
            twncnt += 1
        elif row[3] in dobong:
            ton += int(row[6].replace(',', ''))
            ton2 += int(row[4].replace(',', ''))
            toncnt += 1
        elif row[3] in gangdong:
            tto += int(row[6].replace(',', ''))
            tto2 += int(row[4].replace(',', ''))
            ttocnt += 1
        elif row[3] in gangseo:
            tth += int(row[6].replace(',', ''))
            tth2 += int(row[4].replace(',', ''))
            tthcnt += 1
        elif row[3] in jungrang:
            tfo += int(row[6].replace(',', ''))
            tfo2 += int(row[4].replace(',', ''))
            tfocnt += 1
        elif row[3] in geumchun:
            tfi += int(row[6].replace(',', ''))
            tfi2 += int(row[4].replace(',', ''))
            tficnt += 1
    one = one/onecnt
    one2 = one2/onecnt
    ddm.append(float(one))
    ddm.append(float(one2))
    two = two/twocnt
    two2 = two2/twocnt
    jg.append(float(two))
    jg.append(float(two2))
    thr = thr/thrcnt
    thr2 = thr2/thrcnt
    jr.append(float(thr))
    jr.append(float(thr2))
    fou = fou/foucnt
    fou2 = fou2/foucnt
    gr.append(float(fou))
    gr.append(float(fou2))
    fiv = fiv/fivcnt
    fiv2 = fiv2/fivcnt
    ydp.append(float(fiv))
    ydp.append(float(fiv2))
    six = six/sixcnt
    six2 = six2/sixcnt
    sd.append(float(six))
    sd.append(float(six2))
    sev = sev/sevcnt
    sev2 = sev2/sevcnt
    sp.append(float(sev))
    sp.append(float(sev2))
    eig = eig/eigcnt
    eig2 = eig2/eigcnt
    sch.append(float(eig))
    sch.append(float(eig2))
    nin = nin/nincnt
    gj.append(float(nin))
    ten = ten/tencnt
    ten2 = ten2/tencnt
    ga.append(float(ten))
    ga.append(float(ten2))
    ele = ele/elecnt
    ele2= ele2/elecnt
    yc.append(float(ele))
    yc.append(float(ele2))
    twe = twe/twecnt
    twe2 = twe2/twecnt
    dj.append(float(twe))
    dj.append(float(twe2))
    tht = tht/thtcnt
    tht2 = tht2/thtcnt
    gn.append(float(tht))
    gn.append(float(tht2))
    fot = fot/fotcnt
    fot2 = fot2/fotcnt
    mp.append(float(fot))
    mp.append(float(fot2))
    fif = fif/fifcnt
    fif2 = fif2/fifcnt
    sd.append(float(fif))
    sd.append(float(fif2))
    sit = sit/sitcnt
    sit2 = sit2/sitcnt
    ep.append(float(sit))
    ep.append(float(sit2))
    set = set/setcnt
    set2 = set2/setcnt
    gb.append(float(set))
    gb.append(float(set2))
    eit = eit/eitcnt
    eit2 = eit2/eitcnt
    ys.append(float(eit))
    ys.append(float(eit2))
    nit = nit/nitcnt
    nit2 = nit2/nitcnt
    sb.append(float(nit))
    sb.append(float(nit2))
    twn = twn/twncnt
    twn2 = twn2/twncnt
    nw.append(float(twn))
    nw.append(float(twn2))
    ton = ton/toncnt
    ton2 = ton2/toncnt
    db.append(float(ton))
    db.append(float(ton2))
    tto = tto/ttocnt
    tto2 = tto2/ttocnt
    gd.append(float(tto))
    gd.append(float(tto2))
    tth = tth/tthcnt
    tth2 = tth2/tthcnt
    gs.append(float(tth))
    gs.append(float(tth2))
    tfo = tfo/tfocnt
    tfo2 = tfo2/tfocnt
    jl.append(float(tfo))
    jl.append(float(tfo2))
    tfi = tfi/tficnt
    tfi2 = tfi2/tficnt
    gch.append(float(tfi))
    gch.append(float(tfi2))

for yr in range(2016, 2019):
    for i in range(1, 13):
        one = 0
        one2 = 0
        onecnt = 0
        two = 0
        two2 = 0
        twocnt = 0
        thr = 0
        thr2 = 0
        thrcnt = 0
        fou = 0
        fou2 = 0
        foucnt = 0
        fiv = 0
        fiv2 = 0
        fivcnt = 0
        six = 0
        six2 = 0
        sixcnt = 0
        sev = 0
        sev2 = 0
        sevcnt = 0
        eig = 0
        eig2 = 0
        eigcnt = 0
        nin = 0
        nin2 = 0
        nincnt = 0
        ten = 0
        ten2 = 0
        tencnt = 0
        ele = 0
        ele2 = 0
        elecnt = 0
        twe = 0
        twe2 = 0
        twecnt = 0
        tht = 0
        tht2 = 0
        thtcnt = 0
        fot = 0
        fot2 = 0
        fotcnt = 0
        fif = 0
        fif2 = 0
        fifcnt = 0
        sit = 0
        sit2 = 0
        sitcnt = 0
        set = 0
        set2 = 0
        setcnt = 0
        eit = 0
        eit2 = 0
        eitcnt = 0
        nit = 0
        nit2 = 0
        nitcnt = 0
        twn = 0
        twn2 = 0
        twncnt = 0
        ton = 0
        ton2 = 0
        toncnt = 0
        tto = 0
        tto2 = 0
        ttocnt = 0
        tth = 0
        tth2 = 0
        tthcnt = 0
        tfo = 0
        tfo2 = 0
        tfocnt = 0
        tfi = 0
        tfi2 = 0
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
                one += int(row[6].replace(',', ''))
                one2 += int(row[4].replace(',', ''))
                onecnt += 1
            elif row[3] in junggu:
                two += int(row[6].replace(',', ''))
                two2 += int(row[4].replace(',', ''))
                twocnt += 1
            elif row[3] in jongro:
                thr += int(row[6].replace(',', ''))
                thr2 += int(row[4].replace(',', ''))
                thrcnt += 1
            elif row[3] in guro:
                fou += int(row[6].replace(',', ''))
                fou2 += int(row[4].replace(',', ''))
                foucnt += 1
            elif row[3] in yeongdeong:
                fiv += int(row[6].replace(',', ''))
                fiv2 += int(row[4].replace(',', ''))
                fivcnt += 1
            elif row[3] in sungdong:
                six += int(row[6].replace(',', ''))
                six2 += int(row[4].replace(',', ''))
                sixcnt += 1
            elif row[3] in songpa:
                sev += int(row[6].replace(',', ''))
                sev2 += int(row[4].replace(',', ''))
                sevcnt += 1
            elif row[3] in seocho:
                eig += int(row[6].replace(',', ''))
                eig2 += int(row[4].replace(',', ''))
                eigcnt += 1
            elif row[3] in gwangjin:
                nin += int(row[6].replace(',', ''))
                nin2 += int(row[4].replace(',', ''))
                nincnt += 1
            elif row[3] in gwanack:
                ten += int(row[6].replace(',', ''))
                ten2 += int(row[4].replace(',', ''))
                tencnt += 1
            elif row[3] in yangcheon:
                ele += int(row[6].replace(',', ''))
                ele2 += int(row[4].replace(',', ''))
                elecnt += 1
            elif row[3] in dongjak:
                twe += int(row[6].replace(',', ''))
                twe2 += int(row[4].replace(',', ''))
                twecnt += 1
            elif row[3] in gangnam:
                tht += int(row[6].replace(',', ''))
                tht2 += int(row[4].replace(',', ''))
                thtcnt += 1
            elif row[3] in mapo:
                fot += int(row[6].replace(',', ''))
                fot2 += int(row[4].replace(',', ''))
                fotcnt += 1
            elif row[3] in seodae:
                fif += int(row[6].replace(',', ''))
                fif2 += int(row[4].replace(',', ''))
                fifcnt += 1
            elif row[3] in eunpung:
                sit += int(row[6].replace(',', ''))
                sit2 += int(row[4].replace(',', ''))
                sitcnt += 1
            elif row[3] in gangbuk:
                set += int(row[6].replace(',', ''))
                set2 += int(row[4].replace(',', ''))
                setcnt += 1
            elif row[3] in yongsan:
                eit += int(row[6].replace(',', ''))
                eit2 += int(row[4].replace(',', ''))
                eitcnt += 1
            elif row[3] in sungbuk:
                nit += int(row[6].replace(',', ''))
                nit2 += int(row[4].replace(',', ''))
                nitcnt += 1
            elif row[3] in nowon:
                twn += int(row[6].replace(',', ''))
                twn2 += int(row[4].replace(',', ''))
                twncnt += 1
            elif row[3] in dobong:
                ton += int(row[6].replace(',', ''))
                ton2 += int(row[4].replace(',', ''))
                toncnt += 1
            elif row[3] in gangdong:
                tto += int(row[6].replace(',', ''))
                tto2 += int(row[4].replace(',', ''))
                ttocnt += 1
            elif row[3] in gangseo:
                tth += int(row[6].replace(',', ''))
                tth2 += int(row[4].replace(',', ''))
                tthcnt += 1
            elif row[3] in jungrang:
                tfo += int(row[6].replace(',', ''))
                tfo2 += int(row[4].replace(',', ''))
                tfocnt += 1
            elif row[3] in geumchun:
                tfi += int(row[6].replace(',', ''))
                tfi2 += int(row[4].replace(',', ''))
                tficnt += 1
        one = one / onecnt
        one2 = one2 / onecnt
        ddm.append(float(one))
        ddm.append(float(one2))
        two = two / twocnt
        two2 = two2 / twocnt
        jg.append(float(two))
        jg.append(float(two2))
        thr = thr / thrcnt
        thr2 = thr2 / thrcnt
        jr.append(float(thr))
        jr.append(float(thr2))
        fou = fou / foucnt
        fou2 = fou2 / foucnt
        gr.append(float(fou))
        gr.append(float(fou2))
        fiv = fiv / fivcnt
        fiv2 = fiv2 / fivcnt
        ydp.append(float(fiv))
        ydp.append(float(fiv2))
        six = six / sixcnt
        six2 = six2 / sixcnt
        sd.append(float(six))
        sd.append(float(six2))
        sev = sev / sevcnt
        sev2 = sev2 / sevcnt
        sp.append(float(sev))
        sp.append(float(sev2))
        eig = eig / eigcnt
        eig2 = eig2 / eigcnt
        sch.append(float(eig))
        sch.append(float(eig2))
        nin = nin / nincnt
        gj.append(float(nin))
        ten = ten / tencnt
        ten2 = ten2 / tencnt
        ga.append(float(ten))
        ga.append(float(ten2))
        ele = ele / elecnt
        ele2 = ele2 / elecnt
        yc.append(float(ele))
        yc.append(float(ele2))
        twe = twe / twecnt
        twe2 = twe2 / twecnt
        dj.append(float(twe))
        dj.append(float(twe2))
        tht = tht / thtcnt
        tht2 = tht2 / thtcnt
        gn.append(float(tht))
        gn.append(float(tht2))
        fot = fot / fotcnt
        fot2 = fot2 / fotcnt
        mp.append(float(fot))
        mp.append(float(fot2))
        fif = fif / fifcnt
        fif2 = fif2 / fifcnt
        sd.append(float(fif))
        sd.append(float(fif2))
        sit = sit / sitcnt
        sit2 = sit2 / sitcnt
        ep.append(float(sit))
        ep.append(float(sit2))
        set = set / setcnt
        set2 = set2 / setcnt
        gb.append(float(set))
        gb.append(float(set2))
        eit = eit / eitcnt
        eit2 = eit2 / eitcnt
        ys.append(float(eit))
        ys.append(float(eit2))
        nit = nit / nitcnt
        nit2 = nit2 / nitcnt
        sb.append(float(nit))
        sb.append(float(nit2))
        twn = twn / twncnt
        twn2 = twn2 / twncnt
        nw.append(float(twn))
        nw.append(float(twn2))
        ton = ton / toncnt
        ton2 = ton2 / toncnt
        db.append(float(ton))
        db.append(float(ton2))
        tto = tto / ttocnt
        tto2 = tto2 / ttocnt
        gd.append(float(tto))
        gd.append(float(tto2))
        tth = tth / tthcnt
        tth2 = tth2 / tthcnt
        gs.append(float(tth))
        gs.append(float(tth2))
        tfo = tfo / tfocnt
        tfo2 = tfo2 / tfocnt
        jl.append(float(tfo))
        jl.append(float(tfo2))
        tfi = tfi / tficnt
        tfi2 = tfi2 / tficnt
        gch.append(float(tfi))
        gch.append(float(tfi2))
            
for i in range(1, 10):
    one = 0
    one2 = 0
    onecnt = 0
    two = 0
    two2 = 0
    twocnt = 0
    thr = 0
    thr2 = 0
    thrcnt = 0
    fou = 0
    fou2 = 0
    foucnt = 0
    fiv = 0
    fiv2 = 0
    fivcnt = 0
    six = 0
    six2 = 0
    sixcnt = 0
    sev = 0
    sev2 = 0
    sevcnt = 0
    eig = 0
    eig2 = 0
    eigcnt = 0
    nin = 0
    nin2 = 0
    nincnt = 0
    ten = 0
    ten2 = 0
    tencnt = 0
    ele = 0
    ele2 = 0
    elecnt = 0
    twe = 0
    twe2 = 0
    twecnt = 0
    tht = 0
    tht2 = 0
    thtcnt = 0
    fot = 0
    fot2 = 0
    fotcnt = 0
    fif = 0
    fif2 = 0
    fifcnt = 0
    sit = 0
    sit2 = 0
    sitcnt = 0
    set = 0
    set2 = 0
    setcnt = 0
    eit = 0
    eit2 = 0
    eitcnt = 0
    nit = 0
    nit2 = 0
    nitcnt = 0
    twn = 0
    twn2 = 0
    twncnt = 0
    ton = 0
    ton2 = 0
    toncnt = 0
    tto = 0
    tto2 = 0
    ttocnt = 0
    tth = 0
    tth2 = 0
    tthcnt = 0
    tfo = 0
    tfo2 = 0
    tfocnt = 0
    tfi = 0
    tfi2 = 0
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
            one += int(row[6].replace(',', ''))
            one2 += int(row[4].replace(',', ''))
            onecnt += 1
        elif row[3] in junggu:
            two += int(row[6].replace(',', ''))
            two2 += int(row[4].replace(',', ''))
            twocnt += 1
        elif row[3] in jongro:
            thr += int(row[6].replace(',', ''))
            thr2 += int(row[4].replace(',', ''))
            thrcnt += 1
        elif row[3] in guro:
            fou += int(row[6].replace(',', ''))
            fou2 += int(row[4].replace(',', ''))
            foucnt += 1
        elif row[3] in yeongdeong:
            fiv += int(row[6].replace(',', ''))
            fiv2 += int(row[4].replace(',', ''))
            fivcnt += 1
        elif row[3] in sungdong:
            six += int(row[6].replace(',', ''))
            six2 += int(row[4].replace(',', ''))
            sixcnt += 1
        elif row[3] in songpa:
            sev += int(row[6].replace(',', ''))
            sev2 += int(row[4].replace(',', ''))
            sevcnt += 1
        elif row[3] in seocho:
            eig += int(row[6].replace(',', ''))
            eig2 += int(row[4].replace(',', ''))
            eigcnt += 1
        elif row[3] in gwangjin:
            nin += int(row[6].replace(',', ''))
            nin2 += int(row[4].replace(',', ''))
            nincnt += 1
        elif row[3] in gwanack:
            ten += int(row[6].replace(',', ''))
            ten2 += int(row[4].replace(',', ''))
            tencnt += 1
        elif row[3] in yangcheon:
            ele += int(row[6].replace(',', ''))
            ele2 += int(row[4].replace(',', ''))
            elecnt += 1
        elif row[3] in dongjak:
            twe += int(row[6].replace(',', ''))
            twe2 += int(row[4].replace(',', ''))
            twecnt += 1
        elif row[3] in gangnam:
            tht += int(row[6].replace(',', ''))
            tht2 += int(row[4].replace(',', ''))
            thtcnt += 1
        elif row[3] in mapo:
            fot += int(row[6].replace(',', ''))
            fot2 += int(row[4].replace(',', ''))
            fotcnt += 1
        elif row[3] in seodae:
            fif += int(row[6].replace(',', ''))
            fif2 += int(row[4].replace(',', ''))
            fifcnt += 1
        elif row[3] in eunpung:
            sit += int(row[6].replace(',', ''))
            sit2 += int(row[4].replace(',', ''))
            sitcnt += 1
        elif row[3] in gangbuk:
            set += int(row[6].replace(',', ''))
            set2 += int(row[4].replace(',', ''))
            setcnt += 1
        elif row[3] in yongsan:
            eit += int(row[6].replace(',', ''))
            eit2 += int(row[4].replace(',', ''))
            eitcnt += 1
        elif row[3] in sungbuk:
            nit += int(row[6].replace(',', ''))
            nit2 += int(row[4].replace(',', ''))
            nitcnt += 1
        elif row[3] in nowon:
            twn += int(row[6].replace(',', ''))
            twn2 += int(row[4].replace(',', ''))
            twncnt += 1
        elif row[3] in dobong:
            ton += int(row[6].replace(',', ''))
            ton2 += int(row[4].replace(',', ''))
            toncnt += 1
        elif row[3] in gangdong:
            tto += int(row[6].replace(',', ''))
            tto2 += int(row[4].replace(',', ''))
            ttocnt += 1
        elif row[3] in gangseo:
            tth += int(row[6].replace(',', ''))
            tth2 += int(row[4].replace(',', ''))
            tthcnt += 1
        elif row[3] in jungrang:
            tfo += int(row[6].replace(',', ''))
            tfo2 += int(row[4].replace(',', ''))
            tfocnt += 1
        elif row[3] in geumchun:
            tfi += int(row[6].replace(',', ''))
            tfi2 += int(row[4].replace(',', ''))
            tficnt += 1
    one = one / onecnt
    one2 = one2 / onecnt
    ddm.append(float(one))
    ddm.append(float(one2))
    two = two / twocnt
    two2 = two2 / twocnt
    jg.append(float(two))
    jg.append(float(two2))
    thr = thr / thrcnt
    thr2 = thr2 / thrcnt
    jr.append(float(thr))
    jr.append(float(thr2))
    fou = fou / foucnt
    fou2 = fou2 / foucnt
    gr.append(float(fou))
    gr.append(float(fou2))
    fiv = fiv / fivcnt
    fiv2 = fiv2 / fivcnt
    ydp.append(float(fiv))
    ydp.append(float(fiv2))
    six = six / sixcnt
    six2 = six2 / sixcnt
    sd.append(float(six))
    sd.append(float(six2))
    sev = sev / sevcnt
    sev2 = sev2 / sevcnt
    sp.append(float(sev))
    sp.append(float(sev2))
    eig = eig / eigcnt
    eig2 = eig2 / eigcnt
    sch.append(float(eig))
    sch.append(float(eig2))
    nin = nin / nincnt
    gj.append(float(nin))
    ten = ten / tencnt
    ten2 = ten2 / tencnt
    ga.append(float(ten))
    ga.append(float(ten2))
    ele = ele / elecnt
    ele2 = ele2 / elecnt
    yc.append(float(ele))
    yc.append(float(ele2))
    twe = twe / twecnt
    twe2 = twe2 / twecnt
    dj.append(float(twe))
    dj.append(float(twe2))
    tht = tht / thtcnt
    tht2 = tht2 / thtcnt
    gn.append(float(tht))
    gn.append(float(tht2))
    fot = fot / fotcnt
    fot2 = fot2 / fotcnt
    mp.append(float(fot))
    mp.append(float(fot2))
    fif = fif / fifcnt
    fif2 = fif2 / fifcnt
    sd.append(float(fif))
    sd.append(float(fif2))
    sit = sit / sitcnt
    sit2 = sit2 / sitcnt
    ep.append(float(sit))
    ep.append(float(sit2))
    set = set / setcnt
    set2 = set2 / setcnt
    gb.append(float(set))
    gb.append(float(set2))
    eit = eit / eitcnt
    eit2 = eit2 / eitcnt
    ys.append(float(eit))
    ys.append(float(eit2))
    nit = nit / nitcnt
    nit2 = nit2 / nitcnt
    sb.append(float(nit))
    sb.append(float(nit2))
    twn = twn / twncnt
    twn2 = twn2 / twncnt
    nw.append(float(twn))
    nw.append(float(twn2))
    ton = ton / toncnt
    ton2 = ton2 / toncnt
    db.append(float(ton))
    db.append(float(ton2))
    tto = tto / ttocnt
    tto2 = tto2 / ttocnt
    gd.append(float(tto))
    gd.append(float(tto2))
    tth = tth / tthcnt
    tth2 = tth2 / tthcnt
    gs.append(float(tth))
    gs.append(float(tth2))
    tfo = tfo / tfocnt
    tfo2 = tfo2 / tfocnt
    jl.append(float(tfo))
    jl.append(float(tfo2))
    tfi = tfi / tficnt
    tfi2 = tfi2 / tficnt
    gch.append(float(tfi))
    gch.append(float(tfi2))

# 비율
prate = []
# 65세이상
orate = []
# 65세 미만
urate = []

for i in range(0, len(jr)):    # 구를 넣음
    temp = jr[i]
    if i % 2 == 0:
        orate.append(temp)
    else:
        urate.append(temp)

for i in range(0, len(orate)):
    prate.append(orate[i] / (orate[i] + urate[i]))

# 비율
# DataFrame안에 첫번째 인자로 넣습니다
df = pd.DataFrame(prate, index=datelist, columns=['value'])
model = ARIMA(df, order=(0, 1, 1))
model_fit = model.fit(trend='nc', full_output=True, disp=1)
# model_fit.plot_predict()
# plt.show()
fore = model_fit.forecast(steps=1)
temp = list(fore)
output1 = float(temp[0])
output1 = output1 * 100

# 무임승차
df = pd.DataFrame(orate, index=datelist, columns=['value'])
model = ARIMA(df, order=(0, 1, 1))
model_fit = model.fit(trend='nc', full_output=True, disp=1)
# model_fit.plot_predict()
# plt.show()
fore = model_fit.forecast(steps=1)
temp = list(fore)
output2 = float(temp[0])

# 유임승차
df = pd.DataFrame(urate, index=datelist, columns=['value'])
model = ARIMA(df, order=(0, 1, 1))
model_fit = model.fit(trend='nc', full_output=True, disp=1)
# model_fit.plot_predict()
# plt.show()
fore = model_fit.forecast(steps=1)
temp = list(fore)
output3 = float(temp[0])

print("다음달 무임승차 예측 " + format(output2, ".2f") + "명")
print("다음달 유임승차 예측 " + format(output3, ".2f") + "명")
print("다음달 무임승차 예측 비율 " + format(output1, ".2f") + "%")
