import pityna


def prompt(obj):
    """ピティナのプロンプトを作る関数

    Args:
        obj (object): 呼び出し元のPitynaオブジェクト

    Returns:
        str: ピティナのプロンプト用の文字列
    """
    return obj.get_name() + ":" + obj.get_responder_name() + "> "


print("Pityna System prototype : Pityna")
pityna = pityna.Pityna("pityna")

while True:
    inputs = input(" > ")
    if not inputs:
        print("バイバイ")
        break
    response = pityna.dialogue(inputs)
    print(prompt(pityna), response)
