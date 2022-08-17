from datetime import datetime, timedelta
import random
yesterday = datetime.today() - timedelta(41)
H = random.randrange(20,24)
M = random.randrange(0,60)
S = random.randrange(0,60)
dayto = datetime.today().strftime('%A %d %B %Y ' + str(H)+':'+ str(M) +':'+ str(S) + ' KST')
dayyester = yesterday.strftime('%A %d %B %Y ' + str(H)+':'+ str(M) +':'+ str(S) + ' KST')
print("# today")
print('git commit --amend --no-edit --date "' + dayto + '"' )
print('GIT_COMMITTER_DATE="' + dayto + '" git commit --amend --no-edit')
print("# yesterday")
print('git commit --amend --no-edit --date "' + dayyester + '"' )
print('GIT_COMMITTER_DATE="' + dayyester + '" git commit --amend --no-edit')
# git commit --amend --no-edit --date "Thursday 12 May 2022 23:39:21 KST"
# GIT_COMMITTER_DATE="Thursday 12 May 2022 23:39:21 KST" git commit --amend --no-edit