#関数を定義する
def calculator_bmi(weight, height):
  if height == 0:
    return "Error: Division by zero"
  return weight / height / height
#メインプログラム_文字の表示
num1 = float(input("Enter your weight[kg]:"))
num2 = float(input("Enter your height[cm]:"))
#cmをmに変換吸する
num2 = num2 / 100
#数値を入力させる
print(f"{num1} / {num2} / {num2} = {calculator_bmi(num1, num2)}")
bmi_result = calculator_bmi(num1, num2)
print(f"BMI: {bmi_result:.1f}")