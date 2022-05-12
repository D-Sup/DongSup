from datetime import datetime, timedelta
yesterday = datetime.today() - timedelta(1)
print(datetime.today().strftime('%A %d %B %Y %H:%M:%S'))
print(yesterday.strftime('%A %d %B %Y %H:%M:%S'))

# git commit --amend --no-edit --date "Sun 3 Oct 2021 12:34:56 KST"
# GIT_COMMITTER_DATE="Sun 3 Oct 2021 12:34:56 KST" git commit --amend --no-edit