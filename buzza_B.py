import machine  # type: ignore # マシンモジュールをインポートします
import utime  # type: ignore # 時間関連のモジュールをインポートします

# GPIOピン15を出力モードで設定し、ブザーとして使用
buzzer = machine.Pin(15, machine.Pin.OUT)


# 簡単なブザー制御の関数を定義
def Buzz_a_Bit():
    print("DANGER")  # 警告メッセージを表示
    for i in range(15):
        buzzer.toggle()  # ブザーの状態を切り替える
        utime.sleep(0.025)  # 0.025秒間待機
    for i in range(5):
        buzzer.toggle()
        utime.sleep(0.1)  # 0.1秒間待機
    utime.sleep(0.2)  # 0.2秒間待機
    for i in range(15):
        buzzer.toggle()
        utime.sleep(0.025)
    for i in range(5):
        buzzer.toggle()
        utime.sleep(0.1)


# 無限ループでオプションメニューを表示
while True:
    print("0: buzzer off\n1: buzzer on")

    # ここではボタンやスイッチで選択をエミュレートするのが通常
    # 例えば、時間でのデモや任意のイベントを使って選択肢を設定できます。
    # ここではサンプルとして、5秒後に自動的に「1」を選択する処理を行っています。

    # サンプルで選択を決定する（通常はボタンやスイッチなどの入力を使用）
    Buzzer_option = "1"  # ここでは常に"1"を選択、実際はユーザー入力を想定

    if Buzzer_option == "1":
        Buzz_a_Bit()
        print("buzzer ON")
    else:
        buzzer.value(0)
        print("buzzer off")

    utime.sleep(5)  # 次の選択まで5秒待機（サンプルのための一時停止）
