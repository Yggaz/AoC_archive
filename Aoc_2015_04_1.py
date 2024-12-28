# 282749
# 9962624
import hashlib
done = False
cnt = 282748
while not done:
    cnt += 1
    res = hashlib.md5(('yzbqklnj'+str(cnt)).encode()).hexdigest()[:6]
    done = res == '000000'
print(cnt)
