#by wxyinasilent
#2022/11/19
#github/wxyinasilent555

import cv2

def bit2num(pixcels):
   output_val = 0
   for i, pix in enumerate(pixcels):
      if pix > 128: # 白色
         output_val += pow(2, i)
   return output_val

def main():
   video_path = 'cxk.mp4' # bad apple视频文件
   cap = cv2.VideoCapture(video_path) # 打开视频
   cnt = 0
   fout = open('cxk.txt', 'w') # 解码后保存的文件
   while True:
      ret, frame = cap.read()       # 一帧一帧的读取
      if not ret:
         break
      cnt += 1
      frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) # 转换为灰度的画面
      frame = cv2.resize(frame, (128, 64))  # 图像尺寸调整到128*64大小
      convert_val = []
      for row in range(0, 8):   # page0 ~ page7
         for col in range(0, 128): # seg0 ~ seg127
            cur_data = frame[row*8: row*8+8, col] # 取出对应的8个像素点
            convert_val.append(str(bit2num(cur_data))) # 转换成8位的数据

      fout.write("%s\n"%(','.join(convert_val)))

      # cv2.imshow("capture", frame)  #显示画面
      # if cv2.waitKey(30) & 0xff == ord('q'): #按q退出
      #    break

if __name__ =='__main__':
   main()