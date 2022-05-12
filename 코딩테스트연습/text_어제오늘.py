from datetime import datetime, timedelta
import random
yesterday = datetime.today() - timedelta(1)
H = random.randrange(20,24)
M = random.randrange(0,61)
S = random.randrange(0,61)
print(datetime.today().strftime('%A %d %B %Y ' + str(H)+':'+ str(M) +':'+ str(S)))
print(yesterday.strftime('%A %d %B %Y ' + str(H)+':'+ str(M) +':'+ str(S)))

# git commit --amend --no-edit --date "Thursday 12 May 2022 23:39:21 KST"
# GIT_COMMITTER_DATE="Thursday 12 May 2022 23:39:21 KST" git commit --amend --no-edit