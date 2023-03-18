import sys
from PyQt5 import QtWidgets
import mainWindow

# __name__は定義済み変数で、モジュールがインポートによって読み込まれた時に
# そのモジュールの名前になる
if __name__ == "__main__":
    # QApplicationはウィンドウシステムを初期化し、
    # コマンドライン引数を使用してアプリケーションオブジェクトを構築する
    app = QtWidgets.QApplication(sys.argv)  # コマンドライン引数を指定

    # 画面を構築するMainWindowクラスのオブジェクトを生成
    win = mainWindow.MainWindow()
    # メインウィンドウを画面に表示
    win.show()
    # メッセージループ（終了の操作が行われるまでは画面を閉じなくする）を開始
    # 終了時に0が返される
    ret = app.exec()
    # exec()の戻り値をシステムに返してプログラムを終了する
    # exec()メソッドが戻り値を返した時点でプログラムは終了するが、
    # 明示的にプログラムを終了してメモリ解放を行うことを宣言している
    sys.exit(ret)
