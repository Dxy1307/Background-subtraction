# nó chọn số lượng phân phối gaussian thích hợp cho mỗi pixel. Trọng số của hỗn hợp thể hiện tỷ lệ thời gian mà những màu đó ở trong cảnh. Màu nền là những màu tồn tại lâu hơn và tĩnh hơn.

import numpy as np
import cv2

cap = cv2.VideoCapture('video/input/slow.flv')

fgbg = cv2.createBackgroundSubtractorMOG2()

while(1):
    ret, frame = cap.read()

    fgmask = fgbg.apply(frame)

    cv2.imshow('frame', fgmask)
    k = cv2.waitKey(30) & 0xFF
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()