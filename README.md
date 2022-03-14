
# Usage
```python train.py --batch-size 64 --data='./path/to/data.yaml' --device 0,1,2,3```

# Predict & Save result
```python val.py --data='./path/to/data.yaml' --weights ../result/runs/train/exp9/weights/last.pt --save-txt --project=../result/runs/val/ --name=exp2```

# Evaluation
```python eval.py```
