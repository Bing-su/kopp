# kopp

KOrean PostPositions

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
아노가가 공격했다
```

```python
>>> from kopp import kopp

>>> print(kopp("아노아(이)가 공격했다."))
'아노아(이)가 공격했다.'
```
