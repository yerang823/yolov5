import glob
from sklearn.metrics import confusion_matrix,accuracy_score,f1_score,precision_score,recall_score

def evaluate(pred_path):
	label_li=glob.glob(path+'*.txt')

	label=[]
	pred=[]
	for i in range(len(label_li)):
		f=open(label_li[i],'r')
		lines=f.readlines()
		#print(lines[0])
		f.close()

		# label
		clas=label_li[i].split('/')[-1][0]
		if clas=='N' or clas=='A':
			label.append(0)
		else:
			label.append(1)

		# pred
		if lines[0][0]=='0':
			pred.append(0)
		else:
			pred.append(1)
			
	cm=confusion_matrix(y_true=label, y_pred=pred)
	acc=accuracy_score(y_true=label, y_pred=pred)
	f1=f1_score(y_true=label, y_pred=pred)
	preci=precision_score(y_true=label, y_pred=pred)
	recall=recall_score(y_true=label, y_pred=pred)

	print(cm)
	print('acc=',acc)
	print('f1=',f1)
	print('preci=',preci)
	print('recall=',recall)
	
if __name__=='__main__':
	cv=44
	print('cv=',cv)
	#path='../result/%d/val/exp/labels/'%cv
	path='../result/%d/val/exp/labels/'%cv
	evaluate(path)
