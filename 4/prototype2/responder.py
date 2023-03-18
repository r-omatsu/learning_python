import random


class Responder(object):
    """応答クラスのスーパークラス"""

    def __init__(self, name):
        """Responderオブジェクトの名前をnameに格納

        Args:
            name (str): Responderオブジェクトの名前
        """
        self.name = name

    def response(self, input):
        """オーバーライドを前提としたresponseメソッド

        Args:
            input (str): ユーザーが入力した文字列

        Returns:
            str: 応答メッセージ
        """
        return ""


class RepeatResponder(Responder):
    """オウム返しのためのサブクラス"""

    def response(self, input):
        """responseをオーバーライド、オウム返しの返答をする

        Args:
            input (str): ユーザーが入力した文字列

        Returns:
            str: 応答メッセージ
        """
        return "{}ってなに?".format(input)


class RandomResponder(Responder):
    """ランダムな応答のためのサブクラス"""

    def __init__(self, name):
        """Responderオブジェクトの名前をnameに格納し、
        ランダムに抽出するメッセージを格納したリストを作成する

        Args:
            name (str): Responderオブジェクトの名前
        """
        super().__init__(name)
        # ランダム応答用のメッセージリストを格納
        self.responses = ["いい天気ですね", "君はパリピ？", "100円拾った"]

    def response(self, input):
        """response()をオーバーライドし、ランダムな応答を返す

        Args:
            input (str): ユーザーが入力した文字列

        Returns:
            str: リストからランダムに抽出した文字列
        """
        return random.choice(self.responses)
