cv_num=11
path='../result/%d/val/exp2/labels/*.txt'%cv_num

test_li=glob.glob(path)

cnt_n, cnt_a, cnt_p1, cnt_p2, cnt_p3 = 0,0,0,0,0
cnt_n_tp, cnt_a_tp, cnt_p1_tp, cnt_p2_tp, cnt_p3_tp = 0,0,0,0,0


for i in range(len(test_li)):
    f=open(test_li[i],'r')
    label = f.readlines()[0].split(' ')[0]
    f.close()

    gt_clas = test_li[i].split('/')[-1][:2]

    if gt_clas=='N1' or gt_clas=='N2':
        cnt_n+=1
        if label=='0':
            cnt_n_tp+=1

    elif gt_clas=='A1':
        cnt_a+=1
        if label=='0':
            cnt_a_tp+=1

    elif gt_clas=='P1':
        cnt_p1+=1
        if label=='1':
            cnt_p1_tp+=1

    elif gt_clas=='P2':
        cnt_p2+=1
        if label=='1':
            cnt_p2_tp+=1

    elif gt_clas=='P3':
        cnt_p3+=1
        if label=='1':
            cnt_p3_tp+=1

print('    N, A, P1, P2, P3')
print('GT=',cnt_n,cnt_a,cnt_p1,cnt_p2,cnt_p3)
print('TP=',cnt_n_tp,cnt_a_tp,cnt_p1_tp,cnt_p2_tp,cnt_p3_tp)