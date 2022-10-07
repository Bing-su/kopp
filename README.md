# kopp

KOrean PostPositions, kopp [ko-pi-pi]

파이썬 한글 조사 처리

## Install

```bash
pip install kopp
```

## Usage

```bash
# shell
kopp '아노아(이)가 공격했다'
```
```
아노아가 공격했다
```

```python
>>> from kopp import kopp

>>> print(kopp("서울(으)로 부산(으)로."))
'서울로 부산으로'
```
