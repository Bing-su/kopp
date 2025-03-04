# kopp

KOrean PostPositions, kopp [ko-pi-pi]

파이썬 한글 조사 처리

## Install

```bash
pip install kopp
```

## Usage

`"(이)가", "(와)과", "(을)를", "(은)는", "(으)로", "(아)야", "(이)여", "(이)라"`처럼 처리된 한국어 텍스트를
앞에 오는 글자에 맞춰 처리합니다.

터미널에서 바로 사용할 수 있고, 임포트해서 사용할 수도 있습니다.

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

## Reference

[Python 에서 한글 조사 을/를, 이/가, 은/는, 와/과 출력하기](http://dr-roach.com/blog/korean-postposition/)

[myevan/pyjosa](https://github.com/myevan/pyjosa)
