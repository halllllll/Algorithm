## 問題名
Transformation
## キーワード
文字列操作
## 概要
文字列とオペレーションの回数とオペレーションが与えられるからオペレーションに従って文字列操作しろ
## 方針と読解
やるだけ。reverseしたりreplaceしたり。特にreverseは「何文字目から何文字目までをreverse」みたいなやつなので組み込みのreverseがある言語でもそんなオプションねぇだろうというやつで気をつける。<br>
オペレーションはswitchなりなんなりでお好きに

## 参考
revsereはこれをパクってちょっと手を加えた

[Go example projects](https://github.com/golang/example/blob/master/stringutil/reverse.go)

```go
func Reverse(s string, a int, b int) string {
	r := []rune(s)
	for i, j := a, b; i < (a+b)/2+1; i, j = i+1, j-1 {
		r[i], r[j] = r[j], r[i]
	}
	return string(r)
}
```

## 所感
あっはい