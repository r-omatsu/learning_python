class Pityna:
    """ピティナの本体クラス"""

    def __init__(self, name):
        """Pitynaオブジェクトの名前をnameに格納
        Responderオブジェクトを生成してresponderに格納

        Args:
            self(object): 呼び出し元のPitynaオブジェクト
            name(str): Pitynaオブジェクトの名前
        """
        self.name = name
        self.responder = Responder("Repeat")

    def dialogue(self, input):
        """応答オブジェクトのresponse()を呼び出して応答文字列を取得する

        Args:
            self (object): 呼び出し元のPitynaオブジェクト
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
            str: このクラス名
        """
        return self.name


class Responder:
    """応答クラス"""

    def __init__(self, name):
        """Responderオブジェクトの名前をnameに格納

        Args:
            name (str): Responderオブジェクトの名前
        """
        self.name = name

    def response(self, input):
        """応答文字列を作って返す

        Args:
            input (str): ユーザーが入力した文字列

        Returns:
            str: 応答メッセージ
        """
        return "{}ってなに？".format(input)


############################################################
# 実行ブロック                                               #
############################################################
def prompt(obj):
    """ピティナのプロンプトを作る関数

    Args:
        obj (object): 呼び出し元のPitynaオブジェクト

    Returns:
        str: ピティナのプロンプト用文字列
    """
    return obj.get_name() + ":" + obj.get_responder_name() + "> "


print("Pityna System prototype : pityna")
pityna = Pityna("pityna")

while True:
    inputs = input(" > ")
    if not inputs:
        print("バイバイ")
        break
    else:
        response = pityna.dialogue(inputs)
        print(prompt(pityna), response)
