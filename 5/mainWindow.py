from PyQt5 import QtWidgets
import qt_PitynaUI
import pityna


class MainWindow(QtWidgets.QMainWindow):
    """MainWindowクラス

    QtWidgets.QMainWindowを継承したサブクラス
    UI画面の構築を行う

    Attributes:
        action (bool): ラジオボタンの状態を保持する
        pityna (obj:`pityna`): Pitynaオブジェクトを保持する
        ui (obj:`Ui_MainWindow`): Ui_MainWindowオブジェクトを保持する
    """

    def __init__(self):
        super().__init__()
        self.pityna = pityna.Pityna("pityna")  # Pitynaオブジェクトを生成
        self.action = True  # ラジオボタンの状態を初期化
        self.ui = qt_PitynaUI.Ui_MainWindow()  # Ui_MainWindowオブジェクトを生成

        # setupUi()で画面を構築。MainWindow自身を引数にすることが必要
        self.ui.setupUi(self)

    def putlog(self, str):
        """対話ログをリストに追加する

        Args:
            str (str): ユーザーの入力または応答メッセージをログ用に整形した文字列
        """
        # QListWidgetクラスのaddItem()でログをリストに追加する
        self.ui.listWidgetLog.addItem(str)

    def prompt(self):
        """ピティナのプロンプトを作るメソッド

        Returns:
            str: プロンプトを作る文字列
        """
        # Pitynaクラスのget_name()でオブジェクト名を取得
        p = self.pityna.get_name()
        # 「Responderを表示」がオンならオブジェクト名を付加する
        if self.action == True:
            p += ":" + self.pityna.get_responder_name()

        # プロンプト記号をつけて返す
        return p + "> "

    def buttonTalkSlot(self):
        """「話す」ボタンのイベントハンドラー

        ・Pitynaクラスのdialogue()を実行して応答メッセージを取得
        ・入力文字列および応答メッセージをログに出力
        """
        # ラインエディットのテキストを取得
        value = self.ui.lineEdit.text()

        if not value:
            # 入力エリアが未入力の場合
            self.ui.labelResponse.setText("ヨシ！！！")
        else:
            self.putlog("> " + value)
            # 入力されていたら対話オブジェクトを実行
            # インプット文字列を引数にしてdialogue()を実行し、応答メッセージを取得
            response = self.pityna.dialogue(value)
            # ピティナの応答メッセージをラベルに出力
            self.ui.labelResponse.setText(response)
            self.putlog(self.prompt() + response)

            # QLineEditクラスのclear()でラインエディットのテキストをクリア
            self.ui.lineEdit.clear()

    def closeEvent(self, event):
        """ウィジェットの閉じるイベントでコールされるイベントハンドラー

        ウィジェットを閉じるclose()実行時にQCloseEventにより呼ばれる

        Args:
            event (QCloseEvent): 閉じるイベント発生時に渡されるQCloseEventオブジェクト
        """
        # メッセージボックスを表示
        reply = QtWidgets.QMessageBox.question(
            self,
            "確認",  # タイトル
            "プログラムを終了しますか",  # メッセージ
            # Yes | No ボタンを表示する
            buttons=QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
        )

        # Yesクリックでウィジェットを閉じ、Noクリックで閉じる処理を無効に
        if reply == QtWidgets.QMessageBox.Yes:
            event.accept()  # イベント続行
        else:
            event.ignore()  # イベント取り消し

    def showResponderName(self):
        self.action = True

    def hiddenResponderName(self):
        self.action = False
