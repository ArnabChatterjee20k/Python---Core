import requests as req
url = "https://rr1---sn-gwpa-gq2z.googlevideo.com/videoplayback?expire=1644710843&ei=W_cHYoefGraQg8UPndS52A4&ip=2409%3A4061%3A601%3Aa09c%3A65e2%3A3ff3%3Aaa1c%3Ab059&id=o-ACYiV3E4ZyybQKOhhrFTQr_-1xwwBSUzjxgcpiLdU48j&itag=251&source=youtube&requiressl=yes&mh=zY&mm=31%2C29&mn=sn-gwpa-gq2z%2Csn-qxaeenls&ms=au%2Crdu&mv=m&mvi=1&pcm2cms=yes&pl=41&initcwndbps=185000&vprv=1&mime=audio%2Fwebm&ns=3plDn2yzTatlRHYMbY42CFoG&gir=yes&clen=13243055&dur=892.481&lmt=1563293094605199&mt=1644688843&fvip=1&keepalive=yes&fexp=24001373%2C24007246&c=WEB&txp=2301222&n=i5Qnm9YLItVwSQ&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cvprv%2Cmime%2Cns%2Cgir%2Cclen%2Cdur%2Clmt&sig=AOq0QJ8wRQIgSASFLJd8ohFDeOiZlznjy2hQz6mNZ_KyPkHGrUS9tlICIQDJ2WxB0EXBamkoM5M-AeqjxPG6mAEKMIXGVhH4TQACgw%3D%3D&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpcm2cms%2Cpl%2Cinitcwndbps&lsig=AG3C_xAwRQIhAKtWZudkbIyst0ybOOzunJllZFXS9qoMT0RPiHS9jxKZAiBtR6LINAKT4enqjpZC2KJ4aQ5KEih2knTL7KN4nSuDmw%3D%3D&alr=yes&cpn=Y35LifeeftB6HR1q&cver=2.20220211.01.00&range=0-999999999999999999999&rn=9&rbuf=19458"
res = req.get(url)
print (res.status_code)