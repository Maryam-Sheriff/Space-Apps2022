import requests
var = requests.get('https://www.missionjuno.swri.edu/Vault/VaultOutput?VaultID=43845&ts=1656511106')
print(var.content)
with open('E:\PJ40 SOUTHERN CIRCUMPOLAR CYCLONES.png','wb') as f:
    f.write(var.content)



