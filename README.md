# Result of Detection and Classification
<p align="center">
    <img src="https://user-images.githubusercontent.com/97432613/158125486-bd20ce96-9fef-4611-b7fa-dc4ab16bcb5b.png"  width="80%" height="80%"/>
</p>


# Usage

### Train
```python train.py --batch-size 64 --data='./path/to/data.yaml' --device 0,1,2,3```

### Predict & Save result
```python val.py --data='./path/to/data.yaml' --weights ../result/runs/train/exp9/weights/last.pt --save-txt --project=../result/runs/val/ --name=exp2```

### Evaluation
```python eval.py```
