# pylookwhat
  
有時候必須參考其它專案的設定來完成一些特定的工作，
可以用 execfile 來執行設定檔( conf.py )
但是將會遇到的問題有 
1. 相關套件未安裝
2. 相對的套件不在 sys.path 裡
3. 套件名稱重複

有了 pylookwhat 之後這些問題都將輕鬆的解決


    import pylookwhat
    
    what = {}
    lookwhat = [ 'A', 'B'  ]
    filename = 'what.py'
    pylookwhat.lookwhat( filename, what, lookwhat  )
    
    print what

