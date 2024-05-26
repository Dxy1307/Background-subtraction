# Thuật toán này kết hợp ước tính hình ảnh nền thống kê và phân đoạn Bayes trên mỗi pixel. Nó sử dụng một vài khung hình đầu tiên (120 theo mặc định) để tạo mô hình nền và sử dụng thuật toán phân đoạn tiền cảnh xác suất để xác định các đối tượng tiền cảnh có thể có bằng cách sử dụng suy luận Bayes. Các quan sát mới hơn có trọng số lớn hơn các quan sát cũ để thích ứng với khả năng chiếu sáng thay đổi. Một số hoạt động lọc hình thái học như đóng và mở được thực hiện để loại bỏ nhiễu không mong muốn. Bạn sẽ nhận được một cửa sổ màu đen trong một vài khung hình đầu tiên.

import numpy as np
import cv2

cap = cv2.VideoCapture('video/input/slow.flv')

kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(3,3))
fgbg = cv2.bgsegm.createBackgroundSubtractorGMG()

while(1):
    ret, frame = cap.read()

    fgmask = fgbg.apply(frame)
    fgmask = cv2.morphologyEx(fgmask, cv2.MORPH_OPEN, kernel)

    cv2.imshow('frame', fgmask)
    k = cv2.waitKey(30) & 0xFF
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()