import responder


class Pityna(object):
    """ピティナの本体クラス"""

    def __init__(self, name):
        """Pitynaオブジェクトの名前をnameに格納
        Responderオブジェクトを生成してresponderに格納

        Args:
            name (str): Pitynaオブジェクトの名前
        """
        self.name = name
        self.responder = responder.RandomResponder("Random")

    def dialogue(self, input):
        """応答オブジェクトのresponse()を呼び出して応答文字列を取得する

        Args:
            input (str): ユーザーによって入力された文字列

        Returns:
            str: 応答文字列
        """
        return self.responder.response(input)

    def get_responder_name(self):
        """応答に使用されたオブジェクト名を返す

        Returns:
            str: 応答オブジェクトの名前
        """
        return self.responder.name

    def get_name(self):
        """Pitynaオブジェクトの名前を返す

        Returns:
            str: このクラスの名前
        """
        return self.name
