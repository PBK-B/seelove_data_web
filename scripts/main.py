from scripts.script.getWyyComment import getWyyComment
from scripts.script.wyyCommentDataCleaning import wyyCommentCleaning
import time

if __name__ == '__main__':
    time1 = time.time()
    getWyyComment()
    wyyCommentCleaning()
    time2 = time.time()
    print(time2-time1)
